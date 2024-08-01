# Arduino Serial Communication GUI

This project demonstrates a simple serial communication setup between a Python GUI and an Arduino board. It allows users to send commands to control an LED on the Arduino and receive status updates through a user-friendly interface.

## Components

1. **Python GUI**: A graphical interface built with tkinter that allows users to connect to the Arduino and send commands.
2. **Arduino Sketch**: A program running on the Arduino that receives commands, controls the LED, and sends back status information.

## Requirements

### For the Python GUI:
- Python 3.x
- pyserial library

### For the Arduino:
- Arduino board (e.g., Arduino Uno)
- Arduino IDE

## Setup

### Python GUI Setup:
1. Ensure you have Python 3.x installed on your system.
2. Install the pyserial library:
   ```
   pip install pyserial
   ```
3. Save the Python script as `arduino_gui.py`.

### Arduino Setup:
1. Connect your Arduino board to your computer via USB.
2. Open the Arduino IDE.
3. Copy the Arduino sketch and paste it into a new sketch in the Arduino IDE.
4. Upload the sketch to your Arduino board.

## Usage

1. Run the Python script:
   ```
   python led.py
   ```
2. In the GUI:
   - Enter the correct COM port for your Arduino (e.g., COM8 for Windows, /dev/ttyUSB0 for Linux).
   - Click "Connect" to establish a connection with the Arduino.
   - Use the buttons to send commands:
     - "LED ON": Turns on the LED
     - "LED OFF": Turns off the LED
     - "STATUS": Requests the current state of the LED
   - The sent commands and responses from the Arduino will be displayed in the text area.

## Troubleshooting

- If you can't connect to the Arduino, make sure you've selected the correct COM port.
- Ensure that no other program is currently using the serial port.
- If you're not receiving responses, check that the baud rate in the Arduino sketch matches the one in the Python script (9600 by default).

## Extending the Project

You can extend this project by:
- Adding more commands to control additional components on the Arduino.
- Implementing data logging functionality in the GUI.
- Adding graphs or visual representations of data from sensors connected to the Arduino.

## License

This project is open-source and available under the MIT License.