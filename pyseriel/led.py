import tkinter as tk
from tkinter import ttk
import serial
import threading

class ArduinoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Arduino Serial Communication")
        self.master.geometry("400x350")

        self.serial_port = None

        # Create and place widgets
        self.port_label = ttk.Label(master, text="Port:")
        self.port_label.grid(row=0, column=0, padx=5, pady=5)

        self.port_entry = ttk.Entry(master)
        self.port_entry.grid(row=0, column=1, padx=5, pady=5)
        self.port_entry.insert(0, "COM8")  # Default port, change as needed

        self.connect_button = ttk.Button(master, text="Connect", command=self.connect)
        self.connect_button.grid(row=0, column=2, padx=5, pady=5)

        # Create command buttons
        self.led_on_button = ttk.Button(master, text="LED ON", command=lambda: self.send_command("LED ON"))
        self.led_on_button.grid(row=1, column=0, padx=5, pady=5)

        self.led_off_button = ttk.Button(master, text="LED OFF", command=lambda: self.send_command("LED OFF"))
        self.led_off_button.grid(row=1, column=1, padx=5, pady=5)

        self.status_button = ttk.Button(master, text="STATUS", command=lambda: self.send_command("STATUS"))
        self.status_button.grid(row=1, column=2, padx=5, pady=5)

        self.output_text = tk.Text(master, height=15, width=50)
        self.output_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.output_text.yview)
        self.scrollbar.grid(row=2, column=3, sticky="ns")
        self.output_text.configure(yscrollcommand=self.scrollbar.set)

    def connect(self):
        port = self.port_entry.get()
        try:
            self.serial_port = serial.Serial(port, 9600, timeout=1)
            self.output_text.insert(tk.END, f"Connected to {port}\n")
            threading.Thread(target=self.read_from_arduino, daemon=True).start()
        except serial.SerialException as e:
            self.output_text.insert(tk.END, f"Error: {str(e)}\n")

    def send_command(self, command):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.write(f"{command}\n".encode())
            self.output_text.insert(tk.END, f"Sent: {command}\n")
        else:
            self.output_text.insert(tk.END, "Error: Not connected to Arduino\n")

    def read_from_arduino(self):
        while self.serial_port and self.serial_port.is_open:
            try:
                data = self.serial_port.readline().decode().strip()
                if data:
                    self.output_text.insert(tk.END, f"Received: {data}\n")
                    self.output_text.see(tk.END)
            except serial.SerialException:
                self.output_text.insert(tk.END, "Error: Connection lost\n")
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoGUI(root)
    root.mainloop()