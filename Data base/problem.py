# user_input = input("Enter data (comma separated): ")
# strings = user_input.split(',')
# file = open("user_data.txt", "w")
# for string in strings:
#     file.write(string.strip() + "\n")
# file.close()




# TASK 2
def login(username, password):
    correct_username = username
    correct_password = password
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login succsessful")
    else:
        print("invalide credentials")


login("Shalom", "54321")



# TASK 3
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# temp_celsius = float(input("Enter temperature in Celsius: "))
# temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
# print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")



# TASK 4
# sentence = input("Enter sentence: ")
# words = sentence.split()
# for word in words:
#     word_length = len(word)
#     print("word:", word, "=lenth:", word_length)



# TASK 5
# print("Enter the first listof numbers(seperated by spacees): ")
# list1 = [int(num) for num in input().split()]
# print("Enter the second list of numbers(seperated by spaces): ")
# list2 = [int(num) for num in input().split()]
# merged_list = sorted(list1 + list2)
# print("Sorted merged list: ")
# print(merged_list)


# PART 6
# def calculate_simple_interest(principal, rate, time):
#     simple_interst = (principal * rate * time) / 100
#     return simple_interst
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the Rate of interest: "))
# time = float(input("Enter the Time time in years: "))
# interest = calculate_simple_interest(principal, rate, time)
# print("The simple interest is:", interest)


# PATR 7
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# word_frequency = {}

# for word in words:
#     word = word.lower()
#     if word in word_frequency:
#         word_frequency[word] += 1
#     else:
#         word_frequency[word] = 1


# print("Word frequencies:")
# for word, frequency in word_frequency.items():
#     print(f"{word}: {frequency}")


# PART 8
# import random

# number_to_guess = random.randint(1, 50)

# while True:
#     guess = int(input("Enter your guess: "))

#     if guess > number_to_guess:
#         print("Too high.")
#     elif guess < number_to_guess:
#         print("Too low.")
#     else:
#         print(f"Correct! The number was {number_to_guess}.")
        # break




# PART 9

