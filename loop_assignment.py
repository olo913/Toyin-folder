# Task 1: Print the Elements of a List
# For Loop:
# Write a program that iterates over a list of numbers and prints each number.
# While Loop:
# Write the same program using a `while` loop instead of a `for` loop.
# CODE
items = (10, 25, 36, 47, 50, 66, 74, 89)
# for i in items:
    # print(i)
    # ...

# while loop
i = 0
while i < 6:
    # print(items[i])
    i += 1

# Task 2: Reverse a String
# For Loop:
# Write a program that takes a string as input and prints
# the string in reverse order using a `for` loop.
# While Loop:
# Write the same program using a `while` loop.
# CODE
input_str = input("Enter a string: ")
# print("Reversed String: ")
# for i in range(len(input_str) -1, -1, -1):
#     print(input_str[i], end="")

# FOR WHILE LOOP
i = len(input_str) -1
while i >= 0:
    print(input_str[i], end="")
    i -= 1



# Task 3: FizzBuzz
# For Loop:
# Write a program that prints numbers from 1 to 50.
# For multiples of 3, print "Fizz" instead of
# the number, and for multiples of 5, print "Buzz."
# For numbers that are multiples of both
# 3 and 5, print "FizzBuzz."
# While Loop:
# Write the same program using a `while` loop.
# CODE
# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# WHILE LOOP
# i = 1
# while i <= 50:
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Buzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#     i += 1

