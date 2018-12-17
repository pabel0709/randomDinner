import random

for i in range(0,100000000000000):
    print("wpisz 1 aby wylosować zupe")
    print("wpisz 2 aby wylosować dodatek ")
    print("wpisz 3 aby wylosować surówke")
    print("wpisz 4 aby wylosować obiad na 7 dni")
    wybor=input("wpisz 5 aby wylosować jeden obiad: ")

    if wybor=="1":
        indexZup = 0
        zupy = ["pomidorowa", "rosół", "barszcz", "ogórkowa", "cebulowa"]
        indexZup = (random.randint(0, len(zupy) - 1))
        print(zupy[indexZup])

    if wybor=="2":
        indexdod = 0
        dodatki = ["ziemniaki", "ryż", "kasza"]
        indexdod = (random.randint(0, len(dodatki) - 1))
        print(dodatki[indexdod])



    if wybor=="3":
        surówki = 0
        surówki = ["marchewka", "buraczki", "kapusta"]
        indexsur = (random.randint(0, len(surówki) - 1))
        print(surówki[indexsur])

    if wybor=="4":
        for dni in range(1,8):
            print("dzien {}".format(dni))
            indexZup = 0
            zupy = ["pomidorowa", "rosół", "barszcz", "ogórkowa", "cebulowa"]
            indexZup = (random.randint(0, len(zupy) - 1))
            print(zupy[indexZup])
            indexdod = 0
            dodatki = ["ziemniaki", "ryż", "kasza"]
            indexdod = (random.randint(0, len(dodatki) - 1))
            print(dodatki[indexdod])
            surówki = 0
            surówki = ["marchewka", "buraczki", "kapusta"]
            indexsur = (random.randint(0, len(surówki) - 1))
            print(surówki[indexsur])

















    if wybor == "5":
        indexZup = 0
        zupy = ["pomidorowa", "rosół", "barszcz", "ogórkowa", "cebulowa"]
        indexZup = (random.randint(0, len(zupy) - 1))
        print(zupy[indexZup])
        indexdod = 0
        dodatki = ["ziemniaki", "ryż", "kasza"]
        indexdod = (random.randint(0, len(dodatki) - 1))
        print(dodatki[indexdod])
        surówki = 0
        surówki = ["marchewka", "buraczki", "kapusta"]
        indexsur = (random.randint(0, len(surówki) - 1))
        print(surówki[indexsur])




















