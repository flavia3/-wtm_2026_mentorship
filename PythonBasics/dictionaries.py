# 8. Student Profile
student_profile = {
    "Name": "Michaella Chloe", 
    "Age": 20, 
    "Course": "Computer Science",
    "Level": "Undergraduate",
    "Skills": ["Python", "Data Analysis", "Graphics Design"]
}
print(f"Student Profile: {student_profile}")    

print(f"Student Name: {student_profile['Name']}")

student_profile["Email"] = "michechloe@gmail.com"
print(f"Updated Student Profile: {student_profile}")

student_profile["Level"] = "Graduate"
print(f"Updated Student Level: {student_profile['Level']}")

student_profile.pop("Age")
print(f"Updated Student Profile after removing Age: {student_profile}")


