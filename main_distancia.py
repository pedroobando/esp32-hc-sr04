from machine import Pin, time_pulse_us
import time

class HCSR04:
    def __init__(self, trig_pin, echo_pin):
        self.trig = Pin(trig_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        self.trig.off()

    def distance_cm(self):
        # Enviar un pulso de 10us para iniciar la medición
        self.trig.off()
        time.sleep_us(2)
        self.trig.on()
        time.sleep_us(10)
        self.trig.off()
        
        # Medir el tiempo del pulso de respuesta del ECHO
        duration = time_pulse_us(self.echo, 1, 1000000)  # Espera hasta 1 segundo para un pulso de alta (1)

        # Calcular la distancia en cm (velocidad del sonido = 34300 cm/s)
        distance = (duration / 2) / 29.1
        return distance

# Pines de HC-SR04 a ESP32
TRIG_GPIO5_PIN = 5
ECHO_GPIO18_PIN = 18


# VCC   =>  5V
# Trig  =>  GPIO5 
# Echo  =>  GPIO18
# GND   =>  GND



# Inicialización del sensor
sensor = HCSR04(TRIG_GPIO5_PIN, ECHO_GPIO18_PIN)

while True:
    try:
        distance = sensor.distance_cm()
        print("Distancia: {:.2f} cm".format(distance))
    except OSError as e:
        print("Error al medir la distancia:", e)
    time.sleep(1)
