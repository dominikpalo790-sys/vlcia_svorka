while True:
    print("Viliam Pavlov")
    print("pre MENU menu stalcte 1")
    if input() == "1":
        print ("---- MENU ---")
        print ("pre vypisani mena 10x stalcte 1")
        if input() == "1":
            for i in range(10):
                print("Viliam Pavlov")
        else:
            print("toto nie je 1")
    else:
        print("toto nie je 1")
    break