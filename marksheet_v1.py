print("Welcome to the Marksheet Generator")
print("Please Enter the Following Details:")

subjects = ["English", "Maths", "Physics", "Chemistry", "Computer"]
obtained_marks = {}

def input_marks():
    print("\nEnter Marks for Each Subject (0-100):")
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    obtained_marks[subject] = mark
                    break
                else:
                    print("Invalid! Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a number.")

# Student Details
name = input("\nEnter Your Name: ")
roll = input("Enter Your Roll Number: ")
clas = input("Enter Your Class: ")
section = input("Enter Your Section: ")

input_marks()  # Get validated marks

# Calculations
total_obtained = sum(obtained_marks.values())
max_total = 100 * len(subjects)
percentage = (total_obtained / max_total) * 100

# Grade Determination
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display Marksheet
print("\n\n" + "=" * 50)
print("MARKSHEET".center(50))
print("=" * 50)
print(f"Name: {name}\t\tRoll Number: {roll}")
print(f"Class: {clas}\t\tSection: {section}")
print("-" * 50)
print(f"{'Subject':<20}{'Obtained':>10}{'Max Marks':>10}")
print("-" * 50)
for subject in subjects:
    print(f"{subject:<20}{obtained_marks[subject]:>10}{100:>10}")
print("-" * 50)
print(f"{'Total Marks':<20}{total_obtained:>10}{max_total:>10}")
print(f"\nPercentage: {percentage:.2f}%\t\tGrade: {grade}")
print("=" * 50)

# ... [previous code until grade determination]

# Custom Messages based on Grade
if grade == "A+":
    message = "Outstanding achievement! Keep shining! ✨"
elif grade == "A":
    message = "Excellent performance! Well done! 🎉"
elif grade == "B":
    message = "Good work! Keep improving! 💪"
elif grade == "C":
    message = "Satisfactory. Aim higher next time! 🔥"
elif grade == "D":
    message = "Passed, but needs more effort. 📚"
else:
    message = "Needs improvement. Seek guidance! 🤝"

# Display Marksheet
print("\n\n" + "=" * 50)
print("MARKSHEET".center(50))
print("=" * 50)
print(f"Name: {name}\t\tRoll Number: {roll}")
print(f"Class: {clas}\t\tSection: {section}")
print("-" * 50)
print(f"{'Subject':<20}{'Obtained':>10}{'Max Marks':>10}")
print("-" * 50)
for subject in subjects:
    print(f"{subject:<20}{obtained_marks[subject]:>10}{100:>10}")
print("-" * 50)
print(f"{'Total Marks':<20}{total_obtained:>10}{max_total:>10}")
print(f"\nPercentage: {percentage:.2f}%\t\tGrade: {grade}")
print("\n" + "=" * 50)
print(f"REMARKS: {message}".center(50))
print("=" * 50 + "\n")