int rpin = 19;
int gpin = 20;
int bpin = 21;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Native USB only
  }
  Serial.print("RGB LED");
  delay(1);
  pinMode(rpin, OUTPUT);
  pinMode(gpin, OUTPUT);
  pinMode(bpin, OUTPUT);
  
}

void loop() {

  RGB_color(255,0,0);
  delay(1000);
  RGB_color(0,255,0);
  delay(1000);
  RGB_color(0,0,255);
  delay(1000);

  
 
  for (int r=50; r<=250; r=r+50) {
    for (int g=50; g <=250; g=g+50) {
      for (int b=50; b<=250; b=b+50) {
        RGB_color(r,g,b);
        delay (500);
      }
    }
  }
}

void RGB_color(int rl, int gl, int bl) {
  analogWrite(rpin, rl);
  analogWrite(gpin, gl);
  analogWrite(bpin, bl);
}
