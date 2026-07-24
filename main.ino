#include <BH1750.h>
#include <Wire.h>
#include <Adafruit_BMP280.h>

BH1750 lightMeter;
Adafruit_BMP280 bmp;

void setup() {
    Serial.begin(9600);      // Le nombre de 'baud' pour décrypter le 'Serial Monitor'
    Wire.begin();            // Initialise la communication de l'I2C
    lightMeter.begin();      // On démarre le capteur de lumière
    bmp.begin(0x76);         // On démarre le capteur BMP280

    pinMode(7, OUTPUT);      // Pour la lampe
    pinMode(9, OUTPUT);
}

void loop() {
    float lux = lightMeter.readLightLevel();        // Prendre la valeur du capteur de la lumière
    uint32_t pressure = bmp.readPressure() / 100;   // Prend la valeur en Pa et la convertit en hPa
    float temperature = bmp.readTemperature();      // Prend la valeur de la température en °C
    float altitude = bmp.readAltitude();            // Prend la valeur de l'altitude (à partir du niveau de la mer)

    if (temperature >= 30) {
        digitalWrite(7, HIGH);

        tone(9, 1000);
        delay(200);

        tone(9, 800);
        delay(200);

        noTone(9);
    }
    else {
        digitalWrite(7, LOW);
    }

    Serial.print(temperature);
    Serial.print(",");

    Serial.print(pressure);
    Serial.print(",");

    Serial.print(lux);
    Serial.print(",");

    Serial.println(altitude);

    delay(5000); // Attendre 5 s
}