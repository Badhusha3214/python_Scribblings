import serial
import time
import tkinter as tk

ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=0)  


    
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("400x230")


root.resizable(True, True)

#label = tk.Label(root, text="Selecte file",bg='#ffbd33')
#label.place(x=130, y=140)

def on_button_click():
    ser.write(b"o")
    




button2 = tk.Button(root, text="    Convert File    ", command=on_button_click, bg='#131313',fg="#ffffff")
button2.place(x=130, y=90)

# Start the main event loop
root.mainloop()




