print("Lemonade Tycoon v0.1")
totalLemons = 0
ice = 0
sugar = 0
totalDays = 0



def stock():
    global lemonPurchase
    stockMenu = True
    while stockMenu:
        print("1. Buy Lemons")
        print("2. Buy Ice")
        print("3. Buy Sugar")
        print("4. Check Stock")
        print("5. GO back")
        stockMenu = input("What to do?")
        if stockMenu == "1":
            lemonPurchase = int(input("How Many Lemons DO you want?"))
            totalLemons = + lemonPurchase
        elif stockMenu == "4":
            print("Lemons: {}".format(totalLemons))
            print("Ice: {}".format(ice))
            print("Sugar: {}".format(sugar))
        elif stockMenu == "5":
            stockMenu = False


ans = True
while ans:
    print ("Day {}".format(totalDays))
    print("Choices")
    print("1. Next Day")
    print("2. Buy Stock")

    ans = input("What to do?")
    if ans == "1":
        totalDays += 1
    elif ans == "2":
        stock()





