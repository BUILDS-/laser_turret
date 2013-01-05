// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.

#include <math.h>
#include <Servo.h> 
#include <avr/interrupt.h>


Servo panServo;  // create servo object to control a servo
Servo tiltServo;

// a maximum of eight servo objects can be created 

int pos = 0;    // variable to store the servo position 

void setup() 
{ 
  noInterrupts();
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  Serial.begin(9600);
//  Serial.println("Hello Computer");
  Serial.read();
//  TCNT0 = 0;
//  TCCR0A = (1 << WGM01);
//  TCCR0B = (1 << CS01)|(1 << CS00);
//  OCR0A = 0x22;
//
//  TIMSK0 = (1<<OCIE0A);
  
  interrupts();
  panServo.attach(9);  // attaches the servo on pin 9 to the servo object 
  tiltServo.attach(10);
//  delay(500);
} 

//ISR(TIMER0_COMPA_vect) {
//  digitalWrite(13, HIGH);
//}

void loop() 
{
  static int p = 0;
  static int t = 0;
  static int i = 0;
  static char inBuf[256];
  static char angle[10];
  static int buf_i = 0;
  int ang_i = 0;
  if (Serial.available() > 0) {
    inBuf[buf_i] = Serial.read();
    
    switch (inBuf[buf_i]) {
      case '\n':
        for (int buf_loc = 0; buf_loc < buf_i; buf_loc++) {
          switch (inBuf[buf_loc]) {
            case 'a':
              p++;
              break;
            case 'd':
              p--;
              break;
            case 'w':
              t--;
              break;
            case 's':
              t++;
              break;
            case 'c':
              t = 0; p = 0; break;
            case 'p':
              for (ang_i = 0; ang_i < buf_i; ang_i++) {
                if ((inBuf[buf_loc+1+ang_i] == '-') && (ang_i == 0)) {
                  angle[ang_i] = inBuf[buf_loc+1+ang_i];
                } else if ((inBuf[buf_loc+ang_i+1] >='0') && (inBuf[buf_loc+ang_i+1] <='9')) {
                  angle[ang_i] = inBuf[buf_loc+1+ang_i];
                } else {
                  angle[ang_i] = '\0';
                  break;
                }
              }
              buf_loc = buf_loc+ang_i;
              p = atoi(angle);
              break;
            case 't':
              for (ang_i = 0; ang_i < buf_i; ang_i++) {
                if ((inBuf[buf_loc+1+ang_i] == '-') && (ang_i == 0)) {
                  angle[ang_i] = inBuf[buf_loc+1+ang_i];
                } else if ((inBuf[buf_loc+ang_i+1] >='0') && (inBuf[buf_loc+ang_i+1] <='9')) {
                  angle[ang_i] = inBuf[buf_loc+1+ang_i];
                } else {
                  break;
                }
              }
              buf_loc = buf_loc+ang_i+1;
              t = atoi(angle);
              break;
          }
        }
        buf_i = 0;
        break; 
      default:
        buf_i++;
        break;
    }
      // say what you got:
//    if (incomingByte == 'a') {
//      p += 1;
//    } else if (incomingByte == 'd') {
//      p -= 1;
//    } else if (incomingByte == 'w') {
//      t--;
//    } else if (incomingByte == 's') {
//      t++;
//    } else if (incomingByte == 'c') {
//      t = 0;
//      p = 0;
 //   }
    
    
  }
//  p = 10*sin(2*M_PI*i/40);
//  t = 10*(2*M_PI*i/20);
  panServo.write(90+p);
  tiltServo.write(90+t);
//  delay(10);
//  i = (i++) % 200;
} 

