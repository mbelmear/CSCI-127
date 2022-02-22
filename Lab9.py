
import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 9
# Month __, 20__
# Your Name
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die with given number of sides"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Farkle:

    def __init__(self, sides):
        """A constructor method that can record 6 dice rolls"""
        self.rolls = np.zeros(6, dtype=np.int16)
        self.sides = sides

    def roll_dice(self):
        """A general method that rolls 6 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(self.sides).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(self.sides + 1, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts
        
#--------------------------------------------------

    def is_it_four_of_a_kind(self):
        if 4 in self.count_outcomes():#if there is a four in the array 
            return True#return true meaning that there is four of a kind
        else:
            return False#otherwise return false as there isn't four of a kind in that particular array
    
    def is_it_straight(self):
        sortedarray = np.sort(self.rolls)#sort the array by increasing number 1,2,3,4,5 etc...
        for i in range(len(sortedarray)-1):#for every number in the range of the length of sorted array - 1  
            if(sortedarray[i] +1 == sortedarray[i+1]):#if the dice is equal to the next numbered dice 
                continue#then continue
            else:
                return False#otherwise return false meaning that particular array doesn't have a straight
    
        return True
    
    def is_it_two_triplets(self):
        count = 0#start counting at 0
        for ele in self.count_outcomes():#for every element in the count_outcomes method
            if ele == 3:#if there is a 3
                count += 1#make count equal to 1
        if count == 2:#so if there is more than one 3 and count is equal to 2
            return True #return true meeaning there is two triplets

# -------------------------------------------------
        
def main(how_many):

    four_of_a_kind = 0
    straight = 0
    two_triplets = 0
    game = Farkle(6)

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_four_of_a_kind():
            four_of_a_kind += 1
        elif game.is_it_straight():
            straight += 1
        elif game.is_it_two_triplets():
            two_triplets += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    
    print("Number of Four of a Kinds:", four_of_a_kind)
    print("Percent:", "{:.2f}%\n".format(four_of_a_kind * 100 / how_many))
    print("Number of Straights:", straight)
    print("Percent:", "{:.2f}%\n".format(straight * 100 / how_many))
    print("Number of Two Triplets:", two_triplets)
    print("Percent:", "{:.2f}%".format(two_triplets * 100 / how_many))

# -------------------------------------------------

main(1000)
    
        
