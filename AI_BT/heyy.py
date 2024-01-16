import serial
import time
import tkinter as tk

# This code is to connect to the arduino  
# rhis code will send input to the serial panel of arduino ide 

ser = serial.Serial('COM17',115200,timeout=0) # change according to your data

root = tk.Tk()
root.title("Tkinter exapmle")
root.geometry("400x230") # size of the display

root.resizable(True,True)

def on_button_click():
    ser.write(b'o')

button2=tk.Button(root, text="led on", command=on_button_click)
button2.place(x=130, y=90) # place of switch

def on_button():
    ser.write(b'f')

button2=tk.Button(root, text="led off", command=on_button)
button2.place(x=130, y=50)

root.mainloop()