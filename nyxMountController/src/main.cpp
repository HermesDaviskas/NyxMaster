#include <Arduino.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Booted...");
  pinMode(2, OUTPUT);
}

void loop() {
  digitalWrite(2, HIGH);  // Turn LED on
  delay(500);
  digitalWrite(2, LOW);   // Turn LED off
  delay(500);
}