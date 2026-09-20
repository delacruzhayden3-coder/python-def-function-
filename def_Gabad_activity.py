# This def function calculates the average of three grades.

def calculate_average(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3
    return average


# Ask the user to enter three grades
grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))
grade3 = float(input("Enter third grade: "))

# Use the function to calculate the average
average = calculate_average(grade1, grade2, grade3)

# Display the calculated average
print("Your average grade is:", average)
