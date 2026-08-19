def coke_machine():
    amount_due = 50
    print("Amount Due:", amount_due)
    while amount_due > 0:
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            amount_due -= coin
            print("Amount Due:", amount_due)
        else:
            print("Amount Due:", amount_due)
    print("Change owed:", abs(amount_due))
        
    



def main():
    coke_machine()

main()