# TASK 2
# def multiply():
# num = int(input("Enter a number: "))
#     print(f"Multiplication table for {num}:\n")
#     for i in range(1, 11):
#         product = num * i
#         print(f"{num} x {i} = {product}")

# i = 0
# while i <= 10:
#     product = num * i
#     print(f"{num} x {i} = {product}")
#     i += 1


# TASK 3
import random
def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    while True:
        user_guess = input("Guess a number between 1 and 10:")
        if not user_guess.isdigit():
            print("invalid input. Pleasenter a whole number.")
            user_guess = int(user_guess)
        attempts += 1
        if user_guess == number_to_guess:
                print(f"\nCongratulation! You guessed the number in{attempts} attempts.")
                break
        elif user_guess < number_to_guess:
             print("Too  low! Try again.")
        else:
             print("Too high. Try again.")
             guess_the_number()
