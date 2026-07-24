import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'

with serial.Serial('COM3', 9600, timeout=5) as ser:
    line = ser.readline()

ser.close()