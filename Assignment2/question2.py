#  Student Grade Evaluator & Class Performance Tracker
count = int(input("How many student entries do you want to create? "))
student_records = {}

for i in range(count):
    print(f"\n--- Entry {i + 1} ---")

    name = input("Enter student name: ") #student's name
    score = float(input("Enter score (0-100): ")) #student's score

    # Store the student's name as the key and score as the value.
    student_records[name] = score

print("\n====================================")
print("EVALUATION RESULTS")
print("====================================")

# Create counters for passed and failed students.
passed = 0
failed = 0

# Go through each student and their score.
for name, score in student_records.items():
    # Check if the student scored 70 or above.
    if score >= 70:
        grade = "A"
        status = "Passed with Distinction"
        passed += 1

    # Check if the student scored 50 or above.
    elif score >= 50:
        grade = "B"
        status = "Passed"
        passed += 1

    # If the score is below 50.
    else:
        grade = "F"
        status = "Needs Improvement"
        failed += 1

    # Print the student's evaluation.
    print(
        f"- {name}: Score {score:.1f} | "
        f"Grade {grade} | {status}"
    )

# Calculate the total of all scores.
total_score = sum(student_records.values())

# Calculate the average score.
average_score = total_score / count

print("\n===================================")
print("CLASS PERFORMANCE")
print("======================================")

print(f"Average Score: {average_score:.1f}")
print(f"Total Passed: {passed}")
print(f"Total Failed: {failed}")
