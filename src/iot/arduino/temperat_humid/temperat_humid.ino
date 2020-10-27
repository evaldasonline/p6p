
#include<SPI.h>                   // spi library for connecting nrf
#include <Wire.h>                             // i2c libary fro 16x2 lcd display
#include<RF24.h>                  // nrf library
#include <printf.h>

int dot=0;
  //  const uint64_t pipe = 0xE0E0F1F1E0LL ;    // pipe address same as sender i.e. raspberry pi
  const uint64_t pipe = 0xE8E8F0F0E1LL ;    // pipe address same as sender i.e. raspberry pi

RF24 radio(9, 10) ;  // ce, csn pins    

void setup(void) {
  printf_begin();
  while (!Serial) ;
  Serial.begin(9600) ;     // start serial monitor baud rate
  Serial.print("Serial up.. ") ; // debug message
  Serial.print(" Setting Up radio.. ") ; // debug message
  radio.begin();            // start radio at ce csn pin 9 and 10
  radio.setPALevel(RF24_PA_HIGH) ;   // set power level   RF24_PA_MIN, RF24_PA_LOW, RF24_PA_HIGH and RF24_PA_MAX
  radio.setChannel(0x76) ;            // set chanel at 76
  radio.setDataRate( RF24_250KBPS );
  radio.openReadingPipe(1, pipe) ;        // start reading pipe 
  radio.enableDynamicPayloads() ;
  radio.printDetails();
  radio.powerUp() ;          
  radio.startListening() ;        // start listening forever
  
  Serial.println(" Radio on..") ; // debug message
}

void loop(void) {

  char receivedMessage[32] = {0} ;   // set incmng message for 32 bytes
  Serial.print(".") ; // debug message
  dot=dot+1;
  if (dot>60) {
    Serial.println(";");
    dot=0;
  }
  if (radio.available()) {       // check if message is coming
    radio.read(receivedMessage, sizeof(receivedMessage));    // read the message and save
    Serial.println("!") ; 
    String stringMessage(receivedMessage) ;     // change char to string
    Serial.println(receivedMessage) ;    // print message on serial monitor 
    // Serial.println("Turning off the radio.") ;   // print message on serial monitor
    // radio.stopListening() ;   // stop listening radio
    delay(1000);    // delay of 1 second 
  }
  delay(1000);
}
