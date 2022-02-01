# --------------------------------------
# CSCI 127, Lab 4                      |
# February 11, 2021                    |
# Michael Belmear                      |
# -------------------------------------- 
# Calculate how many of each word are  |
# in a sentence using 2 techniques.    |
# --------------------------------------


def make_word_list(my_string):#making my_string the variable in this function
    punctuation = "(,.?!''-;:)"#assigning the variable punctuation, punctuation characters
    for e in my_string:  #for every element in my_string
        if e in punctuation:#if the elements in mystring contain punctuation
            my_string = my_string.replace(e, "")#replace them with an empty string
    my_string = my_string.lower() #converting my_string to lowercase
    my_list = (my_string.split()) #converting my_string into a list
    return(my_list) #return my_list




def count_freq_iteratively(my_list):
    words = []#words gets an empty list
    counts = []#counts gets an empty list 
    for word in my_list:#for every word in the empty list
        if word in words:#if a word is in the empty list already then skip it
            continue
        else:
            num_occ = my_list.count(word)#otherwise if word is not in the list already, count the number of occurances of that word in the list
            words.append(word)#add the word the list 
            counts.append(num_occ)#add the word count of that word to the list
        print(word, num_occ)#print the word and the number of times that it occurs




def count_freq_recursively(my_list):#defing mylist as the function to be counted
    if my_list == []:#base case if the list is empty program stops running
        return
    num_occ = my_list.count(my_list[0])#the number of occurances gets mylist counted starting at the first term
    print(my_list[0], num_occ)#printing the first word in mylist and the number of occurances
    count_freq_recursively(my_list[num_occ:])#counting the number of occurances of each word only once




def main():
    user_input = input("Enter words: ")
    print()
    words = make_word_list(user_input)

    print("Iterative Count: ")
    count_freq_iteratively(words)
    words.sort()
    
    print()
    print("Recursive Count: ")
    count_freq_recursively(words)


main()
