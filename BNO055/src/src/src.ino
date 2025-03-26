#include <Arduino.h>
#include <Wire.h>
#include <math.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define BNO055_SAMPLERATE_DELAY_MS 100
#define G 9.79948
#define PI 3.141592

Adafruit_BNO055 myIMU = Adafruit_BNO055(55, 0x28, &Wire);
uint8_t sysC = 0, accC = 0, gyrC = 0, magC = 0;
unsigned long millis_old;
float dt_secs;

float accX_raw = 0;
float accX_raw_old = 0;
float accX_filtered = 0;
float accX_filtered_old = 0;

float accY_raw = 0;
float accY_raw_old = 0;
float accY_filtered = 0;
float accY_filtered_old = 0;

float accZ_raw = 0;
float accZ_raw_old = 0;
float accZ_filtered = 0;
float accZ_filtered_old = 0;

float gyroX_raw = 0;
float gyroX_raw_old = 0;
float gyroX_filtered = 0;
float gyroX_filtered_old = 0;

float gyroY_raw = 0;
float gyroY_raw_old = 0;
float gyroY_filtered = 0;
float gyroY_filtered_old = 0;

float gyroZ_raw = 0;
float gyroZ_raw_old = 0;
float gyroZ_filtered = 0;
float gyroZ_filtered_old = 0;

float magX_raw = 0, magX_raw_old = 0, magX_filtered = 0, magX_filtered_old = 0;
float magY_raw = 0, magY_raw_old = 0, magY_filtered = 0, magY_filtered_old = 0;
float magZ_raw = 0, magZ_raw_old = 0, magZ_filtered = 0, magZ_filtered_old = 0;

float eulerX_raw = 0;
float eulerX_raw_old = 0;
float eulerX_filtered = 0;
float eulerX_filtered_old = 0;

float gyroX_vel = 0;
float gyroY_vel = 0;
float gyroZ_vel = 0;

float theta_raw = 0;
// float theta_raw_old = 0;
// float theta_filtered = 0;
// float theta_filtered_old = 0;
float phita_raw = 0;
// float phita_raw_old = 0;
// float phita_filtered = 0;
// float phita_filtered_old = 0;
float zeta_raw = 0;
float zeta_raw_old = 0;
float zeta_filtered = 0;
float zeta_filtered_old = 0;

void setup() {
  Wire.begin(21, 22);
  delay(100);

  Serial.begin(115200);
  delay(100);

  myIMU.begin();
  myIMU.setExtCrystalUse(true);
  delay(1000);

  uint8_t system_status = 0, self_test_result = 0, gyrC = 0, system_error = 0;
  myIMU.getSystemStatus(&system_status, &self_test_result, &system_error);
  // Serial.println(system_status);
  // Serial.println(self_test_result);
  // Serial.println(system_error);

  int8_t temp = myIMU.getTemp();
  // Serial.println(temp);

  millis_old = millis();

}

void loop() {
  
  dt_secs = (millis() -millis_old) /1000.0;
  millis_old = millis();

  myIMU.getCalibration(&sysC, &gyrC, &accC, &magC);

  imu::Vector<3> acc = myIMU.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  imu::Vector<3> gyr = myIMU.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
  imu::Vector<3> mag = myIMU.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER);
  imu::Vector<3> euler = myIMU.getVector(Adafruit_BNO055::VECTOR_EULER);

  accX_raw = acc.x();
  accX_filtered = .7 *accX_filtered_old + .15 *accX_raw + .15 *accX_raw_old ;
  accX_filtered_old = accX_filtered;
  accX_raw_old = accX_raw;

  accY_raw = acc.y();
  accY_filtered = .7 *accY_filtered_old + .15 *accY_raw + .15 *accY_raw_old ;
  accY_filtered_old = accY_filtered;
  accY_raw_old = accY_raw;

  accZ_raw = acc.z();
  accZ_filtered = .7 *accZ_filtered_old + .15 *accZ_raw + .15 *accZ_raw_old ;
  accZ_filtered_old = accZ_filtered;
  accZ_raw_old = accZ_raw;

  gyroX_raw = gyr.x();
  gyroX_filtered = .7 *gyroX_filtered_old + .15 *gyroX_raw + .15 *gyroX_raw_old ;
  gyroX_filtered_old = gyroX_filtered;
  gyroX_raw_old = gyroX_raw;

  gyroY_raw = gyr.y();
  gyroY_filtered = .7 *gyroY_filtered_old + .15 *gyroY_raw + .15 *gyroY_raw_old ;
  gyroY_filtered_old = gyroY_filtered;
  gyroY_raw_old = gyroY_raw;

  gyroZ_raw = gyr.z();
  gyroZ_filtered = .7 *gyroZ_filtered_old + .15 *gyroZ_raw + .15 *gyroZ_raw_old ;
  gyroZ_filtered_old = gyroZ_filtered;
  gyroZ_raw_old = gyroZ_raw;

    magX_raw = mag.x();
    magX_filtered = 0.7 * magX_filtered_old + 0.15 * magX_raw + 0.15 * magX_raw_old;
    magX_filtered_old = magX_filtered;
    magX_raw_old = magX_raw;

    magY_raw = -mag.y();
    magY_filtered = 0.7 * magY_filtered_old + 0.15 * magY_raw + 0.15 * magY_raw_old;
    magY_filtered_old = magY_filtered;
    magY_raw_old = magY_raw;

    magZ_raw = mag.z();
    magZ_filtered = 0.7 * magZ_filtered_old + 0.15 * magZ_raw + 0.15 * magZ_raw_old;
    magZ_filtered_old = magZ_filtered;
    magZ_raw_old = magZ_raw;

  eulerX_raw = euler.x();
  eulerX_filtered = .7 *eulerX_filtered_old + .15 *eulerX_raw + .15 *eulerX_raw_old ;
  eulerX_filtered_old = eulerX_filtered;
  eulerX_raw_old = eulerX_raw;

  gyroX_vel = gyroX_vel +gyroX_filtered *dt_secs;
  gyroY_vel = gyroY_vel +gyroY_filtered *dt_secs;
  gyroZ_vel = gyroZ_vel +gyroZ_filtered *dt_secs;

  theta_raw = atan2(accX_filtered /G, accZ_filtered /G) /2.0 /PI *360.0;
  // theta_filtered = .7 *theta_filtered_old + .15 *theta_raw + .15 *theta_raw_old ;
  // theta_filtered_old = theta_filtered;
  // theta_raw_old = theta_raw;

  phita_raw = atan2(accY_filtered /G, accZ_filtered /G) /2.0 /PI *360.0;
  // phita_filtered = .7 *phita_filtered_old + .15 *phita_raw + .15 *phita_raw_old ;
  // phita_filtered_old = phita_filtered;
  // phita_raw_old = phita_raw;

  float theta_raw_rad=theta_raw /360 *(2 *PI);
  float phita_raw_rad=phita_raw /360 *(2 *PI);
  float magX_Comp = magX_filtered *cos(theta_raw_rad) -magY_filtered *sin(phita_raw_rad) *sin(theta_raw_rad) +magZ_filtered *cos(phita_raw_rad) *(theta_raw_rad);
  float magY_comp = magY_filtered *cos(phita_raw_rad) +magZ_filtered *sin(phita_raw_rad);

  zeta_raw = atan2(magY_comp, magX_Comp) / PI *180.0;
  zeta_filtered = .7 *zeta_filtered_old + .15 *zeta_raw + .15 *zeta_raw_old ;
  zeta_filtered_old = zeta_filtered;
  zeta_raw_old = zeta_raw;

  if (zeta_raw < 0) zeta_raw += 360;  // Normalize to [0, 360]

  Serial.printf("%.2f, %.2f, %.2f, %.1f, %.1f, %.1f, %u, %u, %u, %u, %.1f, %.1f, %.1f, %.1f\n", accX_filtered, accY_filtered, accZ_filtered, gyroX_vel, gyroY_vel, gyroZ_vel*-1, sysC, accC, gyrC, magC, theta_raw, phita_raw, zeta_filtered, eulerX_filtered);


  delay(BNO055_SAMPLERATE_DELAY_MS);
}
