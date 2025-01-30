print("Tervetuloa laskimeen!")
print("Valitse toiminto:")
print("1. Yhteenlasku")
print("2. Vähennyslasku")
print("3. Kertolasku")
print("4. Jakolasku")

valinta = input("Valitse toiminto (1/2/3/4):")

luku1 = int(input("Syötä ensimmäinen luku: "))
luku2 = int(input("Syötä toinen luku: "))

if valinta == "1":
    tulos = luku1 + luku2
    print(f"Tulos: {tulos}")
elif valinta == "2":
    tulos = luku1 - luku2
    print(f"Tulos: {tulos}")
elif valinta == "3":
    tulos = luku1 * luku2
    print(f"Tulos: {tulos}")
elif valinta == "4":
    if luku2 !=0:
        tulos = luku1 / luku2
        print(f"Tulos: {tulos}")
    else:
        print("Virhe! Et voi jakaa nollalla.")
else:
    print("Virheellinen valinta.")