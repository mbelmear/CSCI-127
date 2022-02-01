# --------------------------------------
# CSCI 127, Lab 3                      |
# February 4, 2021                     |
# Michael Belmear                      |
# -------------------------------------- 
# Calculate how many vowels are in a   |
# sentence using three techniques.     |
# --------------------------------------

def count_built_in(sentence):
    count = 0
    count += sentence.count("a")
    count += sentence.count("e")
    count += sentence.count("i")
    count += sentence.count("o")
    count += sentence.count("u")
    return count   
    
def count_iterative(sentence):
    count = 0
    for i in sentence:
        if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
            count += 1
    return count

def count_recursive(sentence):
    count = 0
    vowels = ("aeiouAEIOU")
    if (len(sentence) == 0):
        return 0
    if sentence[0] in vowels:
        return 1 + count_recursive(sentence[1:])
    return count_recursive(sentence[1:])
     

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of vowels  using ...")
        print("-------------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
