# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Lab 2: Season Checker
# Michael Belmear
# Last Modified: January 28, 2021
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------


# TODO: write a function called season_checker that returns
#  a string: Spring, Summer, Winter, Fall, or Invalid

def main():
    user_month = input("Enter month: ")
    user_day = int(input("Enter day: "))
    season = season_checker(user_month, user_day)
    print(season) 

    # TODO: output the season for the user in a print statement,
    # or tell them if they input an invalid date

def season_checker(month, day):

    if ((month == "March" and day > 19 and day < 32) or (month == "April" and day > 1 and day < 31) or (month == "May" and day > 1 and day < 32) or (month == "June" and day > 1 and day < 21)):
        return ("That's a Spring day.")
    if ((month == "June" and day > 20 and day < 31) or (month == "July" and day > 1 and day < 32) or (month == "August" and day > 1 and day < 32) or (month == "September" and day > 1 and day < 22)):
        return ("That's a Summer day.")
    if ((month == "September" and day > 21 and day < 31) or (month == "October" and day > 1 and day < 32) or (month == "November" and day > 1 and day < 31) or (month == "December" and day > 1 and day < 21)):
        return ("That's a Fall day.")
    if ((month == "December" and day > 20 and day < 32) or (month == "January" and day > 1 and day < 32) or (month == "February" and day > 1 and day < 30) or (month == "March" and day > 1 and day < 20)):
        return ("That's a Winter day.")
    else:
        return ("That's an unrecognized date.")
    

main()

 
