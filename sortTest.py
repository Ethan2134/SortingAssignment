import os
import argparse
parser = argparse.ArgumentParser()
#add a true/false that allows for the viewing of mismatch error
parser.add_argument("-v", action='store_true', help="Shows the lines that are mismatched during tests, assuming there are an equal number of names")
command = parser.parse_args()
# TEST CASE 1
os.system("python3 sortme.py -r")
print("Test Case 1: Checking the reversed sort...")
with open('Sorted Reverse Text.txt') as f1, open('Output Reverse Text.txt') as f2:
    expected = f1.readlines()
    actual = f2.readlines()
    if expected == actual:
        print("The files match. Test case passed")
    else:
        print("The files DO NOT match. Test case failed")
        if command.v:
            if len(expected) == len(actual):
                count = 0
                for name in expected:
                    if(name != actual[count]):
                        print("Error at line ", count+1, ". Expected: ", name, ". Actual: ", actual[count])
                    count += 1
            else:
                print("The files do not have an equal number of names! Expected: ", len(expected), ". Actual: ", len(actual))

#TEST CASE 2
os.system("python3 sortme.py")
print("Test Case 2: Checking the normal sort...")
with open('Sorted Text.txt') as f1, open('Output Text.txt') as f2:
    expected = f1.readlines()
    actual = f2.readlines()
    if expected == actual:
        print("The files match. Test case passed")
    else:
        print("The files DO NOT match. Test case failed")
        if command.v:
            if len(expected) == len(actual):
                count = 0
                for name in expected:
                    if(name != actual[count]):
                        print("Error at line ", count+1, ". Expected: ", name, ". Actual: ", actual[count])
                    count += 1
            else:
                print("The files do not have an equal number of names! Expected: ", len(expected), ". Actual: ", len(actual))
            