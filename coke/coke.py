i = 0
money_inserted = 0

while i < 50:
    coin = int(input("Insert Coin: "))
    if(coin == 30):
        print("Amount due: 50")
        i = 0
        money_inserted = 0
    else:
        money_inserted += coin
        i = money_inserted
        if (i>=50):
            break
        else:
            print("Amount Due: ", 50-i)

change_owed = money_inserted - 50
print("Change_owed: " + str(change_owed))

