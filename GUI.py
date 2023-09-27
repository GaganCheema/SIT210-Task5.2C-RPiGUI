from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPI.GPIO.BCM)

redled=LED(20)
blueled=LED(16)
greenled=LED(21)

win=Tk()
win.title("LED's CONTROL")
myFont=tkinter.font.Font(family='Helvetica', size=12, weight='bold')

def RedLED():
    if redled.is_lit:
        redled.off()
        RedLedButton["text"]="Turn Red Led On"
    else:
        redled.on()
        RedLedButton["text"]="Turn Off Red Led"
        blueled.off()
        BlueLedButton["text"]="Turn Off Blue Led"
        greenled.off()
        GreenLedButton["text"]="Turn Off Green Led"
    
def BlueLED():
    if blueled.is_lit:
        blueled.off()
        BlueLedButton["text"]="Turn Blue Led On"
    else:
        redled.off()
        RedLedButton["text"]="Turn Off Red Led"
        blueled.on()
        BlueLedButton["text"]="Turn Off Blue Led"
        greenled.off()
        GreenLedButton["text"]="Turn Off Green Led"

def GreenLED():
    if greenled.is_lit:
        greenled.off()
        GreenLedButton["text"]="Turn Green Led On"
    else:
        redled.off()
        RedLedButton["text"]="Turn Off Red Led"
        blueled.off()
        BlueLedButton["text"]="Turn Off Blue Led"
        greenled.on()
        GreenLedButton["text"]="Turn Off Green Led"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

RedLedButton=Button(win, text='Turn Red Led On', font=myFont, command=RedLED,height=4,width=24)
RedLedButton.grid(row=0,column=1)

BlueLedButton=Button(win, text='Turn Blue Led On', font=myFont, command=BlueLED,height=4,width=24)
BlueLedButton.grid(row=2,column=1)

GreenLedButton=Button(win, text='Turn Green Led On', font=myFont, command=GreenLED,height=4,width=24)
GreenLedButton.grid(row=4,column=1)

exitButton=Button(win, text='Exit', font=myFont, command=close,height=1,width=7)
exitButton.grid(row=5,column=1)

win.protocol("WM_Delete_Window", close)

win.mainloop()
