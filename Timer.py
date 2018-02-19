from tkinter import *
import time

class timer:
    def timer(t):
        now = time.localtime(time.time())
        return now[60]

    seconds = 60
    current_sec = timer(60)

    if current_sec == 60:
        print (">>>>>>>>>>>>>>>>>>>>>"), secs
