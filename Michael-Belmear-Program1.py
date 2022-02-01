# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Michael Belmear
# Last Modified: Month 2,1,2021
# ---------------------------------------
# This Program calculates your GPA
# ---------------------------------------


def translate(letter_grade):
    letter_grade = letter_grade.lower()
    if (letter_grade == "a"):
        return (4.0)
    elif (letter_grade == "a-"):
        return (3.7)
    elif (letter_grade == "b+"):
        return (3.3)
    elif (letter_grade == "b"):
        return (3.0)
    elif (letter_grade == "b-"):
        return (2.7)
    elif (letter_grade == "c+"):
        return (2.3)
    elif (letter_grade == "c"):
        return (2.0)
    elif (letter_grade == "c-"):
        return (1.7)
    elif (letter_grade == "d+"):
        return (1.0)
    elif (letter_grade == "f"):
        return (0.0)
    


def main():
    course = int(input("Enter the number of courses you are taking: "))
    print()
    totalGradePoint = 0
    totalCredits = 0   
    for i in range(course):
        letter_grade = input("Enter grade for course " + str((i+1))+": ")
        credit = int(input("Enter credits for course " +str((i+1))+": "))
        nbrgrd = translate(letter_grade)
        totalGradePoint += (nbrgrd)*(credit)
        totalCredits += credit
        print()

    GPA = (totalGradePoint)/(totalCredits)
    input("Your GPA is " +str(round(GPA,2)))
    


main()

