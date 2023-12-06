# AoC_Day6_2023.py

import math

import time
start_time = time.time()

with open("AoC2023Inputs/Day6Input.txt") as inputFile:
    lines = inputFile.readlines()

# Set times to the first line
times = lines[0].split()
times.remove("Time:")

# Set distances to the second line
distances = lines[1].split()
distances.remove("Distance:")

# Convert all the stuff in the lists to int
for i in range(len(times)):
    times[i] = int(times[i])
    distances[i] = int(distances[i])

# List of 0's for ways to win for each race
waysToWin = [0] * len(times)

raceDistance = 0

# Loop per race, and calculate the distance per time possibility
for i in range(len(times)):
    for buttonTime in range(1, times[i]):
        raceDistance = buttonTime * (times[i] - buttonTime)
        if raceDistance > distances[i]:
            waysToWin[i] += 1

# Multiply all the ways to win
totalWaysToWin = 1
for i in range(len(waysToWin)):
    totalWaysToWin *= waysToWin[i]

print(f"Part 1 ways to win: {totalWaysToWin}")


# ---Part 2 below---

# To solve this, we can find the roots of the quadratic equation formed by the
# graph of distance travelled as a function of time the button is held
# Let y = boat distance, x = button time, t = total time, r = record distance
# y = x(t-x) = -x^2+tx. We want -x^2+tx>r -> -x^2+tx-r > 0
# This has 2 roots a and b, any integer values of x inbetween a and b are ways
# to win the race, so find how many of those there are

# Find t and r
t = ""
r = ""
for i in range(len(times)):
    t += str(times[i])
    r += str(distances[i])

# Convert t and r to int after processing them as strings
t = int(t)
r = int(r)

# x1 is the lower root, x2 is the higher root
x1 = math.ceil((-t + math.sqrt((t**2)-(4*(-1)*(-r))))/(-2))
x2 = math.floor((-t - math.sqrt((t**2)-(4*(-1)*(-r))))/(-2))
waysToWin2 = x2 - x1 + 1
print(f"Part 2 ways to win: {waysToWin2}")

print(f"Program executed in %s seconds" % (time.time() - start_time))
