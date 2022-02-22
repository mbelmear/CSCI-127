# --------------------------------------
# CSCI 127, Lab 6                      |
# March 4, 2021                        |
# Michael Belmear                      |
# --------------------------------------

def first2third(translate, gender, name):
    f2tm = {"me":"him", "myself":"himself", "i":"he", "am":"is", "I'm":"he's", "my":"his", "have":"has", "want":"wants"}
    f2tf = {"me":"her", "myself":"herself", "i":"she", "am":"is", "I'm":"she's", "my":"hers", "have":"has", "want":"wants"}
    f2tn = {"me":"them", "myself":"themselves", "i":"they", "am":"are", "I'm":"they're", "my":"their", "have":"have", "want":"want"}
    translate = translate.lower()
    punctuation = '(,.?!;-,:)'
    for letter in translate:
        if letter in punctuation:    
                translate = translate.replace(letter, " " + letter)    
    translate = translate.split(" ")
    newsentence = " "
    newsentence = newsentence + " "
    for word in translate:   
        if (word in f2tm and gender == 'm'):
            newsentence = newsentence + " " + f2tm[word] + ""
        elif (word in f2tf and gender == 'f'):  
            newsentence = newsentence + " " + f2tf[word] + ""
        elif (word in f2tn and gender == 'n'):
            newsentence = newsentence + " " + f2tn[word] + ""
        else:
            newsentence = newsentence + " " + word  
    return("I'm asking for my friend" + "," + " " + name + "...\n" + newsentence)
  
        
def main():
    user_string = input("Enter the string to be translated: ")
    friend_name = input("Enter the name of the friend: ")
    print("Should " + friend_name + " be male, female, or no gender? ")
    friend_gender = ""
    while (friend_gender != 'm' and friend_gender != 'f' and friend_gender != 'n'):
        friend_gender = input("Enter m, f, or n: ").lower()
    translation = first2third(user_string, friend_gender, friend_name)
    print(translation)
    
    
main()
