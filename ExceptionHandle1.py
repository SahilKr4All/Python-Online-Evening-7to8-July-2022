def atm():
    total = 10000
    pin = input("Enter your Pin:")
    if pin == "1234":
        print("LOGIN SUCCESS!")
    else:
        raise ValueError("Login Failed")

    amount = int(input("Enter Amount :"))
    if amount > total:
        raise ValueError("***sInsufficient Balance***")
    else:
        print("Amount Withdrawn Successfully")
        total = total - amount
        print(total)
        
try:
    atm()
except ValueError as msg:
    print(msg)
    atm()
