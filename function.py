# Function definition
def greet():
    # Algorithim or Instruction to follow
    word = "Hello world"
    print(word)

    # Call the function
    # greet()

def greeting(name):
    print(f"My name is {name}")

# greeting("Toyn")

def calc(n,x,y):
    print(n + n)

# calc(10, 50, 20)

def multi(length):
    for i in range(length):
        print("##")

# multi(5)

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

# main()

def calc():
    a = 10 + 5
    b = a * 2
    c = 10 + b
    d = c - 5
    return d
    e = d / 2
    print(e)

# print(calc())

# def condition(x, y):
#     if x > y:
#         return "x is grater than y"
#     return

# def add(a, b):
    return a + b

def subtraction():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    return b

# def devide():
    





def max_number(a, b, c):
    # if a > b and a > c:
    #     return a 
    # elif b > a and b > c:
    #     return b
#     # return c
    return f"Maximum number of {a}, {b}, and {c} is {max(a, b , c)}"

def min_num(a, b, c):
    return f"Mininimun Number: {min(a, b , c)}"

def sum_num(a, b, c):
    return f"Sum: {sum([a, b, c])}"

    
print(max_number(10, 29, 30))
print(min_num(10, 29, 30))
print(sum_num(10, 29, 30))

# LAMBDA FUNCTION
# A lambda function is a small anonymous function.
# A lambda functioncan can take any number of arguments, but can only have one exprssion.
# Syntax: lambda arguments : expression
# Use lambda function when an anonymous function is required for a short period
# Example
x = lambda a, b : (a + 10) * b
# print(x(5, 4))

def myfunc(n):
    return lambda a : a 










# GLOBAL VARIABLE
# A variable declered outside a finction is a global variable


    



