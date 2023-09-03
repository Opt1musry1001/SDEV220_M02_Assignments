# SDEV220_M02_Lab_CaseStudy.py
# Author: Ryan Moore
# Date: 9/2/23
# Collects student's name and GPA and determines whether
# the student is on the Dean's List or Honor Roll.

# Get student's last name or quit.
lastName = input("Please enter the student's last name or ZZZ to quit: ")

# Get the rest of the student's info and test qualifications.
while lastName != 'ZZZ':
    firstName = input("Please enter the student's first name: ")
    GPA = float(input("Please enter the student's GPA: "))

    # Make sure GPA is valid.
    while (GPA < 0) or (GPA > 5):
        GPA = float(input("Please enter a valid GPA: "))

    # Test GPA.
    if GPA >= 3.5:
        print(firstName, lastName, "has made the Dean's List.")
    elif GPA >= 3.25:
        print(firstName, lastName, "has made the Honor Roll.")
    else:
        print(firstName, lastName, "is not on the Dean's List or the Honor Roll.")
    
    # Get new student or quit.
    lastName = input("Please enter the student's last name or ZZZ to quit: ")

# Exit message.
print("Program ended successfully.")
