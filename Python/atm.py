withdraw=float(input("Enter the amount of cash to be withdrwan\n"))
inital=float(input("Enter the account balance\n"))
if withdraw > inital:
    print("Pehli Fursat Me Nikal")
else:
    if (withdraw%5)==0:
        total = withdraw-0.50
        print("Successful Transaction")
        print(total)
    else:
        print("Incorrect withdrawl amount")
        print(inital)