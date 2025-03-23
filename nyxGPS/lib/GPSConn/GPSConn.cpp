#include <Arduino.h>

HardwareSerial gpsSerial(2); // Use UART2 (RX2 = GPIO16, TX2 = GPIO17)

extern String GPSLocData;

void initializeGPS(int rxPin, int txPin) {
    gpsSerial.begin(9600, SERIAL_8N1, rxPin, txPin); // L76G default baud rate is 9600
    Serial.println("Waveshare L76G GPS Initialized...");
}

void pollGPSData() {
    if (gpsSerial.available()) {
        String gpsData = gpsSerial.readStringUntil('\n');
        if (gpsData.startsWith("$GNGGA")) {
            GPSLocData = gpsData;
        }
    }
}