#Author: Ethan Raby
#Will sort a list of names by length of name, and alphabetically.
#reads the file and removes any white space
def file_read(fname):
    content_array = []
    with open(fname) as f:
        for line in f:
            line = line.strip()
            line = line.replace(' ', '')
            content_array.append(line)
    return content_array
    
array = file_read('Sort Me.txt')
#sort by alphabet
array.sort()
#sort by length
array = sorted(array,key=len)
for name in array:
    print(name)
#wait for user to end program
input("Press enter to exit")