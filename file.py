# FILES

# Open a file for reading 
file = open("soft.py", "r")

# Reading from a file
# print(file.read()) # Read the antire file
# print(filr.read(10)) # Read the first 10 charcters
# print(file.readline()) # Read the first line
# print(file.readline()) # Read the second line
# prin dt(file.readline()) # Read all the line and return a list

# Run a loop to read the lines
# for f in file:
    # print(f, end='')
    # pass

#  WITH
# Open and automatically close the file when done

# with open("filenewfile.txt", 'w') as file:
#     file.write("Hello world\n")
#     file.write("Welcome to programing with\n")
#     file.write("Happy coding 😊🚀\n")




# ASSIGNMENT
# PART 1
# def write_to_file(strings):
#     with open("output.txt", "w") as file:
#         for string in strings:
#             file.write(string + 
# "\n")

# write_to_file(["Hello", "This is a test", "Python is fun!"])

    


# PART 2
# def read_from_file():
    # with open("output.txt", "r") as file:
        # for line in file:
        #     print(line.strip())

# read_from_file()

# PART 3
# def count_words_in_file():
#     with open("text.txt", "r") as file:
#         content = file.read()
#         words = content.split()
#         return len(words)
    
# word_count = count_words_in_file()
# print(word_count)


# PART 4
# def copy_file():
#     with open("text.txt", "r") as source_file:
#         content = source_file.read()
#     with open("copy.txt", "w") as destination_file:
#         destination_file.write(content)

# copy_file()

# PART 5
def append_to_file(text):
    with open("output.txt", "a") as file:
        file.write(text + "\n")  

append_to_file("I like apple.")