# servo written by Simon Monk
# comments by Brian Cox
# Updated 11-6-18


from Tkinter import *       #Load Python's GUI package
import RPi.GPIO as GPIO     #Load module to support RPi's GPIO pins and create object called GPIO
import time                 #Load module that allows RPi to work with time

GPIO.setmode(GPIO.BCM)      #Configures GPIO numbering system
GPIO.setup(18, GPIO.OUT)    #Configures GPIO pin 18 as an output
pwm = GPIO.PWM(18, 100)     #Creat
pwm.start(5)

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()
