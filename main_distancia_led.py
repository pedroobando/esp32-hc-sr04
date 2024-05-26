from machine import time_pulse_us, Pin, SoftI2C, sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time
# import datetime 

# Parametros del LCD 16x2
I2C_ADDR = 0X27
TOTAL_ROWS = 2
TOTAL_COLS = 16

SCL_GPIO_22 = Pin(22)
SDA_GPIO_21 = Pin(21)
FREQ = 10000

# Pantalla LCD Inicializa 
i2c = SoftI2C(scl=SCL_GPIO_22, sda=SDA_GPIO_21, freq=FREQ)
lcd = I2cLcd(i2c, I2C_ADDR, TOTAL_ROWS, TOTAL_COLS)
# lcd.backlight_off()
lcd.backlight_on()
lcd.clear()
# lcd.move_to(0, 1)
# lcd.putstr("ESP32 y LCD")

# lcd.putstr("Romana: ")

# Manejador de la distancia
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

# Inicialización del sensor
sensor = HCSR04(TRIG_GPIO5_PIN, ECHO_GPIO18_PIN)

lcd.putstr("Distancia")
while True:
    try:
        distance = sensor.distance_cm()
        print("Distancia: {:.2f} cm".format(distance))
        lcd.move_to(1, 1)
        lcd.putstr(str("{:.2f} cm   ".format(distance)))
    except OSError as e:
        print("Error al medir la distancia:", e)
    time.sleep(1)
