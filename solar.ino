const int analogPin = 34; // ADC1_CH6
float voltage = 0.0;

void setup() {
  Serial.begin(115200);
  delay(1000); // Allow time for serial monitor to open
}

void loop() {
  int analogValue = analogRead(analogPin);

  // Convert analog value (0-4095) to voltage (0-3.3V)
  voltage = (analogValue / 4095.0) * 3.3;

  Serial.print("Voltage: ");
  Serial.print(voltage);
  Serial.println(" V");

  delay(1000);
}
