# PART 1
def greet_user(name):
    print(f"Hello, {name}! welcome! ")

# greet_user("Toyin")

# PART 2
def calculate_area(length, width):
    return length * width

# area = calculate_area(6,7)
# print(f"The are of the rectangle is:{area}")




# PART 3
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(10))
# print(is_even(11))

# PART 4
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in celsius: "))
print(f"{celsius}°C is
{celsius_to_fahrenheit(celsius)}°F")



# PART 5
# def find_largest(numbers):
#     return max(numbers)
# numbers = [12, 45, 7, 23]
# print("Largest number:", find_largest(numbers))


# PART 6
# def print_table(number):
#     if not isinstance(number, int):
#         print("inpute must be an integer.")
#         return
#     print(f"Multiplication table for {number}: ")
#     for i in range(1, 11):
#         product = number * i
#         print(f"{number} x {i} = {product}")
# number = int(input("Enter a number: "))
# print_table(number)



# PART 7
# def add(a,b):
#     return a + b
# print(add(30,6))

# def subtract(a, b):
#     return a - b
# print(subtract(20 - 6))

# def division(a, b):
#     return a // b
# print(division(4, 2))



# def compare(x, y):
#     if x > y :
#         return "x is greater than y"
#     elif x < y:
#         return "x is less than y"
#     return "x is equal to y"

# # print(compare(8, 7))

# compare_lamda = lambda x, y: "x is greater than y" if x > y else "x is less than y" if x < y else "x is lequal to than y"
# # print(compare_lamda(8, 8))

# def operation(x, y):
#     if x % 2 == 0:
#         return x * y
#     return x + y

# print(operation_lamda)

# operation_lamda = lambda x, y: x * y if x % 2 == 0 