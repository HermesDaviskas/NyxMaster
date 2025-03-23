#ifndef GPSCONN_H
#define GPSCONN_H

#include <ArduinoJson.h>

// Function to initialize the GPS
void initializeGPS(int rxPin, int txPin);

// Function to read GPS data and store it
void pollGPSData();


#endif
