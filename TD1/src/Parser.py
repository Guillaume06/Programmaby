#!/usr/bin/python

import sys
import os


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
                    print(line)
            # Handle exception during reading
            except:
                print("Error occurred during file reading")
    else:
        print("Error : file ", filename, "not found")


# Main
print("Number of arguments:", len(sys.argv))
print("Argument List:", str(sys.argv))

parseByLine(sys.argv[1])
