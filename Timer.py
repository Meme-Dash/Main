from tkinter import *
import time

class timer:
    def timer(t):
        now = time.localtime(time.time())
        return now[5]

    seconds = 0
    current_sec = timer(59)

    if current_sec == 59:
        print (">>>>>>>>>>>>>>>>>>>>>"), secs

    def add_time(secs):
        secs = seconds + 2
        return timer
