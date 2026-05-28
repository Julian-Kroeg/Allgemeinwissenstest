print("Willkommen zu meinem Allgemeinwissenstest!")
print("Jede richtige Antwort wird mit einem Punkt belohnt! Jede falsche Antwort führt zum Punktabzug!")
input("Drücken Sie Enter um den Test zu beginnen")

punktzahl = 0

print("Frage 1: Welche Stadt war die Hauptstadt von Westdeutschland?")
print("1) Berlin")
print("2) Hamburg")
print("3) Bonn")

while True:
    try:
        antwort1 = int(input("Antwort: "))
        break
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein!")

if antwort1 == 3:
    print(f"Die Antwort {antwort1} ist richtig!")
    punktzahl += 1
else:
    print(f"Die Antwort {antwort1} ist leider falsch!")
    punktzahl -= 1

print("Frage 2: In welchem Zeitraum ereignete sich der erste Weltkrieg?")
print("1) 1933 bis 1945")
print("2) 1914 bis 1918")
print("3) 1945 bis 1955")

while True:
    try:
        antwort2 = int(input("Antwort: "))
        break
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein!")

if antwort2 == 2:
    print(f"Die Antwort {antwort2} ist richitg!")
    punktzahl += 1
else:
    print(f"Die Antwort {antwort2} ist leider falsch!")
    punktzahl -= 1

print("Frage 3: Welches Bundesland ist flächenmäßig das größte?")
print("1) Baden-Württemberg")
print("2) Brandenburg")
print("3) Bayern")

while True:
    try:
        antwort3 = int(input("Antwort: "))
        break
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein!")

if antwort3 == 3:
    print(f"Die Antwort {antwort3} ist richtig!")
    punktzahl += 1
else:
    print(f"Die Antwort {antwort3} ist leider falsch!")
    punktzahl -= 1

print("Frage 4: Aus wie vielen Knochen besteht ein Erwachsenenkörper?")
print("1) 306")
print("2) 250")
print("3) 206")

while True:
    try:
        antwort4 = int(input("Antwort: "))
        break
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein!")

if antwort4 == 3:
    print(f"Die Antwort {antwort4} ist richtig!")
    punktzahl += 1
else:
    print(f"Die Antwort {antwort4} ist leider falsch!")
    punktzahl -= 1

print("Frage 5: Was ist eine Primzahl?")
print("1) Eine Bruchzahl, inwelcher Nenner und Zähler identisch sind")
print("2) Eine Zahl, welche nur durch sich selbst und 1 teilbar ist")
print("3) Eine Dezimalzahl, welche unendlich viele Nachkommestellen hat")

while True:
    try:
        antwort5 = int(input("Antwort: "))
        break
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein!")

if antwort5 == 2:
    print(f"Die Antwort {antwort5} ist richtig!")
    punktzahl += 1
else:
    print(f"Die Antwort {antwort5} ist leider falsch!")
    punktzahl -= 1

input("Der Test ist beendet! Drücken Sie Enter, um das Ergebnis zu sehen")
print(f"Sie haben {punktzahl} Punkte erreicht!")
print("Teilen Sie mir doch das Ergebnis in einem Bewerbungsgespräch mit :) ")
input("Bitte drücken Sie Enter um das Programm zu beenden")