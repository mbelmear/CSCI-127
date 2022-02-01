# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Classics CSV Library          |
# Michael Belmear                          |
# Last Modified: March 4, 2021             |
# -----------------------------------------+
# This program finds the longest book by   |
# word count, a range of books by the      |
# difficulty level input by the user, a    |
# list of all the books by a particular    |
# author, and a list of the oldest authors.|
# -----------------------------------------+

def longest(book):
    input_file = open("classics.csv", 'r', encoding = "ISO-8859-1")#assigning the variable input file to the csv file we need to open.
    input_file.readline()#converting the file into something we can iterate
    numwords = {}#making an empty dictionary 
    for line in input_file:#for every line in the csv file
        book_info = line.split(',')#splitting the file into a list 
        numwords[book_info[3]] = int(book_info[-1][:-2])
    inverse = [(value, key) for key, value in numwords.items()]
    print("The longest book is",max(inverse)[1])
    #https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    #this prints out the key using the max value
        
def fk_difficulty_range(input_file, least, most):
    input_file = open("classics.csv", 'r', encoding = "ISO-8859-1")
    input_file.readline()
    diffrange = []#making an empty list 
    least = int(least)#making the variable least an integer for when we call it later
    most = int(most)#making the variable most an integer for when we call it later
    for line in input_file:#for every line in the csv file
        book_info = line.split(',')#spliting the file into something we can iterate
        grade = book_info[23]#assigning the variable grade to the 23rd index in the file 
        grade = float(grade)#making grade a float
        title = book_info[3]#assigning the variable title to the 3rd index in the file
        book_grade = (grade, title)#assign the variable book_grade to consist of the grade and title variables as index 0 and 1
        diffrange.append([grade, title])#putting grade and title into the empty list 
        diffrange.sort()#putting the list into ascending order by grade level
    for i in range(least, most + 1):#for every element in the range least-most 
        print(str(i) + " " + str(diffrange[i][1]) + " - " + title + " - " + "Grade Level: " + str(diffrange[i][0]))#print the title and grade level

def all_books_by_author(input_file, author):
    input_file = open("classics.csv", 'r', encoding = "ISO-8859-1")
    input_file.readline()
    for line in input_file:
        book_info = line.split(',')
        name = book_info[11]#name is assigned to the 11th index in the csv file
        if author in name:#if the author is in the name 
            title = book_info[3]#the title is assigned to the third index of the csv file
            name = name.split(';')#spliting the name variable into seomething we can iterate
            first = name[1]#the variable first gets the second index of the name variable
            last = name[0]#the variable last gets the first index of the name variable
            if author == last:#if author is equal to the last variable
                print(title + " by " + first + " " + last)#then print the title followed by the first and last name of the author
        else:
            pass#if not then skip it

def authors_birth(input_file):
    input_file = open("classics.csv", 'r', encoding = "ISO-8859-1")
    input_file.readline()
    oldest = []#making an empty list
    for line in input_file:#for every line in the csv file
        book_info = line.split(',')#split the file into something we can iterate
        name = book_info[11]#assigning the name variable to the 11th index of the csv file 
        year = book_info[9]#assigning the year variable to the 9th index of the csv file
        if name not in oldest:#if the name is not in the list 
             oldest.append([name, year])#add the name and year to the list
        else:
            pass#if so then skip it
        oldest.sort()#sort the list into alphabetical order
    searched = []#make a new empty list
    for author in oldest:#for every author in the first list
        if author[0] == "Anonymous" or author[1] == 0:#if a term in oldest list is anonymous or 0 
            continue#skip it
        elif author in searched:
            continue#otherwise if the author is in the new list then continue       
        else:
            print(author[0] + " was born in " + author[1])#print the author and the year they were born
            searched.append(author)#alphabetize the list    

# -----------------------------------------+
# Do not change anything below this line   |
# with the exception of code related to    |
# option 4.                                |
# -----------------------------------------+

# -----------------------------------------+
# menu                                     |
# -----------------------------------------+
# Prints a menu of options for the user.   |
# -----------------------------------------+

def menu():
    print()
    print("1. Identify the longest book by word count.")
    print("2. List a range of books by difficulty rating.")
    print("3. Identify all books by certain author.")
    print("4. Print authors and their birth years in alphabetical order.")
    print("5. Quit.")
    print()
    
# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Repeatedly query the user for options.   |
# -----------------------------------------+

def main():
    input_file = "classics.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            longest(input_file)
        elif (choice == 2):
            least = input("Enter least difficult out of 1000 (e.g. 250): ")
            most = input("Enter most difficult out of 1000 (e.g. 300): ")
            print("Using the Flesch–Kincaid grade level formula.")
            fk_difficulty_range(input_file, least, most)
        elif (choice == 3):
            author = input("Enter last name of author (e.g. Dickens): ")
            all_books_by_author(input_file, author)
        elif (choice == 4):
            authors_birth(input_file)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

main()
