#include <Servo.h>

const int extraPin = 7;

Servo PowerServo;
void setup() {
  // put your setup code here, to run once:


  PowerServo.attach(9);
  delay(1000);
  PowerServo.write(60);
  delay(1000);
  PowerServo.write(90);
  delay(1000);
  pinMode(extraPin, OUTPUT);
  digitalWrite(extraPin, LOW);
  while (1);
}
