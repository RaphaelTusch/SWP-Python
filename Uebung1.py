zahl = 7
if zahl > 5:
    print('Zahl größer 5')
elif zahl < 8:
    print('Zahl kleiner 8')
else:
    print('Zahl nicht zwischen 5 und 8')

x=0
while x < 10:
    x += 1
    if x == 3:
        pass   # 3 wird übersprungen
    if x == 5:
        break  #Schleife bei 5 abgebrochen


for i in range(1, 6):
    if i == 2:
        pass
    if i == 4:
        break


try:
    ergebnis = 10 / 0
except ZeroDivisionError:
    print("Fehler: Division durch Null!")
else:
    ("Alternativer Teil")
finally:
    print("Das wird immer ausgeführt")