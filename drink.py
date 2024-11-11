x = 5
y = 10

# Condition
# if x < y:
#     # Statement
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")

# if x != y:
#     print("x is not equal to y")
# elif x == y:
#     print("x is equal to y")

# Assignment
# If invalid drink? Continue asking what they want
# then in the fifth time, ask if they want to continue
# If 'yes' keep asking. If 'no' stop the program
import sys
coke = 450
fanta = 400

print("We have\n1. Coke\n2. Fanta\n")
count = 0
drink = input("What do you want? ")
if drink == "coke" or drink == "1":
    qty = int(input("How many are you buying? "))
    print("We have\n1. Vanilla\n2. Diet")
    option = input("Enter your choice: ")
    balance = coke * qty
    if option == "vanilla":
        print("Take your vanilla coke")
    elif option == "diet":
        print("Take your diet coke")
    else:
        print("Take your original coke")
elif drink == "fanta" or drink == "2":
    qty = int(input("How many are you buying? "))
    print("We have\n1. Peach\n2. Grape")
    option = input("Enter your choice: ")
    flavor = ["peach", "grape"]
    if option in flavor:
        print(f"Take your {option} fanta")
    else:
        print("Take your original fanta")
else:
    print("Sorry we don't  have that")
    sys.exit()

print("\n1. cash payment\n2. Bank payment")
payment = input("Enter cash or bank")

if payment == "bank" or payment == "2":
    amount = int(input("Enter amount: "))
    if amount >= balance:
        change = amount - balance
        print(f"Your change is {change}")
    else:
        for _ in range(2):
            print("Insufficiant fund")
            amount = int(input("Enter ammount: "))
            if amount > balance:
                continue

elif payment == "bank" or payment == "2":
    print(f"We have deducted {balance} from your account")
else:
    print("Invalid payment method")


