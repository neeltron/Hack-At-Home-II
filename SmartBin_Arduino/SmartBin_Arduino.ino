#include <Servo.h>

int servoPin1 = 3;
int servoPin2 = 4;
int sFactor1 = 0;
int sFactor2 = 90;
String transmitVar = "0";
Servo Servo1;
Servo Servo2;

void setup() {
  Serial.begin(9600);
  Servo1.attach(servoPin1);
  Servo2.attach(servoPin2);
}
void loop() {
  if (Serial.available() > 0) {
    Serial.println("S Avl.");
    transmitVar = Serial.readString();
    Serial.println(transmitVar);
    if (transmitVar.indexOf('0') > -1) {
      sFactor1 = 0;
      sFactor2 = 90;
    }
    else if (transmitVar.indexOf('1') > -1) {
      sFactor1 = 0;
      sFactor2 = 0;
    }
    else if (transmitVar.indexOf('2') > -1) {
      sFactor1 = 90;
      sFactor2 = 90;
    }
    Servo1.write(sFactor1);
    Servo2.write(sFactor2);
    Serial.println(sFactor1);
    Serial.println(sFactor2);
  }
}
