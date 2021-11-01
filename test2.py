import os
# TEST CASE 1
os.system("sortme.py -r")
print("Test Case 1: Checking the reversed sort...")
with open('Sorted Reverse Text.txt') as f1, open('Output Reverse Text.txt') as f2:
    expected = f1.readlines()
    actual = f2.readlines()
    assert expected == actual

#TEST CASE 2
os.system("sortme.py")
print("Test Case 2: Checking the normal sort...")
with open('Sorted Text.txt') as f1, open('Output Text.txt') as f2:
    expected = f1.readlines()
    actual = f2.readlines()
    assert expected == actual
print("Test cases passed.")