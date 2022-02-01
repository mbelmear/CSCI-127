# --------------------------------------
# CSCI 127, Lab 5                      |
# February 25, 2021                    |
# Michael Belmear                      |
# --------------------------------------

def average_magnitude(magnitude):
    quakes = open('earthquakes.csv', 'r')#assinging the file to quakes
    quakes.readline()#turns the file into something we can iterate
    total = 0#start counting the magnitudes at 0 
    x = 0#the length the list starts at 0
    for line in quakes:#for every line in the quakes file
        i = line.split(',')#split the line into a list 
        x += 1#start counting the length of the list at 0
        total += float(i[-8])#total equals the list added together
    return total / x#divide the total by the length of the list
    

def earthquake_locations(location):
    quakes = open('earthquakes.csv', 'r')
    quakes.readline()
    x = 0
    loc = []
    for line in quakes:
        i = line.split(',')
        if i[-5] not in loc:
            loc.append(i[-5])
            x += 1
    loc.sort()
    y = 0
    print("Alphabetical Order of Earthquake Locations")
    print("------------------------------------------")
    for region in loc:
        y += 1
        if y < 10:
            print(str(y) + ".  ", region)
        elif y < 100:
            print(str(y) + ". ", region)
        else:
            print(str(y) + ".", region)

    print()

def count_earthquakes(file_name, lower_bound, upper_bound):
    quakes = open('earthquakes.csv', 'r')
    quakes.readline()
    total = 0
    for line in quakes:
        i = line.split(',')
        if (float(i[-8]) >= lower_bound and float(i[-8]) <= upper_bound):
            total += 1
    return total

# --------------------------------------

def main(file_name):
    magnitude = average_magnitude(file_name)
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))
    
    earthquake_locations(file_name)
    
    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")
