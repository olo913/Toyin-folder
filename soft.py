import sys

print("What are you buying from us today")
print("We have\n1. Coke #450\n2. Fanta #400\n3. Sprite #350\n4. Pesi #300\n")

coke = 450
fanta = 400
sprite = 350
pepsi = 300

drink = input("Drink: ").lower()
if drink == "Coke" or drink == "1":
    quantity = int(input("How many do you want? "))
    flavor =["zero", "orange", "diet"]
    print(flavor)
    option = input("Enter your flavor: ").lower()
    if option in flavor:
        print(f"Here is your {option} coke")
    else:
        print("Here is your original coke")
    balance = coke * quantity
    print(f"Your balance is {balance}")
elif drink == "fanta" or drink == "2":
    quantity = int(input("How many do you want? "))
    flavor = ["lemon", "berry", "peach"]
    print(flavor)
    option = input("Enter your flavor: ").lower()
    if option in flavor:
        print(f"Here is your {option} fanta")
    else:
        print("Here is your original fanta")
    balance = coke * quantity
    print(f"Your balance is {balance}")
elif drink == "fanta" or drink == "3":
    quantity = int(input("How many do you want? "))
    flavor = ["cherry", "grape", "tropical"]
    print(flavor)
    option = input("Enter your flavor: ").lower()
    if option in flavor:
        print(f"Here is your {option} sprite")
    else:
        print("Here is your original sprite")
    balance = coke * quantity
    print(f"Your balance is {balance}")
elif drink == "pepsi" or drink == "4":
    quantity = int(input("How many do you want? "))
    flavor = ["lime", "mango", "diet"]
    print(flavor)
    option = input("Enter your flavor: ").lower()
    if option in flavor:
        print(f"Here is your {option} pepsi")
    else:
        print("Here is your original pepsi")
    balance = pepsi * quantity
    print(f"Your balance is {balance}")
else:
    print("Invalid request")
    sys.exit()


print("\nPayment type\n1. Cash Payment\2. Bank Payment")
Payment = input("Payment: \n\"cash\" or \"bank\"? ")
if Payment == "cash" or Payment == "1":
    pay = int(input("How much are you paying? "))
    if  pay < balance:
        print("your money is lower than balance")
    else:
        change = pay - balance
        print(f"your change is {change}")
elif Payment == "bank" or Payment == "2":
    print(f"We have deducted {balance} from your account")
else:
    print("invalid payment")









