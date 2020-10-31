// nRF24 radijai
#include <SPI.h>
#include "RF24.h"                

// temperaturos davikliui
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 7     // temperaturos ir dregmes sensorius
#define DHTTYPE    DHT11     // sensoriaus tipas. kazkodel turiu toki

const uint64_t pipe = 0xE0E0E0E0E1LL ;    // pipe address same as sender i.e. raspberry pi

RF24 radio(9, 10) ;  // ce, csn pins    
DHT_Unified dht(DHTPIN, DHTTYPE);

float t;
float h;

void setup() {
  Serial.begin(9600);
  while (!Serial) ;
  Serial.print("Setup initializing: ");
  Serial.print("sensor...");
  dht.begin();   // Initialize temperature sensor device.
  
  Serial.print("radio...");
  radio.begin();            // start radio at ce csn pin 9 and 10
  radio.setPALevel(RF24_PA_HIGH) ;   // set power level   RF24_PA_MIN, RF24_PA_LOW, RF24_PA_HIGH and RF24_PA_MAX
  radio.setChannel(0x76) ;            // set chanel at 76
  radio.setDataRate( RF24_1MBPS );
  radio.openReadingPipe(1, pipe) ;        // start reading pipe 
  radio.enableDynamicPayloads() ;
  radio.powerUp() ;          
  Serial.println("is on");
}

float  get_temp() { 
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  float rez=event.temperature;
  if (isnan(event.temperature)) {    rez = 999;   }
  return rez;
}
float  get_hum() {
  // Get humidity event and print its value.
  sensors_event_t event;
  dht.humidity().getEvent(&event);
  float rez=event.relative_humidity;
  if (isnan(event.relative_humidity)) {    rez = 999;  }
  return rez;
}
void print_output_serial (float  te, float  hu) {
  Serial.print(te); Serial.print("°C\t"); Serial.print(hu); Serial.println("%");
}

String to_string(float te, float hu) {
  String ste=String(te);  String shu=String(hu);  String rez=String("C" + ste + "&" + "H" + shu + "^");  return rez;
}


/////////////////////////////////////////////////////////////////////////////////
void loop() {
//   radio.startListening() ;        // start listening forever
  
  t=get_temp();
  h=get_hum();
 //  print_output_serial(t,h);
  String eile = to_string(t,h);

  Serial.print("Sending: ");
  Serial.print(eile);
  radio.write(&eile, sizeof(eile));
  Serial.println("  ..");  
  
  delay(5000);
}
