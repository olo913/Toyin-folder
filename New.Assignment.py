# TASK 1
# fruit = ["Apple", "Bannana", "Cherry", "Date"]
# fruit.append("Elderberry")
# fruit.remove("Bannana")
# fruit.insert(1, "Elderberry")
# print(F"Number of fruits: {len(fruit)}")
# print(f"sorted fruits: {sorted(fruit)}")


# PART 2
# my_tuple = (10,20, 30)
# print(f"second value in tuple: {my_tuple[1]}")
# try:
    # my_tuple[0] = 5
    # print(my_tuple)
# except Exception as e:
    # print("Error:", e)

# for my_tuples in my_tuple:
    # print(my_tuples)


# PART3
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
student_grades["Diana"] = 92
student_grades["Charlie"] = 80
del student_grades["Alice"]

for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# student_grades = {
#            "Alice": {"Math": "85", "Science": 92, "English": 88},
#            "Bob": {"Math": 79, "Science": 85, "English": 90},
#            "Charlie": {"Math": 95, "Science": 89, "English": 87}}
# student_grades["Diana"] = {"Math": 88, "Science": 91, "English": 86}
# student_grades["Bob"]["Science"] = 90

# for student, grades in student_grades.items():
#     average_grade = sum(grades.value()) / len(grades)
#     print(f"{student}'set average is: {average_grade:.2f}")

# del student_grades["Charlie"]

# for student, grades in student_grades.tems():
#     print(f"{student}'s grades:")
#     print(f"Math: {grades['Math']}")
#     print(f"Science: {student['Science']}")
#     print(f"English: {student['English']}\n " )
