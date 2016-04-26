import argparse
import logging
from itertools import cycle

import RPi.GPIO as GPIO
import time

import math

from boxpi import logconf

_log = logging.getLogger(__name__)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--max', default=100, type=float)
    parser.add_argument('--min', default=20, type=float)
    parser.add_argument('--freq', default=25000, type=float)
    parser.add_argument('-i', '--interval', default=5, type=float)
    parser.add_argument('-p', '--pin', default=12, type=int)
    parser.add_argument('--sweep', action='store_true')

    args = parser.parse_args(args=argv)

    level = logging.DEBUG if args.verbose else logging.INFO

    logconf.configure_logging(level=level)

    pwm_alternate_duty(args.pin, args.min, args.max, args.interval,
                       args.sweep, args.freq)


def pwm_alternate_duty(pin, min_duty, max_duty, interval, sweep, freq=25000):
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)

        pwm = GPIO.PWM(pin, freq)
        _log.info('Starting PWM on pin=%r, freq=%r', pin, freq)

        pwm.start(min_duty)
        if sweep:
            duties = range(math.floor(min_duty), math.ceil(max_duty) + 1, 10)
            while True:
                for duty in duties:
                    set_duty(pwm, duty)
                    sleep(interval / (len(duties)))
        else:
            for duty in cycle([min_duty, max_duty]):
                set_duty(pwm, duty)
                sleep(interval)

        pwm.stop()  # stop the PWM output
    finally:
        GPIO.cleanup()  # when your program exits, tidy up after yourself


def sleep(s):
    _log.debug('Sleeping for %d seconds', s)
    time.sleep(s)


def set_duty(pwm, duty):
    _log.info('Setting duty=%r', duty)
    pwm.ChangeDutyCycle(duty)

if __name__ == '__main__':
    main()
