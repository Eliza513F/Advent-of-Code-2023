# AoC_Day5_2023.py

# Track the program's time to run
import time
start_time = time.time()

with open('AoC2023Inputs/Day5Input.txt') as inputFile:
    lines = inputFile.readlines()

# Create a list of seeds
seeds = lines[0].split()
# Get rid of the starting "seeds:"
seeds.remove("seeds:") 
# Convert all these seed strings to ints for convenience
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

# Create a list of lowerBound, upperBound, and the offset
seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []


# Start at index 3, where the seed-to-soil mapping begins
currentLine = 3
# loop until reaching the end of this type mapping (a newLine character)
while lines[currentLine] != "\n":
    # Create a list of the numbers in the line of input
    mapInfo = lines[currentLine].split()
    
    destination = int(mapInfo[0])
    lowerBound = int(mapInfo[1])
    mapRange = int(mapInfo[2])
    offset = destination - lowerBound # The mapping is just adding this offset
    upperBound = lowerBound + (mapRange - 1) # Upper bound of this mapping

    # List of mappings from lowerBound to upperBound with a certain offset
    seedToSoil.append([lowerBound, upperBound, offset])
        
    # Move down to the next line
    currentLine += 1


# Continue the above thing of going through and mapping all the things
currentLine += 2
# loop until reaching the end of this type mapping (a newLine character)
while lines[currentLine] != "\n":
    # Create a list of the numbers in the line of input
    mapInfo = lines[currentLine].split()
    
    destination = int(mapInfo[0])
    lowerBound = int(mapInfo[1])
    mapRange = int(mapInfo[2])
    offset = destination - lowerBound # The mapping is just adding this offset
    upperBound = lowerBound + (mapRange - 1) # Upper bound of this mapping

    # List of mappings from lowerBound to upperBound with a certain offset
    soilToFertilizer.append([lowerBound, upperBound, offset])
        
    # Move down to the next line
    currentLine += 1


currentLine += 2
# loop until reaching the end of this type mapping (a newLine character)
while lines[currentLine] != "\n":
    # Create a list of the numbers in the line of input
    mapInfo = lines[currentLine].split()
    
    destination = int(mapInfo[0])
    lowerBound = int(mapInfo[1])
    mapRange = int(mapInfo[2])
    offset = destination - lowerBound # The mapping is just adding this offset
    upperBound = lowerBound + (mapRange - 1) # Upper bound of this mapping

    # List of mappings from lowerBound to upperBound with a certain offset
    fertilizerToWater.append([lowerBound, upperBound, offset])
        
    # Move down to the next line
    currentLine += 1


currentLine += 2
# loop until reaching the end of this type mapping (a newLine character)
while lines[currentLine] != "\n":
    # Create a list of the numbers in the line of input
    mapInfo = lines[currentLine].split()
    
    destination = int(mapInfo[0])
    lowerBound = int(mapInfo[1])
    mapRange = int(mapInfo[2])
    offset = destination - lowerBound # The mapping is just adding this offset
    upperBound = lowerBound + (mapRange - 1) # Upper bound of this mapping

    # List of mappings from lowerBound to upperBound with a certain offset
    waterToLight.append([lowerBound, upperBound, offset])
        
    # Move down to the next line
    currentLine += 1


currentLine += 2
# loop until reaching the end of this type mapping (a newLine character)
while lines[currentLine] != "\n":
    # Create a list of the numbers in the line of input
    mapInfo = lines[currentLine].split()
    
    destination = int(mapInfo[0])
    lowerBound = int(mapInfo[1])
    mapRange = int(mapInfo[2])
    offset = destination - lowerBound # The mapping is just adding this offset
    upperBound = lowerBound + (mapRange - 1) # Upper bound of this mapping

    # List of mappings from lowerBound to upperBound with a certain offset
    lightToTemperature.append([lowerBound, upperBound, offset])
        
    # Move down to the next line
    currentLine += 1


currentLine += 2
# loop until reaching the end of this type mapping (a newLine character)
while lines[currentLine] != "\n":
    # Create a list of the numbers in the line of input
    mapInfo = lines[currentLine].split()
    
    destination = int(mapInfo[0])
    lowerBound = int(mapInfo[1])
    mapRange = int(mapInfo[2])
    offset = destination - lowerBound # The mapping is just adding this offset
    upperBound = lowerBound + (mapRange - 1) # Upper bound of this mapping

    # List of mappings from lowerBound to upperBound with a certain offset
    temperatureToHumidity.append([lowerBound, upperBound, offset])
        
    # Move down to the next line
    currentLine += 1


currentLine += 2
# Note: 2 lines of blank space were added to the input file, otherwise this
# creates an error. I am lazy.
while lines[currentLine] != "\n":
    # Create a list of the numbers in the line of input
    mapInfo = lines[currentLine].split()
    
    destination = int(mapInfo[0])
    lowerBound = int(mapInfo[1])
    mapRange = int(mapInfo[2])
    offset = destination - lowerBound # The mapping is just adding this offset
    upperBound = lowerBound + (mapRange - 1) # Upper bound of this mapping

    # List of mappings from lowerBound to upperBound with a certain offset
    humidityToLocation.append([lowerBound, upperBound, offset])
        
    # Move down to the next line
    currentLine += 1


# Put all the seeds through the appropriate mappings. If the mapping for a
# number hasn't been made, it'll be the same number, so nothing is done

for i in range(len(seeds)): # Iterate over every seed
    for j in range(len(seedToSoil)): # Iterate over every list in seedToSoil
        if seeds[i] >= seedToSoil[j][0] and seeds[i] <= seedToSoil[j][1]:
            seeds[i] += seedToSoil[j][2] # Modify it by the mapping offset
            break # We are done with the current seed

# The same code as above is repeated for all mappings, just with the respective
# mapping lists

for i in range(len(seeds)):
    for j in range(len(soilToFertilizer)):
        if (seeds[i] >= soilToFertilizer[j][0] and
        seeds[i] <= soilToFertilizer[j][1]):
            seeds[i] += soilToFertilizer[j][2]
            break

   
for i in range(len(seeds)):
    for j in range(len(fertilizerToWater)):
        if (seeds[i] >= fertilizerToWater[j][0] and
        seeds[i] <= fertilizerToWater[j][1]):
            seeds[i] += fertilizerToWater[j][2]
            break

for i in range(len(seeds)):
    for j in range(len(waterToLight)):
        if (seeds[i] >= waterToLight[j][0] and seeds[i] <= waterToLight[j][1]):
            seeds[i] += waterToLight[j][2]
            break

for i in range(len(seeds)):
    for j in range(len(lightToTemperature)):
        if (seeds[i] >= lightToTemperature[j][0] and
        seeds[i] <= lightToTemperature[j][1]):
            seeds[i] += lightToTemperature[j][2]
            break

for i in range(len(seeds)):
    for j in range(len(temperatureToHumidity)):
        if (seeds[i] >= temperatureToHumidity[j][0] and
        seeds[i] <= temperatureToHumidity[j][1]):
            seeds[i] += temperatureToHumidity[j][2]
            break

for i in range(len(seeds)):
    for j in range(len(humidityToLocation)):
        if (seeds[i] >= humidityToLocation[j][0] and
        seeds[i] <= humidityToLocation[j][1]):
            seeds[i] += humidityToLocation[j][2]
            break

# Find the smallest location in the seeds' final mapping
smallestLocation = seeds[0]
for i in range(1, len(seeds)):
    if seeds[i] < smallestLocation:
        smallestLocation = seeds[i]

print(f"Part 1: Smallest location: {smallestLocation}")


# Part 2 begins below. WARNING: THIS TAKES A MONSTER OF A COMPUTER TO RUN
# It took about 6hr45m of raw processing, with peak RAM usage ~25GB
# on my day 5 input
print("Starting Part 2...")
      
# Function to find the lowest location in a list of seed values, given the
# mappings
def findLowestLocation(allSeeds, seedToSoil, soilToFertilizer,
                       fertilizerToWater, waterToLight, lightToTemperature,
                       temperatureToHumidity, humidityToLocation):
    
    for i in range(len(allSeeds)): # Iterate over every seed
        for j in range(len(seedToSoil)): # Iterate over every list in seedToSoil
            if (allSeeds[i] >= seedToSoil[j][0] and
            allSeeds[i] <= seedToSoil[j][1]):
                allSeeds[i] += seedToSoil[j][2] # Modify it by mapping offset
                break # We are done with the current seed

    # The same code as above is repeated for all mappings, just with the
    # respective mapping lists
    print("Subchunk mapping from seeds to soil complete")
    for i in range(len(allSeeds)):
        for j in range(len(soilToFertilizer)):
            if (allSeeds[i] >= soilToFertilizer[j][0] and
            allSeeds[i] <= soilToFertilizer[j][1]):
                allSeeds[i] += soilToFertilizer[j][2]
                break

    print("Subchunk mapping from soil to fertilizer complete")
    for i in range(len(allSeeds)):
        for j in range(len(fertilizerToWater)):
            if (allSeeds[i] >= fertilizerToWater[j][0] and
            allSeeds[i] <= fertilizerToWater[j][1]):
                allSeeds[i] += fertilizerToWater[j][2]
                break

    print("Subchunk mapping from fertilizer to water complete")
    #print(allSeeds)
    for i in range(len(allSeeds)):
        for j in range(len(waterToLight)):
            if (allSeeds[i] >= waterToLight[j][0] and
                allSeeds[i] <= waterToLight[j][1]):
                allSeeds[i] += waterToLight[j][2]
                break

    print("Subchunk mapping from water to light complete")
    for i in range(len(allSeeds)):
        for j in range(len(lightToTemperature)):
            if (allSeeds[i] >= lightToTemperature[j][0] and
            allSeeds[i] <= lightToTemperature[j][1]):
                allSeeds[i] += lightToTemperature[j][2]
                break

    print("Subchunk mapping from light to temperature complete")
    for i in range(len(allSeeds)):
        for j in range(len(temperatureToHumidity)):
            if (allSeeds[i] >= temperatureToHumidity[j][0] and
            allSeeds[i] <= temperatureToHumidity[j][1]):
                allSeeds[i] += temperatureToHumidity[j][2]
                break

    print("Subchunk mapping from temperature to humidity complete")
    for i in range(len(allSeeds)):
        for j in range(len(humidityToLocation)):
            if (allSeeds[i] >= humidityToLocation[j][0] and
            allSeeds[i] <= humidityToLocation[j][1]):
                allSeeds[i] += humidityToLocation[j][2]
                break

    print("Subchunk mapping from humidity to location complete")
    lowestLocation = allSeeds[0]
    # Find the lowest location in this list
    for i in range(1, len(allSeeds)):
        if allSeeds[i] < lowestLocation:
            lowestLocation = allSeeds[i]

    print(f"Lowest Location in batch: {lowestLocation}")
    return lowestLocation
# ---End of the above monstrosity---
    

seedStarter = lines[0].split()
seedStarter.remove("seeds:")
# convert all the seedStarters to ints
for i in range(len(seedStarter)):
    seedStarter[i] = int(seedStarter[i])

print("Converted seedStarters from str to int")

allSeeds = []
lowestLocations = []
for i in range(len(seedStarter)):
    if i % 2 == 0: # If this is the 0th, 2nd, etc index, add the seed number
        allSeeds.append(seedStarter[i])
    else: # this number describes a range of seeds after the last one
        starter = seedStarter[i-1]
        for k in range(starter+1, starter+seedStarter[i]):
            allSeeds.append(k) # Add k to the list of all seeds
        # At this point, a whole chunk is now in allSeeds, execute the main
        # part of the program on this chunk, and put its lowest location in
        # the list of lowestLocations
        print(f"Batch of {seedStarter[i]} initialized")
        lowestLocations.append(findLowestLocation(allSeeds, seedToSoil,
                                                  soilToFertilizer,
                                                  fertilizerToWater,
                                                  waterToLight,
                                                  lightToTemperature,
                                                  temperatureToHumidity,
                                                  humidityToLocation))
        print(f"Batch of {seedStarter[i]} mapped!")
        print(f"The program has so far taken: ", end = "")
        print("%s seconds" % (time.time() - start_time))
        # Empty the allSeeds to free up RAM for the next batch
        allSeeds = []
        
# After we have all the lowestLocations, find the lowest of them
print(f"List of lowest locations complete")
print(lowestLocations)
lowestLocation = lowestLocations[0]
for i in range(1, len(lowestLocations)):
    if lowestLocations[i] < lowestLocation:
        lowestLocation = lowestLocations[i]

print(f"Lowest location: {lowestLocation}")
