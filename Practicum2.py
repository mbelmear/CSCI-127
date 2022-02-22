##def average_number_char(characters):
##    myfile = open("myfile.txt", 'r')#reading the file into the function
##    myfile.readline()#converting the file into something we can iterate
##    total = 0#start counting the characters at 0
##    x = 0#the length of the list starts at 0
##    
##    for char in myfile:#for every character in the txt file
##        i = char.split(',')#split the characters into a list
##        x += 1#start counting the length of the list at 0
##        total += float(i)#total now equals the list added together
##    return total / x#return the total by the length of the list
##
##def main():
##        characters = average_number_characters(file_name)
##        print("The average number of characters per line: {:.2f}\n".format(characters)) 
##        
##            
##main("myfile.txt")




##class Pants:
##
##    def __init__(self, length, width, price):#making the constructors for the object
##        self.length = length#making each constructor a variable
##        self.width = width
##        self.price = price
##
##    def get_length(self):#making getters
##        return self.length
##    def get_width(self):
##        return self.width
##    def get_price(self):
##        return self.price
##    def calc_cost(self, tax):#adding another attribute to calculate cost
##        cost = 0
##        tax = .07
##        calc_cost = (tax*self.price) + self.price
##        return calc_cost
##
##    def __str__(self):#using the __str__ method to return a formatted output
##        return str(self.length) + " x " + str(self.width) + ": " + str(self.price)
##    
##       
##        
##        
##def main():
##    SKU_123 = Pants(32, 34, 44.95) # length, waist, price
##    SKU_321 = Pants(34, 30, 24.99)
##    SKU_999 = Pants(40, 32, 90.00)
##
##    print(SKU_123)
##    print(SKU_321)
##
##    tax = .07
##    cost = SKU_999.calc_cost(tax)
##    print("The fancy 999 pants cost ${amount:.2f}".format(amount=cost))
##    
##main()

user_input = input("Enter a string of text: ")#prompts user to enter a string of text

def wordtypefreq(user_input):
    dict = {}#start with empty dictionary 
    for i in user_input:#for every line in the user input
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(wordtypefreq(user_input))

#https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-6.php, used this source to help me complete this problem
