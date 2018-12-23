#!/user/bin/env python
# -*-coding:utf-8 -*-.

import time
def fun(n):
    print(n)
    time.sleep(1)
    fun(n-1)


fun(10)