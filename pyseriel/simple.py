import tkinter as tk
import serial

class ArduinoLEDControl:
    def __init__(self, master):
        self.master = master
        self.master.title("Arduino LED Control")
        self.master.geometry("300x150")

        self.serial_port = None

        self.create_widgets()
        self.connect_to_arduino()

    def create_widgets(self):
        # LED ON button
        self.on_button = tk.Button(self.master, text="LED ON", command=lambda: self.send_command("LED ON"))
        self.on_button.pack(pady=20)

        # LED OFF button
        self.off_button = tk.Button(self.master, text="LED OFF", command=lambda: self.send_command("LED OFF"))
        self.off_button.pack(pady=20)

    def connect_to_arduino(self):
        try:
            self.serial_port = serial.Serial('COM8', 9600, timeout=1)  # Change 'COM8' to your Arduino port
            print("Connected to Arduino")
        except serial.SerialException as e:
            print(f"Failed to connect to Arduino: {e}")

    def send_command(self, command):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.write(f"{command}\n".encode())
            print(f"Sent: {command}")
        else:
            print("Error: Not connected to Arduino")

if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoLEDControl(root)
    root.mainloop()