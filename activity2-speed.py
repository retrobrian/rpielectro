# Original gui_slider written by Simon Monk
# Updates and comments by Brian Cox
# Updated 11-8-18
# Expecting Python 3

from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
pwm = GPIO.PWM(24, 500)
pwm.start(0)

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=100, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, duty):
        pwm.ChangeDutyCycle(float(duty))

root = Tk()
root.wm_title('PWM Percentage')
app = App(root)
root.geometry("400x50+0+0")
root.mainloop()

