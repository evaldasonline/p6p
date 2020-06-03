#include <Servo.h> 

String readString, kampas;
char koja;
int sPin[]= {0,1,2,3}; 
Servo Se[4]; 


void setup() { 
  Serial.begin(9600);
  Serial.println("Pradeda");
  for (int s=0; s<4; s++) {
     Se[s].attach(sPin[s]); 
  }
  juda(0, 90,5);
  juda(1, 90,5);
  juda(2, 90,5);
  juda(3, 90,5);
  
}

/*************************************/

void juda(int k, int l, int p) {
  Se[k].write(l);
  delay(p);
} // end juda()

/*************************************/


void loop(){ 
  while (Serial.available()) {
    int c = Serial.read();  //gets one byte from serial buffer
    readString += (char)c; //makes the String readString
    delay(2);  
  }

  if (readString.length() >0) {
    // Serial.println(readString);  
    koja=readString[0];
    kampas=readString.substring(1);
    int ll = kampas.toInt();
    int kk=(int)koja-48; 
  Serial.println (kk);
  Serial.println (ll );
    juda(kk,ll,10);
    koja =""; kampas=""; readString="";
  }
}
