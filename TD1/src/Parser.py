#!/usr/bin/python

import sys
import os

# Variable initialization
departureClosest = ""
arrivalClosest = ""
closestDistance = 9999999999999.9

departureFarthest = ""
arrivalFarthest = ""
farthestDistance = 0.0


# Calling this function on a line will call all the updating functions
def updateSearch(line):
    updateClosest(line)
    updateFarthest(line)


# Handle the update of the closest distance
def updateClosest(line):
    # With global, it tells that the variable aren't local
    global departureClosest
    global arrivalClosest
    global closestDistance

    # Create a board of thew line, by splitting the sentence on the " "
    lineTab = line.split(" ")

    # Test if the result have the expected size
    if len(lineTab) < 3:
        print("Error during line cast : wrong line format")
        return

    # Cast distance to float and error handling
    try:
        distance = float(lineTab[2])
    except:
        print("Error during the distance cast to double")
        return

    # Test and update of the closest distance
    if distance < float(closestDistance):
        departureClosest = lineTab[0]
        arrivalClosest = lineTab[1]
        closestDistance = lineTab[2]


# Handle the update of the farthest distance
def updateFarthest(line):
    # With global, it tells that the variable aren't local
    global departureFarthest
    global arrivalFarthest
    global farthestDistance

    # Create a board of thew line, by splitting the sentence on the " "
    lineTab = line.split(" ")

    # Test if the result have the expected size
    if len(lineTab) < 3:
        print("Error during line cast : wrong line format")
        return

    # Cast distance to float and error handling
    try:
        distance = float(lineTab[2])
    except:
        print("Error during the distance cast to double")
        return

    # Test and update of the farthest distance
    if distance > float(farthestDistance):
        departureFarthest = lineTab[0]
        arrivalFarthest = lineTab[1]
        farthestDistance = lineTab[2]


# Parse the file line by line and call the corresponding function on each line
def parseByLine(filename):

    # Test the existence of the file
    if os.path.exists(filename):

        # Open file
        with open(filename, 'r') as f:

            # Try to read line by line
            try:

                # Read line by line
                for line in f:

                    # Remove '\n'
                    line = line.strip()
                    updateSearch(line)

            # Handle exception during reading
            except:
                print("Error occurred during file reading")
    else:
        print("Error : file ", filename, "not found")


# Main
print("Number of arguments:", len(sys.argv))
print("Argument List:", str(sys.argv))

# Verify the number of arguments
if len(sys.argv) < 2:
    print("Error : 1 argument needed")
    exit(1)

# Calling function
parseByLine(sys.argv[1])

# Print results
print("Closest distance : ", departureClosest, " to ", arrivalClosest, " (", closestDistance, "km)")
print("Farthest distance : ", departureFarthest, " to ", arrivalFarthest, " (", farthestDistance, "km)")
