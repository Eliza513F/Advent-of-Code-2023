# AoC_Day4_2023.py

# Initial variables
totalPoints = 0
linesOfInput = 209
winningCards = [[] for column in range(linesOfInput)]

# Part 2 variables
sumOfCardsHeld = 0
cardsHeld = [1] * linesOfInput # Create a list linesOfInput long of 1's


# Function to determine how many winning numbers a card has
def numOfWinningNumbers(line, winningCards):
    winningNumbers = 0
    
    lineParts = line.split("|") # Split it up to get just the scratch numbers
    cardNums = lineParts[1].split(" ") # Split scratch numbers up into a list
    
    for i in range(len(cardNums)): # Go through all scratch card numbers
        if cardNums[i] in winningCards:
            winningNumbers += 1

    return winningNumbers

    
# Loop through each line of input
for i in range(linesOfInput):
    rawLine = input()
    thisLine = rawLine.split(" ")
    
    # Loop through the part containing the winning cards
    j = 2
    while not thisLine[j] == "|": # will loop until it reaches |
        if not thisLine[j] == "": # Only add if its a number
            winningCards[i].append(thisLine[j])
        j += 1

    cardPoints = 0
    # Check all the cards after the | to see if theyre winning, if so add points
    while j < len(thisLine):
        if thisLine[j] in winningCards[i]:
            # If it's winning and no points yet, 1 point. Else double the points
            if cardPoints == 0:
                cardPoints = 1
            else:
                cardPoints *= 2
        j += 1

    totalPoints += cardPoints

    # Determine how many winning numbers this card has, and give more cards
    # accordingly
    winningNumbers = numOfWinningNumbers(rawLine, winningCards[i])

    # Add winningNumbers amount of cards to winningNumbers amount of cards below
    # this, multiplied by however many copies of this card we have
    for k in range(i+1, i+1+winningNumbers):
        cardsHeld[k] += cardsHeld[i]
        
# At the end, total up the cards held
for i in range(linesOfInput):
    sumOfCardsHeld += cardsHeld[i]

    
print(f"Sum of card points is {totalPoints}")
print(f"Number of cards held is {sumOfCardsHeld}")
