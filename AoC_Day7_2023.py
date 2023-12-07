# AoC_Day7_2023.py


# Auxiliary function to findHandStrength to discern two pairs from one pairs
def handIsTwoPair(listOfOccurrences):
    numOfOnes = 0
    
    # Count number of 1's occurrences
    for i in range(len(listOfOccurrences)):
        if listOfOccurrences[i] == 1:
            numOfOnes += 1

    # If more than 1 instance of 1, not a two-pair
    if numOfOnes > 1:
        return False
    else:
        return True

# Auxiliary function to findHandStrength to account for the effect of the
# joker on the result. Returns a modified hand-type strength value
def strengthWithJokerEffect(strength, cardOccurrences):
    if cardOccurrences.get('J') == 1: # One joker
        # Mappings: JABCD -> AABCD, JAABC -> AAABC, JAABB -> AAABB,
        # JAAAB -> AAAAB, JAAAA -> AAAAA
        # Cannot have fullhouse or 5ofakind with 1 joker
        strengthMapping = {0: 1, 1: 3, 2: 3.5, 3: 4, 4: 5}
        return strengthMapping[strength]
    elif cardOccurrences.get('J') == 2: # Two jokers
        # Mappings: JJABC -> AAABC, JJAAB -> AAAAB, JJAAA -> AAAAA
        # Cannot have highcard, threeofakind (would be fullhouse), 4ofakind, or
        # 5ofakind with 2 jokers
        strengthMapping = {1: 3, 2: 4, 3.5: 5}
        return strengthMapping[strength]
    elif cardOccurrences.get('J') == 3: # Three jokers
        # Mappings: ABJJJ -> ABAAA, AAJJJ -> AAAAA
        # Cannot have highcard, pair, 2pair, 4ofakind, or 5ofakind with 3 jokers
        strengthMapping = {3: 4, 3.5: 5} 
        return strengthMapping[strength]
    elif cardOccurrences.get('J') == 4: # Four jokers
        return 5 # Has to become 5 of a kind
    else: # 5 jokers
        return 5 # 5 of a kind
    
# Function to determine the strength of a hand as a numerical value
def findHandStrength(hand):
    # A hand can be highcard, onepair, twopair, threeofakind, fullhouse,
    # four of a kind, or five of a kind. We'll assign these values 0-6
    # and then give a decimal based on the cards to sort by better cards
    
    # highcard = 0, pair = 1, twopair = 2, 3ofakind = 3, fullhouse = 3.5,
    # 4ofakind = 4, 5ofakind = 5
    
    strength = 0 # Initially set strength to 0

    # Determine how many cards are in common in a hand by indexing the number
    # of a given card in a dictionary
    cardOccurrences = {}
    for i in range(5): # Go through every card
        # If the index of the ith card doesnt exist, create it and set it to 0
        if cardOccurrences.get(hand[i], 0) == 0:
            cardOccurrences[hand[i]] = 0
        cardOccurrences[hand[i]] += 1 # Add 1 to instances of this card

    # Turn this dictionary to a list so it can be indexed numerically
    listOfOccurrences = []
    for key in cardOccurrences.keys():
        listOfOccurrences.append(cardOccurrences[key])

    # Find the strongest hand
    if 5 in listOfOccurrences: # Five of a kind
        strength += 5
    elif 4 in listOfOccurrences: # Four of a kind
        strength += 4
    elif 3 in listOfOccurrences and 2 in listOfOccurrences: # Full house
        strength += 3.5
    elif 3 in listOfOccurrences: # Three of a kind
        strength += 3
    # If its 2 pair, the list of occurrences must be [1,2,2] or [2,1,2] or
    # [2,2,1]. If we find 1 twice or more then it cant be 2 pair
    elif (handIsTwoPair(listOfOccurrences)): # See function handIsTwoPair
        strength += 2
    elif 2 in listOfOccurrences: # Pair
        strength += 1
    # else: High card, strength remains 0
        
    # To determine what the first higher card in the hand is, assign each card
    # a numerical value and add this value divided by 100^(its position in hand)
    # to its strength. This creates a numerical list of the cards in order
    # in the decimal trail of the number's strength. This preserves the property
    # that a higher strength means a better hand
    decimalTrail = 0
    cardValueDict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                 '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


    # For part 2 if there's a joker in this hand, feed it through an auxiliary
    # function to find the new type strength and modify the cardValueDict to
    # reflect the joker's new value. To solve part 1 just comment out this if
    # block
    if cardOccurrences.get('J', 0) >= 1:
        strength = strengthWithJokerEffect(strength, cardOccurrences)
        # Replace the value of a joker in decimal trail calculations with a 1
        cardValueDict['J'] = 1
        

    # Create the decimal trail for the card's strength as described earlier
    for i in range(1, 5+1):
        decimalTrail += cardValueDict[hand[i-1]]/(100**i)

    # Add the decimal trail to the strength
    strength += decimalTrail

    return strength

# --Main program below--

with open("AoC2023Inputs/Day7Input.txt") as inputFile:
    lines = inputFile.readlines()

# Get the hands and biddings from input into lists
hands = []
bids = []

# Split the lines into split lists: hand and bid
for i in range(len(lines)):
    lines[i] = lines[i].split()

# Go through every line to put hands and bids into lists
for i in range(len(lines)):
    hands.append(lines[i][0])
    bids.append(lines[i][1])

# Create a dictionary for hands to their bids, and hands to their strength
handsToBids = {}
handsToStrengths = {}

# Go through every hand and assign it its corresponding bid and strength
for i in range(len(hands)):
    handsToBids[hands[i]] = bids[i]
    handsToStrengths[hands[i]] = findHandStrength(hands[i])

# Since we want to be able to sort the hands by their strength and then find
# the hand it came from to find its bid, we want a dictionary from strengths to
# bids
strengthsToBids = {}
# Go through every hand
for i in range(len(hands)):
    # Associate the strength with the bid
    strengthsToBids[handsToStrengths[hands[i]]] = handsToBids[hands[i]]


# Create a list of strengths to sort
strengths = []
for i in range(len(hands)):
    strengths.append(handsToStrengths[hands[i]])

# Have Python automatically sort the strengths low to high
strengths.sort()

winnings = 0 # Variable to track winnings
for i in range(len(strengths)):
    # Add the bid times the rank (index+1) to the winnings
    winnings += (int(strengthsToBids[strengths[i]]) * (i+1))

print(f"Total Winnings: {winnings}")
