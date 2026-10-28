# een list met de naam fruit met 5 verschilende soorten fruit
fruit = ["apple", "banaan", "kers", "mandarijn", "druif"]
#voegd fruit toe
fruit.append("aardbij")
# verwijderd aple
fruit.remove("apple")
# print de len van fruit
print(len(fruit))
# een variable om te controleren of banaan al geweest is
check = 0
# een loop door de list fruit
for i in fruit:
    # print het fruit
    print(i)
    # controlleerd of banaan in de list zit
    if i == "banaan":
        print("banaan zit in het boodschapen lijstje")
        check = 1
    # controlleerd of banaan nog niet geweest is
    elif check == 0 and i == fruit[len(fruit) -1]:
        print("banaan zit niet in het boodschapen lijstje")