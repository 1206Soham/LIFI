#define LED_PIN 5  // GPIO 5 is the built-in LED on many ESP32 boards

void setup() {
  Serial.begin(9600);     
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();

    if (command == '1') {
      digitalWrite(LED_PIN, HIGH);  // Turn ON LED
    } else if (command == '0') {
      digitalWrite(LED_PIN, LOW);   // Turn OFF LED
    }
  }
}
