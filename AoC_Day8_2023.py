# AoC_Day8_2023.py

import re

with open("AoC2023Inputs/Day8Input.txt") as inputFile:
    lines = inputFile.readlines()

# String of LR moves
moveSequence = lines[0]
moveSequence = moveSequence.strip() # Get rid of \n
#print(moveSequence)

# Remove unwanted brackets and commas from input and split them by spaces
for i in range(2, len(lines)):
    lines[i] = lines[i].replace("(", "")
    lines[i] = lines[i].replace(")", "")
    lines[i] = lines[i].replace(",", "")
    lines[i] = lines[i].split()

#print(lines)

# Create a dictionary to map from one node to its left/right travel options
travelMaps = {}
# Go over every line of input
for i in range(2, len(lines)):
    # startNode + L = leftNode, startNode + R = rightNode
    travelMaps[lines[i][0]+"L"] = lines[i][2]
    travelMaps[lines[i][0]+"R"] = lines[i][3]

#print(travelMaps)

# Count the steps it takes to get to ZZZ
steps = 0
currentNode = "AAA" # start at AAA

print(moveSequence)

#import time
#start_time = time.time()

# All this is part 1 stuff
"""i = 0
# Use a while loop to loop until we reach ZZZ
while (currentNode != "ZZZ"):
    # Use modulus since we can end up having to traverse the moveSequence many
    # times
    #print("moveSequence is " + moveSequence[i % len(moveSequence)])
    currentNode = travelMaps[currentNode+moveSequence[i % len(moveSequence)]]
    #print("currentNode is " + currentNode)
    i += 1
    steps += 1
    #print(currentNode)
    #time.sleep(1)
    #print(i)"""

# List of current nodes
currentNodes = []

print(steps)
#print(f"So far taken %s seconds" % (time.time() - start_time))
