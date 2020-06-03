#include <Servo.h> 
const int maxkoja=3;
const int maxpattern=8;

int dKoja[maxpattern][maxkoja] = { {90,20,120}, {90, 60, 70}, {90, 40, 70}, {120, 40, 70}, {120, 60, 70}, {60, 60, 70}, {60, 40, 70}, {90, 40, 70}  };
int sPin[] = {0,1,2}; 
int KOJA[maxkoja]; 
int oldKOJA[maxkoja];
int globalPauze=10;
Servo Se[maxkoja]; 


void setup() { 
  Serial.begin(9600);
  Serial.println("Pradeda");
  for (int s=0; s<maxkoja; s++) {
     Se[s].attach(sPin[s]); 
     KOJA[s]=dKoja[0][s];
     oldKOJA[s]=dKoja[0][s];
     
     updateOne(s, -1);
  }
}  //end Setup
/*************************************/
int sign(int x) {
  if (x<0) return -1;
  return 1;
}
/*************************************/
void updateOne(int k, int d) {
  int o,n;
  o=oldKOJA[k]; n=KOJA[k];
  
  if (d== -1) {   //jei inicializuojame - permesti tiesiai i pozicija
    Se[k].write(KOJA[k]);  
  } 
  else {  if (o!=n) { //letas perejimas nuo senos i nauja pozicija
    Serial.print(k); Serial.print(": "); Serial.print(o); Serial.print(" -> "); Serial.print(n); 
    if (o>n) { 
      for (int x=o; x>n; x--) {
        Se[k].write(x); delay(d); 
        Serial.print("<"); 
      }
    } else {
      for (int x=o; x<n; x++) {
        Se[k].write(x); delay(d); 
        Serial.print(">"); 
      }
    }
    Serial.println("!"); 
  }
  oldKOJA[k]=KOJA[k];
  }//tikrinimas ar lygus
}  //end updateOne
/*****************************************/
void updateAll(int d) {
  for (int s=0; s<=maxkoja; s++) {
    updateOne(s,d);
  }
}  //end updateAll
/*******************************************/
void move_to_pattern(int p) {
  int dif[maxkoja];
  int sgn[maxkoja];
  int absdif[maxkoja];
  int maxdif=0;
  int s;
  bool bb=false, b[maxkoja];
  
  for (s=0; s<maxkoja; s++) {
    dif[s] = dKoja[p][s] - oldKOJA[s];
    absdif[s]=abs(dif[s]);
    sgn[s] = sign(dif[s]);
    b[s]=false; if (absdif[s] > 0) {b[s]=true;}   //ar reikia koja judinti
    bb=bb or b[s];
  }
  while (bb) {
    bb=false;
    for (s=0; s<maxkoja; s++) {
      if (b[s]) {
        KOJA[s]=KOJA[s] + sgn[s];
        updateOne(s,globalPauze);
        absdif[s]--;
        if (absdif[s]<=0) {b[s]=false;} else {b[s]=true;} 
      } 
      bb=bb or b[s];
    }
  } 
} // end  move_to_patternca
/*******************************************/
void kom(int k) {
  Serial.print("Koja: "); Serial.print(k); 
  int laikas=1;  String rr="";  bool jau=false;
  while (!jau) {
    while (Serial.available()) {
      char cc = Serial.read(); rr += cc; delay(2);  
    }
    if (rr.length() >0) {
      Serial.println(rr);  
      int n = rr.toInt();    KOJA[k]=n;  updateOne(k,globalPauze); jau=true; break;
    }
    delay(1000); Serial.print(".");  laikas+=1;   if (laikas>20) {Serial.println("");}
  }
} /// end kom()
/*****************************************************/

void komanda(String st) {
  String eile[10];
  char tipas=char(st[0]);
  int kj;
  
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

  if (tipas=='d') {
      globalPauze = eile[1].toInt();
      Serial.print("globali pauze = "); Serial.println(globalPauze);
  } //d

  if (tipas=='p') {
      kj=eile[1].toInt();
      Serial.print("Pattern "); Serial.println(kj); 
      if (kj<maxpattern) { 
        move_to_pattern(kj); 
      }
  } //p

  if (tipas=='m') {
    kj=eile[1].toInt();  //kiek kartu sukti cikla
    for (int x=0; x<kj; x++) {
      for (int j=2; j<=i; j++) {
        int kmp = eile[j].toInt();
        move_to_pattern( kmp );
      }
      
    }
  }

  if (tipas=='h') {
      bool known=false;
      if (eile[1] == "pos" and not known) { known=true;
            Serial.print(String(KOJA[0]) + " / " + String(KOJA[1]) + " / ");
            Serial.print(String(KOJA[2]) + " / " + String(KOJA[3]) ); Serial.println();
      }
      if (not known) { Serial.println("don't know"); }
  } //h

  
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
