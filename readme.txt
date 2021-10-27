Sorting Script

This script will sort a list of names by length in ascending order, and then sort alphabetically and 
add the sorted names to a file. To sort the names in descending order by length, add the -r argument
when running the script from the command line. This script will only sort the one text document, 'Sort Me.txt'
according to the assignment. The normal sort will be added to a text file called 'Output Text.txt', and the
reverse sort will be added to 'Output Reverse Text.txt'. Test cases have been added as well, and will output true
or false, depending on if the actual output matches the expected output. The expected output for a normal sort is 
in a text file called 'Sorted Text.txt', and the expected output for a reverse sort is in 'Sorted Reverse Text.txt'.
After each sort, the outputs will be overwritten, and any information in the file will be lost. By adding a new name
to 'Sort Me.txt', the test cases will fail unless the expected output files are updated as well, and vice versa.


To run the script, navigate to the directory that contains the script from the command line. Run the following command
in Linux: `python3 sortme.py` to sort the names. To sort the names in reverse, type the command: `python3 sortme.py -r`.
To run the tests, navigate to the directory that contains the script from the command line. Run the following command
in Linux: `python3 sortTest.py` to run the test cases. To see the type of error in the file mismatch, run the command
'python3 sortTest.py -v. 


