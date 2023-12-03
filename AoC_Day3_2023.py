# AoC_Day3_2023.py

# --- Functions ---

# Function to check if a given character is a symbol in this problem
def isSymbol(c):
    # If c is not a number or a period, it's a symbol
    if c.isdigit() or c == '.':
        return False
    else:
        return True


def doNothing():
    x = 1+1
    # does nothing, but apparently Python expects an idented block after an
    # except that isnt just a comment



# Checks if any of the spots adjacent to the schematic at (i,j) are symbols,
# checking this for every spot of the number. Returns true if so, false if not
def symbolIsAdjacent(schematic, i, j, length):
    # There are 8 possible adjacencies: 4 diagonals, 2 top/bottom, 2 left/right

    for l in range(length):
        # Just throw everything into try-except blocks in case i or j are
        # at the edges of the matrix
        try:
            if isSymbol(schematic[i-1+l][j-1]):
               return True
        except IndexError:
            doNothing()
        try:
            if isSymbol(schematic[i+l][j-1]):
                return True
        except IndexError:
            doNothing()
        try:
            if isSymbol(schematic[i+1+l][j-1]):
                return True
        except IndexError:
            doNothing()
        try:
            if isSymbol(schematic[i-1+l][j]):
                return True
        except IndexError:
            doNothing()
        try:
            if isSymbol(schematic[i+1+l][j]):
                return True
        except IndexError:
            doNothing()
        try:
            if isSymbol(schematic[i-1+l][j+1]):
                return True
        except IndexError:
            doNothing()
        try:
            if isSymbol(schematic[i+l][j+1]):
                return True
        except IndexError:
            doNothing()
        try:
           if isSymbol(schematic[i+1+l][j+1]):
                return True
        except IndexError:
            doNothing()
    

    # If none of these returned as symbols, there's no adjacent symbols
    return False


# Function to identify and return the length of a number that was found in input
def identifyNumberLength(schematic, i, j):
    length = 1
    # Increment the length while the next index contains a number
    try:
        while schematic[i+1][j].isdigit():
            length += 1
            i += 1
    except IndexError: # Handles some edge case
        doNothing()

    return length


# Function to return number from matrix given its initial indices and length
def constructNumber(schematic, i, j, length):
    numberStr = ""
    for l in range(length):
        numberStr += schematic[i+l][j]

    return int(numberStr)


# Finds the starting index of a found number and returns this as a list [x, y]
def findNumberStartPoint(schematic, i, j):
    # Walk backwards until start of row or no more digits
    x = i
    while x >= 0 and schematic[x-1][j].isdigit():
        x -= 1

    return [x, j]
    
# Function to return the gear ratio of a * (returns 0 if the * is not a gear)
def findGearRatio(schematic, i, j):

    # list of distinct numbers adjacent to this *
    listOfAdjacentNums = []
    
    # There are 8 possible adjacencies: 4 diagonals, 2 top/bottom, 2 left/right
    try:
        if schematic[i-1][j-1].isdigit():
            # Figure out the number we've found
            coordinates = findNumberStartPoint(schematic, i-1, j-1)
            x = coordinates[0]
            y = coordinates[1]
            numLength = identifyNumberLength(schematic, x, y)
            num = constructNumber(schematic, x, y, numLength)
            # If this number isnt in the list of adjacent numbers, add it
            if num not in listOfAdjacentNums:
                listOfAdjacentNums.append(num)
    except IndexError:
        doNothing()
    try: # The rest of this function is just the above repeated as needed
        if schematic[i][j-1].isdigit():
            coordinates = findNumberStartPoint(schematic, i, j-1)
            x = coordinates[0]
            y = coordinates[1]
            numLength = identifyNumberLength(schematic, x, y)
            num = constructNumber(schematic, x, y, numLength)
            if num not in listOfAdjacentNums:
                listOfAdjacentNums.append(num)
    except IndexError:
        doNothing()
    try:
        if schematic[i+1][j-1].isdigit():
            coordinates = findNumberStartPoint(schematic, i+1, j-1)
            x = coordinates[0]
            y = coordinates[1]
            numLength = identifyNumberLength(schematic, x, y)
            num = constructNumber(schematic, x, y, numLength)
            if num not in listOfAdjacentNums:
                listOfAdjacentNums.append(num)
    except IndexError:
        doNothing()
    try:
        if schematic[i-1][j].isdigit():
            coordinates = findNumberStartPoint(schematic, i-1, j)
            x = coordinates[0]
            y = coordinates[1]
            numLength = identifyNumberLength(schematic, x, y)
            num = constructNumber(schematic, x, y, numLength)
            if num not in listOfAdjacentNums:
                listOfAdjacentNums.append(num)
    except IndexError:
        doNothing()
    try:
        if schematic[i+1][j].isdigit():
            coordinates = findNumberStartPoint(schematic, i+1, j)
            x = coordinates[0]
            y = coordinates[1]
            numLength = identifyNumberLength(schematic, x, y)
            num = constructNumber(schematic, x, y, numLength)
            if num not in listOfAdjacentNums:
                listOfAdjacentNums.append(num)
    except IndexError:
        doNothing()
    try:
        if schematic[i-1][j+1].isdigit():
            coordinates = findNumberStartPoint(schematic, i-1, j+1)
            x = coordinates[0]
            y = coordinates[1]
            numLength = identifyNumberLength(schematic, x, y)
            num = constructNumber(schematic, x, y, numLength)
            if num not in listOfAdjacentNums:
                listOfAdjacentNums.append(num) 
    except IndexError:
        doNothing()
    try:
        if schematic[i][j+1].isdigit():
            coordinates = findNumberStartPoint(schematic, i, j+1)
            x = coordinates[0]
            y = coordinates[1]
            numLength = identifyNumberLength(schematic, x, y)
            num = constructNumber(schematic, x, y, numLength)
            if num not in listOfAdjacentNums:
                listOfAdjacentNums.append(num)
    except IndexError:
        doNothing()
    try:
        if schematic[i+1][j+1].isdigit():
            coordinates = findNumberStartPoint(schematic, i+1, j+1)
            x = coordinates[0]
            y = coordinates[1]
            numLength = identifyNumberLength(schematic, x, y)
            num = constructNumber(schematic, x, y, numLength)
            if num not in listOfAdjacentNums:
                listOfAdjacentNums.append(num)
    except IndexError:
        doNothing()

    # If the list of adjacent numbers is 2 long, return those 2 nums multiplied
    # Otherwise, it's not a gear so return 0
    if len(listOfAdjacentNums) == 2:
        return listOfAdjacentNums[0] * listOfAdjacentNums[1]
    else:
        return 0


# --- Main program code starts here ---


# Input is 140x140, demo input is 10x10, program assumes square matrix as input
inputLength = 140

# Initialize sums to 0
sumOfParts = 0
sumOfGearRatios = 0

# Create 2D list, initially assigning all indices a value of 0
schematic = [[0 for i in range(inputLength)] for j in range(inputLength)] 

# Loop through all the lines of input
for j in range(inputLength):
    thisLine = input()
    
    # Loop through all characters in each line, add to the 2D matrix
    for i in range(inputLength):
        schematic[i][j] = thisLine[i]


# Loop through the 2D matrix to find numbers and determine if they are parts
for j in range(inputLength):

    # While loop used since i is incremented by a number's length when one is
    # found to avoid counting a number multiple times
    i = 0
    while i < inputLength:
        if schematic[i][j].isdigit():
            numLength = identifyNumberLength(schematic, i, j)
            thisNumber = constructNumber(schematic, i, j, numLength)
            if symbolIsAdjacent(schematic, i, j, numLength):
                # This number is a part number
                sumOfParts += thisNumber

            # Skip over this number by incrementing i by the number's length
            i += numLength
            
        # Increment i by 1
        i += 1


# Loop through the 2D matrix again to find *'s and add their gear numbers
for j in range(inputLength):

    # Loop through each character in the row
    for i in range(inputLength):
        if schematic[i][j] == '*': # If it's a *, add its gear number
            sumOfGearRatios += findGearRatio(schematic, i, j)



print(f"sum of part numbers = {sumOfParts}")
print(f"sum of gear ratios = {sumOfGearRatios}")
