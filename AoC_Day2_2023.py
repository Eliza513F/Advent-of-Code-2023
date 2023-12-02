# AoC_Day2_2023.py

# Initial variables
sum = 0
thisLine = ""
addThisID = True

# Initial variables for part 2
powerSum = 0
minRed = 0
minGreen = 0
minBlue = 0

# Loop through each line
for gameID in range(1, 101, 1):
    thisLine = input()

    # The sequence of games is in the 2nd index of this list now
    games = thisLine.split(": ")

    # results in a list of str alternating between number and colour
    cubeAmounts = games[1].split(" ")

    # Iterate through every even index of cubeAmounts
    # even indices = number, odd indices = colour
    for i in range(0, len(cubeAmounts), 2):
        if int(cubeAmounts[i]) > 14:
            # This game is impossible no matter the colour
            addThisID = False
        elif int(cubeAmounts[i]) > 13 and "blue" not in cubeAmounts[i+1]:
            # Game is impossible, 14 or more but not blue
            addThisID = False
        elif int(cubeAmounts[i]) > 12 and "red" in cubeAmounts[i+1]:
            # Game is impossible: more than 12 reds
            addThisID = False

    if addThisID:
        sum += int(gameID) # Adds the game's ID

    # Reset addThisID to be true by default
    addThisID = True

    # Iterate through every odd index to find its colour, then check if the
    # minimum number of that colour needed needs to be updated
    for i in range(1, len(cubeAmounts), 2):
        if "red" in cubeAmounts[i]:
            if int(cubeAmounts[i-1]) > minRed:
                minRed = int(cubeAmounts[i-1])
        elif "green" in cubeAmounts[i]:
            if int(cubeAmounts[i-1]) > minGreen:
                minGreen = int(cubeAmounts[i-1])
        else: # blue is in cubeAmounts[i]
            if int(cubeAmounts[i-1]) > minBlue:
                minBlue = int(cubeAmounts[i-1])

    # Add to the power sum accordingly, reset min colour values
    powerSum += minRed * minGreen * minBlue
    minRed = 0
    minGreen = 0
    minBlue = 0
    

print(f"sum of valid gameIDs is {sum}")
print(f"sum of powers of all games is {powerSum}")
