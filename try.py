# -*- coding: utf-8 -*-

import threading


def fun_timer():
    print('Hello Timer!')
    timer = threading.Timer(0.01, fun_timer)
    timer.start()


fun_timer()