import serial
import csv

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'

with serial.Serial('COM3', 9600, timeout=5) as ser: # Boucle pour récuperer les infos
    while True:
        data: bytes = ser.readline() # On récupere la ligne
        ligne: str = data.decode('utf-8').strip() # On la décode en utf-8 pour ne pas l'avoir en binaire
        valeurs: list = ligne.split(',') # On split 'data' pour crée une liste avec que les données (sans les ',')
        with open('data.csv', 'a', newline='') as f:
            if ligne: # Vérifie que 'ligne' n'est pas vide
                writer = csv.writer(f)
                writer.writerow(valeurs)
                print("Fait")

ser.close()