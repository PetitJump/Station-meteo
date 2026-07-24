#include <BH1750.h>
#include <Wire.h>
#include <Adafruit_BMP280.h>
#include <LedControl.h>

BH1750 lightMeter;
Adafruit_BMP280 bmp;
#define DIN_PIN 11
#define CS_PIN  10
#define CLK_PIN 13

LedControl lc = LedControl(DIN_PIN, CLK_PIN, CS_PIN, 1);

const byte digitFont[10][5] = {
  {0x3E, 0x51, 0x49, 0x45, 0x3E}, // 0
  {0x00, 0x42, 0x7F, 0x40, 0x00}, // 1
  {0x42, 0x61, 0x51, 0x49, 0x46}, // 2
  {0x21, 0x41, 0x45, 0x4B, 0x31}, // 3
  {0x18, 0x14, 0x12, 0x7F, 0x10}, // 4
  {0x27, 0x45, 0x45, 0x45, 0x39}, // 5
  {0x3C, 0x4A, 0x49, 0x49, 0x30}, // 6
  {0x01, 0x71, 0x09, 0x05, 0x03}, // 7
  {0x36, 0x49, 0x49, 0x49, 0x36}, // 8
  {0x06, 0x49, 0x49, 0x29, 0x1E}  // 9
};

void setup() {
  Serial.begin(9600); // Le nombre de 'baud' pour décrypter le 'Serial Monitor'
  Wire.begin(); // Initialise la communication I2C
  lightMeter.begin(); // On démarre le capteur de lumière
  bmp.begin(0x76); // On démarre le capteur BMP280
  pinMode(7, OUTPUT); // Pour la lampe / LED
  pinMode(9, OUTPUT);
  pinMode(4, OUTPUT); // Pour le buzzer
  lc.shutdown(0, false);
  lc.setIntensity(0, 8);
  lc.clearDisplay(0);
}

void afficherDizaine(float valeur) {
  int entier = (int)valeur;        // 33.7 -> 33, 25.9 -> 25
  entier = abs(entier);            // au cas où valeur négative
  int dizaine = (entier / 10) % 10; // 33 -> 3, 25 -> 2, 8 -> 0

  lc.clearDisplay(0);
  for (int col = 0; col < 5; col++) {
    lc.setColumn(0, col + 1, digitFont[dizaine][col]); // +1 pour centrer sur les 8 colonnes
  }
}

void loop() {
  float lux = lightMeter.readLightLevel(); // Prendre la valeur du capteur de lumière
  uint32_t pressure = bmp.readPressure() / 100; // Convertit la pression (Pa -> hPa)
  float temperature = bmp.readTemperature(); // Température en °C
  float altitude = bmp.readAltitude(); // Altitude à partir du niveau de la mer

  // --- Gestion de la température ---
  if (temperature >= 30) {
    digitalWrite(7, HIGH);
    delay(100); 
    digitalWrite(7, LOW);
    delay(100);
    digitalWrite(7, HIGH);
    delay(100);
    digitalWrite(7, HIGH);
    delay(100); 
    digitalWrite(7, LOW);
    delay(100);
    tone(4, 1000);
    delay(200);
    tone(4, 1200);
    delay(200);
    noTone(4);
  } else {
    digitalWrite(7, LOW);
  }

  // --- Gestion de la lumière ---
  if (lux >= 300) {
    digitalWrite(9, HIGH);
  } else {
    digitalWrite(9, LOW);
  }

  // --- Affichage Moniteur Série ---
  afficherDizaine(temperature);
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(pressure);
  Serial.print(",");
  Serial.print(lux);
  Serial.print(",");
  Serial.println(altitude);
  
  delay(500); // Attendre 0,5s
}
