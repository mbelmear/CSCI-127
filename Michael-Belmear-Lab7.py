# -----------------------------------------------------
# CSCI 127, Lab 7
# March, 11 2021
# Michael Belmear
#
# This program returns a contact list and lets the user
# search for a contact. 
# -----------------------------------------------------

class Contact:
    """Contact class for representing and manipulating contacts"""

    def __init__(self, first, last, phone):
        """A constructor to initialize Contact attributes"""
        self.first = first
        self.last = last
        self.phone_number = phone
        self.title = ''
        self.full_name = self.first + ' ' + self.last
                
    def set_first_name(self, first):
        self.first = first
        self.full_name = first + ' ' + self.last
    def set_last(self, last):
        self.last = last
        self.full_name = self.first + ' ' + last
    def set_phone_number(self, phone):
        self.phone = phone
    def set_title(self, title):
        self.title = title
    def get_first_name(self):
        return self.first
    def get_last(self):
        return self.last
    def get_phone_number(self):
        return self.phone_number
    def get_title(self):
        return self.title
    def get_full_name(self):
        return self.full_name
    
    def print_entry(self):
        """method to print contact"""
        space = 50 - len(self.full_name)
        if self.title != '':
            space = 50 - (len(self.full_name) + len(self.title) + 2)
            print(self.full_name + ", " + self.title + self.phone_number.rjust(space, '.'))
        else:
            print(self.full_name + self.phone_number.rjust(space, '.'))
    
# -----------------------------------------------------

# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("CONTACTS".center(50, '-'))
    for person in contacts:
        person.print_entry()
    print("".center(50, '-'))

# -----------------------------------------------------

def search_contacts(contacts):

    search_string = input("Search for contact: ") 
    found = False
    if search_string == "":
        return 0
    for contact in contacts:
        if (search_string.lower() in contact.get_full_name().lower()):
            contact.print_entry()
            found = True
        if (search_string.lower() in contact.get_phone_number().lower()):
            contact.print_entry()
            found = True
    if not found:
        print("Search string not found.")
        
# -----------------------------------------------------

def main():
    
    prof = Contact("Daniel", "DeFrance", "406-994-1624")
    mascot = Contact("Bobcat", "", "unlisted")
    mascot.set_first_name("Champ")
    cs_dept_head = Contact("John", "Paxton", "406-994-5979")
    cs_dept_head.set_title("Department Head")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    president.set_title("President")
    
    contacts = [prof, mascot, cs_dept_head, president]
    
    done = False
    while not done:
        print()
        user_input = input("[P]rint contacts, [S]earch contacts, [Q]uit: ")
        if user_input.lower() == 'p':
            print()
            print_directory(contacts)
        elif user_input.lower() == 's':
            print()
            search_contacts(contacts)
        elif user_input.lower() == 'q':
            done = True
        else:
            print("Enter P, S, or Q")
    
# -----------------------------------------------------

main()
