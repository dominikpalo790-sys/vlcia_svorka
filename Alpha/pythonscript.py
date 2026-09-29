print("Dominik Paľo")

while True:
    print("\n1 - Vypíše moje meno 10-krát")
    print("2 - Vypne program")

    volba = input("Vyber možnosť: ")

    if volba == "1":
        for i in range(10):
            print("Dominik Paľo")
    elif volba == "2":
        print("Program sa vypína...")
        break
    else:
        print("Neplatná možnosť, skús znova.")