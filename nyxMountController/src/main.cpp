#include <Arduino.h>
#include <StateToggle.h>

StateToggle inBuildLED(2);

void setup() {
  Serial.begin(115200);
  Serial.println("Booted...");
}

void loop() {
  inBuildLED.toggle();
  delay(1500);
}

