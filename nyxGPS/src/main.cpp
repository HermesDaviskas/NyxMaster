#include <WiFi.h>
#include <WebServer.h>
#include "GPSConn.h"  // Include your GPS module library
#include <nyxNetConnection.h>  // Include your Wi-Fi connection module

String GPSLocData = "No data";

void setup() {
    Serial.begin(9600);
    initializeGPS(26, 27);
}

void loop() {
    
    Serial.println(GPSLocData);
    pollGPSData();

    delay(1000);
}
