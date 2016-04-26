#!/usr/bin/env python

from setuptools import setup

setup(
    name='boxpi',
    version='1.0a1',
    description='PWM',
    author='Joar Wandborg',
    author_email='joar+boxpi@wandb.org',
    license='MIT',
    entry_points={
        'console_scripts': [
            'boxpi=boxpi:main',
        ]
    },
    packages=['boxpi'],
    install_requires=['RPi.GPIO', 'colorlog'],
)
