
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 8     // Digital pin connected to the DHT sensor 
#define DHTTYPE    DHT11     // DHT 11

DHT_Unified dht(DHTPIN, DHTTYPE);
uint32_t delayMS=2000;
float t;
float h;

void setup() {
  Serial.begin(9600);
  // Initialize device.
  dht.begin();
  // sensor_t sensor;
  // dht.temperature().getSensor(&sensor);
  // dht.humidity().getSensor(&sensor);
}

float  get_temp() {
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  if (isnan(event.temperature)) {
    return 999;
    Serial.println(F("Error reading temperature!"));
  }
  else {
    return event.temperature;
  }
}
float  get_hum() {
  // Get humidity event and print its value.
  sensors_event_t event;
  dht.humidity().getEvent(&event);
  if (isnan(event.relative_humidity)) {
    return 999;
    Serial.println(F("Error reading humidity!"));
  }
  else {
    return event.relative_humidity;
  }
}

void print_output (float  te, float  hu) {
    Serial.println();
    Serial.print(F("Humidity: "));
    Serial.print(hu);
    Serial.println(F("%"));
    Serial.print(F("Temperature: "));
    Serial.print(te);
    Serial.println(F("°C"));

}
void loop() {
  // Delay between measurements.
  delay(delayMS);
  // Get temperature event and print its value.
  t=get_temp();
  h=get_hum();
  print_output(t,h);
  
}
