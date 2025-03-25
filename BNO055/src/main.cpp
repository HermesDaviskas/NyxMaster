#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 myIMU = Adafruit_BNO055(55, 0x28);

void setup() {
  Wire.begin(21, 22);
  delay(100);

  Serial.begin(115200);
  delay(100);

  myIMU.begin();
  myIMU.setExtCrystalUse(true);
  delay(100);
}

void loop() {

  int8_t temp = myIMU.getTemp();
  Serial.println(temp);

}