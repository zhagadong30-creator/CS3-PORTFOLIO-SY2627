import random

# Code template to use with function call to analyze_grades
def analyze_grades(grades):
    # Insert your code here
    for i, grade in enumerate(grades):
        if grade >= 60:
            print("student" + str(i) + " passed")
        else:
            print("student" + str(i) + " failed")
    pass


# Grades of students is randomized
class_grades = [round(random.uniform(0.0, 100.0),2) for _ in range(5)]
# Example of how to print multiple values in 1 line
print("Grades:", class_grades)

print("Average grade:", sum(class_grades) / len(class_grades))
