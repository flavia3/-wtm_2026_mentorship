# 1. Personal Information 
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height in cm: ")
student_status = input("Are you a student? (yes/no): ")

print(f"Hello {name}, you are {age} years old and {height} cm tall.")
if student_status == "yes":
    print("You are a student.")
else:
    print("You are not a student.")

# 2. Identify the Data Types
name = "Abdurrahman" 
age = 25 
height = 1.75 
is_student = True 

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")

