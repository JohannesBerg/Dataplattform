#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include "DHT.h"
#include <SoftwareSerial.h>
#include <MHZ.h>


#define DHTPIN 16
#define photoResistor 32

// pin for pwm reading
#define CO2_IN 17

// pin for uart reading
#define MH_Z19_RX 19 // D7
#define MH_Z19_TX 18 // D6

#define sensor 26

#define DHTTYPE DHT21

MHZ co2(MH_Z19_RX, MH_Z19_TX, CO2_IN, MHZ19B);

float hum = 0;
float temp = 0;

DHT dht(DHTPIN, DHTTYPE);

void co2Sensor(){
	Serial.print("\n----- Time from start: ");
	Serial.print(millis() / 1000);
	Serial.println(" s");

	int ppm_uart = co2.readCO2UART();
	Serial.print("PPMuart: ");

	if (ppm_uart > 0)
	{
		Serial.print(ppm_uart);
	}
	else
	{
		Serial.print("n/a");
	}

	int ppm_pwm = co2.readCO2PWM();
	Serial.print(", PPMpwm: ");
	Serial.print(ppm_pwm);

	int temperature = co2.getLastTemperature();
	Serial.print(", Temperature: ");

	if (temperature > 0)
	{
		Serial.println(temperature);
	}
	else
	{
		Serial.println("n/a");
	}

	Serial.println("\n------------------------------");
}

void setup() {
	Serial.begin(9600);
	pinMode(photoResistor, INPUT);
	pinMode(CO2_IN, INPUT);
	pinMode(sensor, INPUT);
	dht.begin();
	if (co2.isPreHeating())
	{
		Serial.print("Preheating");
		while (co2.isPreHeating())
		{
			Serial.print(".");
			delay(5000);
		}
		Serial.println();
	}
}

void loop() {
	Serial.println("Movement: ");
	Serial.println(digitalRead(sensor));

	Serial.println("Light: ");
	Serial.println(analogRead(photoResistor));

	hum = dht.readHumidity();
	temp = dht.readTemperature();

	Serial.print("Humidity: ");
	Serial.print(hum);
	Serial.print(" %, Temp: ");
	Serial.print(temp);
	Serial.println(" Celsius");

	co2Sensor();
	delay(1000);
}