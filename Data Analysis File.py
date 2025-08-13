Monday = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN,"

Tuesday = "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE,"

Wednesday = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE,"


Thursday = "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN,"

Friday = "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"

addAllColours = Monday+Tuesday+Wednesday+Thursday+Friday 

AllColours = [colours.strip() for colours in addAllColours.split(',')]

def EachDayColours(days):
    
    colours= []
    for colour in days:
        if colour not in colours:
            colours.append(colour)
    return colours



total_colours = EachDayColours([colours.strip() for colours in addAllColours.split(',')])

print(f"The mean of colour is : {len(AllColours)/len(total_colours)}")

def numberOfEachColour(colour):
    length_of_colour = [colours for colours in AllColours if colours == colour]
    return len(length_of_colour)

def theMostColour():
    colour_with_itsNumberDict = []

    for colour in total_colours:
        Each_colour_values = {
        colour : numberOfEachColour(str(colour))
        
        }
        colour_with_itsNumberDict.append(Each_colour_values)
    colour_Dict_Flatten = {key: value for data in colour_with_itsNumberDict for key, value in data.items() }
    highest_value = max(colour_Dict_Flatten, key=colour_Dict_Flatten.get)
    print(f"{highest_value} with a value of {colour_Dict_Flatten[highest_value]} is the highest value")
    
    
theMostColour()


def showMedian():
    sorted_colours = sorted(AllColours)
    median_indicator_value = len(AllColours)//2
    print(f"The median colour is:  {sorted_colours[median_indicator_value]}")
    
showMedian()