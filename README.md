# Station-meteo

## Fonctionalité :
- Lecture de température, luminosité, altitude, pression
- Led rouge qui clignote lorsque la température dépasse 30°C
- Led bleu qui s'active lorsque la luminosité dépasse 300 lux
- Panneau led 8x8 qui montre la dizaine de la température (Exemple : 24C° = 2)

## Capteurs :
- BH1750 (Luminosité en lux)
- BMP 280 (Pression, température, altitude)

## Ressources utiliser :
- Pour la bibliothèque serial : [Docs](https://pyserial.readthedocs.io/en/latest/shortintro.html)
- Lire / ecrire csv : [Docs](https://docs.python.org/fr/3/library/csv.html)
- Gestion du temps : [Docs](https://docs.python.org/fr/3/library/time.html)
- Panneau led : [Docs](https://passionelectronique.fr/matrice-led-max7219-arduino/)