#include "nyxNetConnection.h"
#include <WiFi.h>

void connectNyxNet(const char* ssid, const char* password) {
  Serial.print("Connecting to Wi-Fi");
  WiFi.begin(ssid, password);

  // Wait for the connection to succeed
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);  // Wait for 1 second
    Serial.print(".");
  }

  // Print the IP address once connected
  Serial.println();
  Serial.println("Connected to Wi-Fi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}
