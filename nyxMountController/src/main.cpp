#include <Wire.h>
#include <Adafruit_LSM303_Accel.h>
#include <Adafruit_LSM303_Mag.h>
#include <Adafruit_Sensor.h>

Adafruit_LSM303_Accel_Unified accel = Adafruit_LSM303_Accel_Unified(54321);
Adafruit_LSM303_Mag_Unified mag = Adafruit_LSM303_Mag_Unified(12345);

void setup() {
    Serial.begin(115200);
    Wire.begin();

    // Initialize Accelerometer
    if (!accel.begin()) {
        Serial.println("Could not find LSM303 Accelerometer!");
        while (1);
    } else {
        Serial.println("LSM303 Accelerometer detected.");
    }

    // Initialize Magnetometer
    if (!mag.begin()) {
        Serial.println("Could not find LSM303 Magnetometer!");
        while (1);
    } else {
        Serial.println("LSM303 Magnetometer detected.");
    }
}

void loop() {
    // Read Accelerometer Data
    sensors_event_t accelEvent;
    accel.getEvent(&accelEvent);

    Serial.print("Accel X: "); Serial.print(accelEvent.acceleration.x); Serial.print(" m/s², ");
    Serial.print("Y: "); Serial.print(accelEvent.acceleration.y); Serial.print(" m/s², ");
    Serial.print("Z: "); Serial.println(accelEvent.acceleration.z); Serial.print(" m/s²");

    // Read Magnetometer Data
    sensors_event_t magEvent;
    mag.getEvent(&magEvent);

    Serial.print("Mag X: "); Serial.print(magEvent.magnetic.x); Serial.print(" µT, ");
    Serial.print("Y: "); Serial.print(magEvent.magnetic.y); Serial.print(" µT, ");
    Serial.print("Z: "); Serial.println(magEvent.magnetic.z); Serial.print(" µT");

    Serial.println("----------------------------");
    delay(1000);
}
