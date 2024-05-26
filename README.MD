# ESP32 Interface sensor HC-SR04

Conexion del sensor ultrasonico HC-SR04 al esp32, con el objetivo de leer la distancia entre un punto y otro

Microcontrolador: _ESP32 DevkitC_v4_

Programa escrito en micropython, con ayuda de chatGPT

## Conexion Pines HC-SR04 a ESP32

```
  VCC   =>  5V
  Trig  =>  GPIO5
  Echo  =>  GPIO18
  GND   =>  GND
```

## main_distancia.py

Muestra la distancia aproximada que existe entre un punto y otro, (existe un peque~no margen de error)

## main_distancia_lcd.py

La misma aplicacion que la anterior, solamente que ahora la muestra por una pantalla LCD la distancia.

## NOTA;

En Youtube se consigue mucha informacion, colocar esto:

```
  HC-SR04 esp32
```
