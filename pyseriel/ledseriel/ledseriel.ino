const int ledPin = 13;  // Built-in LED pin
String inputString = "";  // String to hold incoming data
boolean stringComplete = false;  // Whether the string is complete

void setup() {
  Serial.begin(9600);  // Initialize serial communication at 9600 bps
  pinMode(ledPin, OUTPUT);
  inputString.reserve(200);  // Reserve 200 bytes for the inputString
}

void loop() {
  // Print the string when a newline arrives:
  if (stringComplete) {
    processCommand(inputString);
    // Clear the string:
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    // Get the new byte:
    char inChar = (char)Serial.read();
    // Add it to the inputString:
    inputString += inChar;
    // If the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}

void processCommand(String command) {
  command.trim();  // Remove any leading or trailing whitespace
  
  if (command == "LED ON") {
    digitalWrite(ledPin, HIGH);
    Serial.println("LED turned ON");
  }
  else if (command == "LED OFF") {
    digitalWrite(ledPin, LOW);
    Serial.println("LED turned OFF");
  }
  else if (command == "STATUS") {
    if (digitalRead(ledPin) == HIGH) {
      Serial.println("LED is ON");
    } else {
      Serial.println("LED is OFF");
    }
  }
  else {
    Serial.println("Unknown command: " + command);
  }
}