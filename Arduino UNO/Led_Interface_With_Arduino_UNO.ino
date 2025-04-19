#define LED_1 3
#define LED_2 5
#define LED_3 7

void setup() {
  pinMode(LED_1, OUTPUT);
  pinMode(LED_2, OUTPUT);
  pinMode(LED_3, OUTPUT);

  digitalWrite(LED_1, LOW);
  digitalWrite(LED_2, LOW);
  digitalWrite(LED_3, LOW);
  delay(1000);
}

void loop() {
  unsigned long startTime = millis();

  while (millis() - startTime < 10000) { 
    //Step 1: Turn LED_1 on and LED_3 off
    digitalWrite(LED_1, HIGH);
    digitalWrite(LED_3, LOW);
    delay(100); 

    // Step 2: Turn LED_3 on and LED_2 off
    digitalWrite(LED_3, HIGH);
    digitalWrite(LED_2, LOW);
    delay(100); 

    // Step 3: Turn LED_2 on and LED_1 off
    digitalWrite(LED_2, HIGH);
    digitalWrite(LED_1, LOW);
    delay(100); 
  }

  // After 10 seconds, turn off all LEDs
  digitalWrite(LED_1, LOW);
  digitalWrite(LED_2, LOW);
  digitalWrite(LED_3, LOW);

  while (true) {
    // Stay here forever (loop stops running)
  }
}
