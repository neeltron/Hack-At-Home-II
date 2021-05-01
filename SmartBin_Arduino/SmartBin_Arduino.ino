#include <Servo.h>
int servoPin1 = 3;
int servoPin2 = 4;
Servo Servo1;
Servo Servo2;
void setup() {
  Servo1.attach(servoPin1);
  Servo2.attach(servoPin2);
}

void loop() {
  Servo1.write(90);
  Servo2.write(90);
  delay(1000);
  Servo1.write(0);
  Servo2.write(0);
  delay(1000);
}
