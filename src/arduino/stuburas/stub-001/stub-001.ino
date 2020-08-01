#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm1 = Adafruit_PWMServoDriver(0x40);
Adafruit_PWMServoDriver pwm2 = Adafruit_PWMServoDriver(0x41);

#define SERVOMIN  150 // This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // This is the 'maximum' pulse length count (out of 4096)
#define USMIN  600 // This is the rounded 'minimum' microsecond length based on the minimum pulse of 150
#define USMAX  2400 // This is the rounded 'maximum' microsecond length based on the maximum pulse of 600
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates

int globalPauze=10;
uint8_t s = 0;
uint8_t servonum = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("8 channel Servo test!");

  pwm1.begin();
  pwm2.begin();

  pwm1.setOscillatorFrequency(27000000);
  pwm1.setPWMFreq(SERVO_FREQ);  // Analog servos run at ~50 Hz updates
  pwm2.setOscillatorFrequency(27000000);
  pwm2.setPWMFreq(SERVO_FREQ);  // Analog servos run at ~50 Hz updates

  delay(10);
}
/**************************************************************************/

void komanda(String st) {
  String eile[10];
  char tipas=char(st[0]);
  
  // iskaidome i dalis komanda
  // pirmas - vienos raides komandos inicializatorius
  eile[0] = st[0]; st=st.substring(1); st.trim();
    //toliau - skirtukas yra tarpas
  int i=0;
  while (st.length() > 0) {
    i++;
    int t=st.indexOf(" "); if (t<0) {t=st.length();}
    eile[i]=st.substring(0,t); eile[i].trim();
    st=st.substring(t); st.trim();
  }
  Serial.print(tipas); Serial.print("% "); 
  for (int x=0; x<=i; x++) {
    Serial.print("eile[" + String(x) + "]=" + eile[x] + ";   ");
  }; Serial.println();

// eile[] - sudeti komandos parametrai

  if (tipas=='1') {  //vieno servo pajudinimas
      kj = eile[1].toInt();
      int kmp = eile[2].toInt();
      Serial.print("Juda "); Serial.print(kj); Serial.print(" "); Serial.println(kmp);
  }

  
  if (tipas=='s') {
      kj = eile[1].toInt();
      int kmp = eile[2].toInt();
      Serial.print("Juda "); Serial.print(kj); Serial.print(" "); Serial.println(kmp);
      KOJA[kj]=kmp; 
      updateOne( kj,globalPauze );
  } // s  
  
  if (tipas=='k') {
      kj = eile[1].toInt();
      int kmp = eile[2].toInt();
      Serial.print("Juda "); Serial.print(kj); Serial.print(" "); Serial.println(kmp);
      KOJA[kj]=kmp; 
      updateOne( kj,globalPauze );
  } // k

  if (tipas=='d') {  // globalios pauzes nustatymas
      globalPauze = eile[1].toInt();
      Serial.print("globali pauze = "); Serial.println(globalPauze);
  } //d


  if (tipas=='m') {
    kj=eile[1].toInt();  //kiek kartu sukti cikla
    for (int x=0; x<kj; x++) {
      for (int j=2; j<=i; j++) {
        int kmp = eile[j].toInt();
        move_to_pattern( kmp );
      }
      
    }
  } //komanderis: m

  
} //end komanda
/**********************************************************/

void loop(){ 
  String readString;
  char c;
  
  while (Serial.available()) {
    c = Serial.read();  //gets one byte from serial buffer
    readString += c; //makes the String readString
    delay(2);  //slow looping to allow buffer to fill with next character
  }

  if (readString.length() >0) {
    komanda(readString);
  }
}
