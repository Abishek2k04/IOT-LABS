#define MOTOR_IN1 8
#define MOTOR_IN2 9

void setup() {
    pinMode(MOTOR_IN1, OUTPUT);
    pinMode(MOTOR_IN2, OUTPUT);
}

void loop() {
    // Rotate Right (Forward)
    digitalWrite(MOTOR_IN1, HIGH);
    digitalWrite(MOTOR_IN2, LOW);
    delay(3000); // rotate for 3 seconds

    // Stop
    digitalWrite(MOTOR_IN1, LOW);
    digitalWrite(MOTOR_IN2, LOW);
    delay(1000); // pause 1 second

    // Rotate Left (Reverse)
    digitalWrite(MOTOR_IN1, LOW);
    digitalWrite(MOTOR_IN2, HIGH);
    delay(3000); // rotate for 3 seconds

    // Stop
    digitalWrite(MOTOR_IN1, LOW);
    digitalWrite(MOTOR_IN2, LOW);
    delay(1000); // pause 1 second
}
