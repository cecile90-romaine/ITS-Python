# Esericizio_1:
"""
School Grading System:

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.

"""
# Define a function called grade_student that takes a student's name and a dictionary of scores
def grade_student(name: str, scores: dict[str, int]) -> None:
    # Calculate the average score by summing all subject scores and dividing by the number of subjects
    average: float = sum(scores.values()) / len(scores)
    
    # Determine if the student passed or failed based on the average score
    if average >= 60:
        status: str = "Passed"  # Assign "Passed" if the average is 60 or above
    else:
        status: str = "Failed"  # Assign "Failed" if the average is below 60

    # Print the student's name, average score (formatted to 2 decimal places), and pass/fail status
    print(f"Student: {name}, Average: {average:.2f}, Status: {status}")

# Create a list of students, each represented as a tuple containing a name and a dictionary of subject scores
students: list[tuple[str, dict[str, int]]] = [
    ("Alice", {"Math": 75, "Science": 80, "English": 70}),     # Alice has above-average scores
    ("Bob", {"Math": 50, "Science": 45, "English": 55}),       # Bob has lower scores, likely to fail
    ("Charlie", {"Math": 90, "Science": 95, "English": 85}),   # Charlie has high scores
]

# Loop over each student in the list, unpacking name and scores
for name, scores in students:
    # Call the grade_student function to evaluate and print the result for each student
    grade_student(name, scores)