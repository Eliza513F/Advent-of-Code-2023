# AoC_Day9_2023.py

# Function to determine if a sequence is all 0's
def sequenceIsAllZeroes(sequence):
    # Loop through every number in the sequence to determine if it's a 0
    for i in range(len(sequence)):
        if sequence[i] != 0:
            return False
    return True # Didn't find any non-0's in the sequence
    
# Recursive function to determine the next value in the sequence
def findNextValue(sequence):
    # base case: the current sequence is all 0's
    if sequenceIsAllZeroes(sequence):
        sequence.append(0)
        return sequence # Return this sequence with an added 0

    # If this sequence is not all 0's, create a sequence that is the difference
    # between each element of the current sequence
    newSequence = []
    for i in range(1, len(sequence)):
        newSequence.append(sequence[i] - sequence[i-1])
    
    # Recursively call this function
    newSequence = findNextValue(newSequence)

    # Return the original sequence with a new last element of the sum of the
    # original sequence and the next value in it
    sequence.append(sequence[i] + newSequence[-1])
    return sequence

# Recursive function to determine the previous value in the sequence for part 2
def findPrevValue(sequence):
    # base case: the current sequence is all 0's
    if sequenceIsAllZeroes(sequence):
        sequence.insert(0, 0) # Add a 0 to the start of the list
        return sequence # Return this sequence

    # If this sequence is not all 0's, create a sequence that is the difference
    # between each element of the current sequence
    newSequence = []
    for i in range(1, len(sequence)):
        newSequence.append(sequence[i] - sequence[i-1])
    
    # Recursively call this function
    newSequence = findPrevValue(newSequence)

    # Return the original sequence with a new first element of the difference
    # between the old first element and the backwards extrapolated value in it
    sequence.insert(0, sequence[0] - newSequence[0])
    return sequence


# --- Main part of program below---

with open("AoC2023Inputs/Day9Input.txt") as inputFile:
    lines = inputFile.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].split() # Split the input lines into lists of digits
    for j in range(len(lines[i])): # Cast the digits in these lines to ints
        lines[i][j] = int(lines[i][j])

# Sum of extrapolated values in original sequences
sumForwardExtrapolatedValues = 0
sumBackExtrapolatedValues = 0
for i in range(len(lines)): # Go through every line of input
    # Add the last digit of the new sequence to the sum of extrapolated values
    extrapolatedSequence = findNextValue(lines[i])
    sumForwardExtrapolatedValues += extrapolatedSequence[-1]
    backExtrapolatedSequence = findPrevValue(lines[i])
    sumBackExtrapolatedValues += backExtrapolatedSequence[0]

print(f"sum of forward extrapolated values: {sumForwardExtrapolatedValues}")
print(f"sum of backward extrapolated values: {sumBackExtrapolatedValues}")
