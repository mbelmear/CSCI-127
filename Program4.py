import string

# ----------------------------------------
# CSCI 127, Joy and Beauty of Data       |
# Program 4: Presidents                  |
# Michael Belmear                        |
# Last Modified: March 20, 2021          |
# ---------------------------------------
# This program sorts the 46 US Presidents|
# by their number, name, time-in-office, |
# year-started, and previous occupations |
# based on what the user inputs.         |
# ---------------------------------------


def print_by_name(pres_listing, name):
    if len(name.lower())< 3:
        print("Must be at least 3 characters!")
        return
    for president in pres_listing:
        if name.lower() in president.get_name().lower():
            print(president)
        else:
            pass
            
def print_by_number(pres_listing, number):
    for president in pres_listing:
        if number == president.get_number():
            print(president)
        else:
            pass
    
def count_by_occupation(pres_listing, occupation):
    occupationlst = []
    for president in pres_listing:
        if occupation in president.get_occupation():
            if president.get_name() in occupationlst:
                continue
            else:
                occupationlst.append(president.get_name())
                print(president)
    
def average_term_length(pres_listing):
    termlen = []
    for president in pres_listing:
        termlen.append(president.get_time_in_office())
    print("The average term length is about " + str(round(sum(termlen)/len(pres_listing), 1)) + " " + "years.")



#---------------------------------------

class President:
    def __init__(self, first, last, number, start_in, term, occupations):
        self.name = first + " " + last
        self.number = number
        self.start_in = start_in
        self.time_in_office = term
        self.occupations = occupations

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_occupation(self):
        return self.occupations

    def get_time_in_office(self):
        return self.time_in_office

    def __str__(self):
        return ("No. " + str(self.number) + " " + '(' + str(self.start_in) + ')' + " " + self.name)

# ---------------------------------------

def print_menu():
    print ("""
1. Print all presidents
2. Print president by name
3. Print president by number
4. Count presidents with occupation
5. Print average term length
6. Quit
    """)
# ---------------------------------------

def print_all_presidents(pres_listing):
    for president in pres_listing:
        print(president)
    
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pres_listing(filename):
    pres_listing = []
    file = open(filename, "r")
    
    for president in file:
        presilist = president.strip().split(",")
        number = int(presilist[0])               # number
        last = presilist[1]                      # last name
        first = presilist[2]                     # first name
        start_in = int(presilist[3])             # first year in office
        term = float(presilist[4])               # years in office
        occupations = []
        for position in range(5, len(presilist)):
            occupations += [presilist[position]] # occupation
        pres_listing += [President(first, last, number, start_in, term, occupations)]

    file.close()
    return pres_listing

# ---------------------------------------

def get_choice(low, high, message):
    
    legal_choice = False
    answer = input(message)
    while answer == "":
        answer = input(message)
    for char in answer:
        if char not in string.digits:
            print('ERROR: ', answer, "is not a number")
            return 0
    answer = int(answer)
    if (low > answer) or (answer > high):
        print('ERROR: ', answer, "is not a choice")
        return 0

    return answer

# ---------------------------------------

def main():
    pres_listing = create_pres_listing("pres_listing.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_all_presidents(pres_listing)
        elif choice == 2:
            name = input("Enter a president name: ").lower()
            print_by_name(pres_listing, name)
        elif choice == 3:
            number = get_choice(1, 46, "Enter a president number: ")
            print_by_number(pres_listing, number)
        elif choice == 4:
            occupation = input("Enter a president occupation: ").lower()
            count_by_occupation(pres_listing, occupation)
        elif choice == 5:
            average_term_length(pres_listing)
        elif choice == 6:
            print("Thank you.  Goodbye!")

# ---------------------------------------

main()
