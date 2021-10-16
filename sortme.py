#Author: Ethan Raby
#Will sort a list of names by length of name, and alphabetically. Can also sort the list
#in reverse order by length of name and alphabetically.


import argparse

parser = argparse.ArgumentParser()
#add a true/false flag that decides to reverse or not
parser.add_argument("-r", action='store_true', help="Sorts in descending length in reverse alphabetic order")
#reads the file and removes any white space
def file_read(fname):
    content_array = []
    with open(fname) as f:
        for line in f:
            line = line.strip()
            line = line.replace(' ', '')
            content_array.append(line)
    return content_array
command = parser.parse_args()
array = file_read('Sort Me.txt')

if command.r:
    #sort in reverse alphabetically
    array.sort(reverse=True)
    #sort in reverse length
    array.sort(key=len, reverse=True)
else:
#    #sort by alphabet
    array.sort()
#    #sort by length
    array = sorted(array,key=len)
for name in array:
    print(name)
#wait for user to end program
input("Press enter to exit")