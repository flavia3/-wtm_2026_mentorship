# Assignment: Student Information Manager 
name = input("Enter your name: ")
age = int(input("Enter your age: ")) 
Height = float(input("Enter your height in cm: "))
is_currently_enrolled = (
    input("Are you currently enrolled? (yes/no): ").lower() == "yes"
)

# Check whether the student is enrolled
if is_currently_enrolled:
    print("You are enrolled.")
else:
    print("You are not enrolled.")

print(
    f"Hello {name}, you are {age} years old and "
    f"{Height} cm tall. Are you currently enrolled? "
    f"{'Yes' if is_currently_enrolled else 'No'}."
)

# 1. list
skills = ["Python", "HTML", "CSS", "JavaScript", "SQL"]

# Printing the first item in the list
print(f"My first skill is: {skills[0]}")

# Removing the one item in the list
skills.remove("CSS")

# printing the updated list
print(f"My skills are: {skills}")

# 2. Tuple 
favourite_numbers = (7, 10, 25)
print("Second favorite number:", favourite_numbers[1])

# 3. Set 
hobbies = {"Reading", "Gaming", "Football", "Reading", "Gaming"}
print("My hobbies are:", hobbies)

# The set will automatically remove duplicate values, so "Reading" and "Gaming" will only appear once in the output.

# adding a new hobby to the set
hobbies.add("Cooking")
print("After adding a new hobby, my hobbies are:", hobbies)

# 4. Dictionary
student_basic_info = {
    "name": "John",
    "age": 25,
    "height": 1.75,
    "is_enrolled": True,
    "skills": ["Python", "SQL", "Excel"],
    "favourite_numbers": (7, 10, 25),
    "hobbies": {"Reading", "Gaming", "Football"}
}
# printing the student's name
print(f"Student's name is: {student_basic_info['name']}")

# printing the student's skills
print(f"Student's skills are: {student_basic_info['skills']}")

# updating the student's age
student_basic_info["age"] = 21
print(f"After updating, the student's age is: {student_basic_info['age']}")

# printing the student's info
print(f"Student's basic information: {student_basic_info}")