# Import all classes and functions from the tkinter library
from tkinter import*

# Import the font module from the tkinter library
import tkinter.font

# Import the LED class from the gpiozero library
from gpiozero import LED

# Import the RPi.GPIO module for GPIO setup
import RPi.GPIO

# Set the GPIO mode to use BCM numbering
RPi.GPIO.setmode(RPI.GPIO.BCM)

# Initialize LEDs on GPIO pins 20, 16, and 21
redled=LED(20)
blueled=LED(16)
greenled=LED(21)

# Create the main window for the GUI
win=Tk()

# Set the title of the GUI window
win.title("LED's CONTROL")

# Create a custom font named 'myFont'
myFont=tkinter.font.Font(family='Helvetica', size=12, weight='bold')

# Define a function to control the Red LED
def RedLED():
    # Check if the Red LED is currently lit
    if redled.is_lit:
        # If lit, turn it off and update button text
        redled.off()
        RedLedButton["text"]="Turn Red Led On"
    else:
        # If not lit, turn it on and update button text
        redled.on()
        RedLedButton["text"]="Turn Off Red Led"
        # Turn off other LEDs and update their button texts
        blueled.off()
        BlueLedButton["text"]="Turn Off Blue Led"
        greenled.off()
        GreenLedButton["text"]="Turn Off Green Led"

# Define a function to control the Blue LED
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

# Define a function to control the Green LED
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

# Define a function to clean up GPIO and exit the GUI
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Create buttons for Red, Blue, and Green LEDs
RedLedButton=Button(win, text='Turn Red Led On', font=myFont, command=RedLED,height=4,width=24)
RedLedButton.grid(row=0,column=1)

BlueLedButton=Button(win, text='Turn Blue Led On', font=myFont, command=BlueLED,height=4,width=24)
BlueLedButton.grid(row=2,column=1)

GreenLedButton=Button(win, text='Turn Green Led On', font=myFont, command=GreenLED,height=4,width=24)
GreenLedButton.grid(row=4,column=1)

# Create an Exit button to close the GUI
exitButton=Button(win, text='Exit', font=myFont, command=close,height=1,width=7)
exitButton.grid(row=5,column=1)

# Set a protocol handler to call the 'close' function when the window is closed
win.protocol("WM_Delete_Window", close)

# Start the main event loop of the GUI
win.mainloop()
