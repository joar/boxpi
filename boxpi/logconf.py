import logging
import colorlog


def configure_logging(level=logging.WARNING):
    formatter = colorlog.ColoredFormatter(
        '%(asctime)s '
        '%(log_color)s%(levelname)8s%(reset)s '
        '%(name)s '
        '%(bold)s%(funcName)s%(reset)s'
        ': %(message)s',
        log_colors=dict(
            DEBUG='blue',
            INFO='green',
            WARNING='yellow',
            ERROR='red',
            CRITICAL='red,bg_white'
        ))

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(level)
    root.addHandler(handler)
