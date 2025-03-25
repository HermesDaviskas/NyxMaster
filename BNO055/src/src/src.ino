#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 myIMU = Adafruit_BNO055(55, 0x28, &Wire);
uint8_t sysC = 0, accC = 0, gyrC = 0, magC = 0;

void setup() {
  Wire.begin(21, 22);
  delay(100);

  Serial.begin(115200);
  delay(100);

  myIMU.begin();
  myIMU.setExtCrystalUse(true);
  delay(1000);

  int8_t temp = myIMU.getTemp();
  Serial.println(temp);
}

void loop() {
  myIMU.getCalibration(&sysC, &gyrC, &accC, &magC);

  imu::Vector<3> acc = myIMU.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  imu::Vector<3> gyr = myIMU.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);

  Serial.printf("%.1f, %.1f, %.1f, %.1f, %.1f, %.1f, %u, %u, %u, %u\n", acc.x(), acc.y(), acc.z(), gyr.x(), gyr.y(), gyr.z(), sysC, accC, gyrC, magC);

  delay(BNO055_SAMPLERATE_DELAY_MS);
}
