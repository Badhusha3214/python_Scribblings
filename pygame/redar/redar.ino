#include <Servo.h>

#define TRIG_PIN 9
#define ECHO_PIN 10
#define SERVO_PIN 11

Servo myServo;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  myServo.attach(SERVO_PIN);
}

void loop() {
  for (int angle = 0; angle <= 180; angle += 5) {
    myServo.write(angle);
    delay(100);
    long distance = measureDistance();
    Serial.print(angle);
    Serial.print(",");
    Serial.println(distance);
  }
  
  for (int angle = 180; angle > 0; angle -= 5) {
    myServo.write(angle);
    delay(100);
    long distance = measureDistance();
    Serial.print(angle);
    Serial.print(",");
    Serial.println(distance);
  }
}

long measureDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  long duration = pulseIn(ECHO_PIN, HIGH);
  long distance = duration * 0.034 / 2;
  
  return distance;
}