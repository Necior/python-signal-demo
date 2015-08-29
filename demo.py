#!/usr/bin/env python3

import signal
import sys


def handle_SIGUSR1(signum, stack):
    print('Received SIGUSR1')


def graceful_exit(signum, stack):
    print()
    sys.exit('Graceful exit')

signal.signal(signal.SIGUSR1, handle_SIGUSR1)
signal.signal(signal.SIGINT, graceful_exit)

while True:
    signal.pause()
