#define TRIG_PIN 6
#define ECHO_PIN 7

void setup() {
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    Serial.begin(9600);
}

void loop() {
    long distance = getDistance();

    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");

    delay(500); // Delay for readability
}

long getDistance() {
    // Trigger the sensor
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    // Read echo duration
    long duration = pulseIn(ECHO_PIN, HIGH);

    // Calculate distance in cm
    long distance = duration * 0.034 / 2;

    return distance;
}
