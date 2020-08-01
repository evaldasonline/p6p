#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


#define SERVOMIN  150 // This is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // This is the 'maximum' pulse length count (out of 4096)
#define USMIN  600 // This is the rounded 'minimum' microsecond length based on the minimum pulse of 150
#define USMAX  2400 // This is the rounded 'maximum' microsecond length based on the maximum pulse of 600
#define FREQUENCY 50 // Analog servos run at ~50 Hz updates

class Kojos {
  
  Adafruit_PWMServoDriver pwm[2] = { Adafruit_PWMServoDriver(0x40), Adafruit_PWMServoDriver(0x41) };

  public:
  Kojos() {
    pwm[1].begin();    pwm[2].begin();
    pwm[1].setOscillatorFrequency(27000000);
    pwm[1].setPWMFreq(FREQUENCY);  // Analog servos run at ~50 Hz updates
    pwm[2].setOscillatorFrequency(27000000);
    pwm[2].setPWMFreq(FREQUENCY);  // Analog servos run at ~50 Hz updates
    
    Serial.println('Objektas Kojos inicializuotas');
  }

  byte _pin[6][3] = { {10,4,0}, {8,7,6}, {5,9,15}, {6,5,0}, {8,7,9}, {11,10,15} };
  byte _pwm[6][3] = { {1,1,1}, {1,1,1}, {1,1,1}, {2,2,2}, {2,2,2}, {2,2,2} };
  /*int _pos[6][3] = { {370,370,370}, {370,370,370}, {370,370,370}, {370,370,370}, {370,370,370}, {370,370,370} };*/
  int _pos[6][3] = { {90,90,90},{90,90,90},{90,90,90},{90,90,90},{90,90,90},{90,90,90} };


  /**** move_s_to **********************/
  void move_s_to(byte k, byte s, int pos){  /* pajudina sanari i pos */
    this->_pos[k][s] = pos;
    pwm[_pwm[k][s]].setPWM(_pin[k][s], 0, this->kampas(pos));
  }

  int kampas(int angle){ //This function calculates servo's motion angle.
    int pulse_wide, analog_value;
    pulse_wide = map(angle, 0, 180, SERVOMIN, SERVOMAX); //This function get angle from 0 to 180 degrees and map from length minimum value to maximum. 
    analog_value = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
    Serial.println(analog_value);
    return analog_value; //The value this function returns.
  }

};

/*********************************************************************
**********************************************************************
*********************************************************************/

Kojos K;
int globalPauze=10;

void setup() {
  Serial.begin(9600);
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
      int kj = eile[1].toInt();
      int kmp = eile[2].toInt();
      Serial.print("Juda "); Serial.print(kj); Serial.print(" "); Serial.println(kmp);
  }

  
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
