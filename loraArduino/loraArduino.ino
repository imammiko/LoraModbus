#include <SPI.h>
#include <LoRa.h>
#include "DHT.h"
#define DHTPIN 5    
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
int counter = 0;
String dataLora;
void setup() {
  Serial.begin(9600);
  while (!Serial);
   dht.begin();
  //Serial.println("LoRa Sender");

  if (!LoRa.begin(434E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  float mq = analogRead(A0); 
  //float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  //float t = dht.readTemperature();
  //if (isnan(h) || isnan(t) ) {
  //  Serial.println(F("Failed to read from DHT sensor!"));
 //   return;
 // }
  // send packet
  LoRa.beginPacket();
  dataLora += "slave1";
  dataLora+="/";
  dataLora+="t:";
  dataLora += 123;
  dataLora+="/";
  dataLora+="h:";
  dataLora += 123;
  dataLora+="/";
  dataLora+="mq:";
  dataLora+=mq;
  dataLora+="/";
  dataLora+="la:";
  dataLora+="latitude";
  dataLora+="/";
  dataLora+="lo:";
  dataLora+="lotitude";
  dataLora+="/";
  
  
  
  
  
  LoRa.print(dataLora);
  dataLora ="";
  LoRa.endPacket();
  
  counter++;

  delay(1000);
}
