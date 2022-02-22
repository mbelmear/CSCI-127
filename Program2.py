# -----------------------------------------+
# Michael Belmear                          |
# CSCI 127, Program 2                      |
# Last Updated: February 16, 2021          |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+

def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result

def royal_flush(hand):
##    print(hand)
    for i in range(len(hand)-1):
        if(hand[i][1] == hand[i+1][1]): #if the card and the next card are the same suit
            continue
        else:
            return False

    if(hand[0][0] == 10):
        for i in range(len(hand)-1):
            if(hand[i][0] +1 == hand[i+1][0]): #if the card + 1 equals the value on the next card
               continue
            else:
                return False
        return True
    # if hand contains 10-14 and all same suit
##        return True
##    else:
##        return False

def straight_flush(hand):
    for i in range(len(hand)-1):
        if(hand[i][1] == hand[i+1][1]): #if the card and the next card are the same suit
            continue
        else:
            return False

    if(hand[0][0] != 10):
        for i in range(len(hand)-1):
            if(hand[i][0] +1 == hand[i+1][0]): #if the card + 1 equals the value on the next card
               continue
            else:
                return False
        return True 
    return False

def straight(hand):
    for i in range(len(hand)-1):
            if(hand[i][0] +1 == hand[i+1][0]): #if the card + 1 equals the value on the next card
               continue
            else:
                return False
    
    return True

def four_of_a_kind(ranks):
    
    if not full_house(ranks):
       count = 0
       for i in range(len(ranks)-1):
            if(ranks[i] == ranks[i+1]):
                count += 1
       if (count == 3):
           return True
       else:
            return False
            
def full_house(ranks):
    count = 0
    for i in range(len(ranks)-1):
        if(ranks[i] == ranks[i+1]):
            count += 1
    if (count == 3):
        
        if (ranks[1] != ranks[3]):
            return True
    else:
        return False
        
    
def three_of_a_kind(ranks):
    if not two_pair(ranks):
        count = 0
        for i in range(len(ranks)-1):
            if(ranks[i] == ranks[i+1]):
                count += 1
        if (count == 2):
            return True
        else:
            return False
    

def two_pair(ranks):
    if (ranks[0] == ranks[1] and ranks[2] == ranks[3]):
        return True
    if (ranks[1] == ranks[2] and ranks[3] == ranks[4]):
        return True
    if (ranks[0] == ranks[1] and ranks[3] == ranks[4]):
        return True
    else:
        return False
    
    
def one_pair(ranks):
    if (ranks[0] == ranks[1]):
        return True
    if (ranks[2] == ranks[3]):
        return True
    if (ranks[3] == ranks[4]):
        return True
    else:
        return False


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort()
    poker_hand_ranks = get_all_ranks(poker_hand)
    print(poker_hand, "--> ", end="")
    if royal_flush(poker_hand):
        print("Royal Flush")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand_ranks):
        print("Four of a Kind")
    elif full_house(poker_hand_ranks):
        print("Full House")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand_ranks):
        print("Three of a Kind")
    elif two_pair(poker_hand_ranks):
        print("Two Pair")
    elif one_pair(poker_hand_ranks):
        print("One Pair")
    else:
        print("Nothing")
		
# -----------------------------------------+

def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[10, "spades"], [14, "spades"], [12, "spades"], [13, "spades"], [11, "spades"]])  # royal flush
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "clubs"]])           # straight flush
    evaluate([[2, "diamonds"], [7, "clubs"], [2, "hearts"], [2, "clubs"], [2, "spades"]])       # 4 of a kind
    evaluate([[8, "diamonds"], [7, "clubs"], [8, "hearts"], [8, "clubs"], [7, "spades"]])       # full house
    evaluate([[13, "diamonds"], [7, "clubs"], [7, "hearts"], [8, "clubs"], [7, "spades"]])      # 3 of a kind
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "spades"]])          # straight
    evaluate([[10, "spades"], [9, "clubs"], [6, "diamonds"], [9, "diamonds"], [6, "hearts"]])   # 2 pair
    evaluate([[10, "spades"], [12, "clubs"], [6, "diamonds"], [9, "diamonds"], [12, "hearts"]]) # 1 pair
    evaluate([[2, "spades"], [7, "clubs"], [8, "diamonds"], [13, "diamonds"], [11, "hearts"]])  # nothing

# -----------------------------------------+

main()
