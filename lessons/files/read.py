#   READING FILES

#   Here, we save the open function opening the ipsum file to a variable, 'ipsum_file':
ipsum_file = open('files/ipsum.txt')

def separator(func): 
    
    def func_wrapper():
        
        print ('-'*40) 
        func()
        print ('-'*40)         
        
    return func_wrapper

print ('-'*40) 
print('Using a for loop:')
@separator
def ex1():
    # Here, we run the file through a 'for' loop, printing each line to the console:
    for line in ipsum_file:
        print(line.rstrip()) # The .rstrip() method trims the space after each line.
        
ex1() 
# ------------------------------------

# At this point, we're at the end of the file and need to return to the beginning, so we use the .seek() method:
print('Using .readlines():')
@separator
def ex2():
    ipsum_file.seek(0) #seeking the first character, indexed at zero
    # Here, we use the .readlines() method to read the contents of the file, and save each individual line as a string in a list of lines.
    lines = ipsum_file.readlines()
    print(lines)
    
ex2()
# ------------------------------------

#Again, we'll need to seek to return to the beginning of the file, but this time, lets play with seek and the .read() method:
print('Using .read()')
@separator
def ex3():
    # Here, we'll seek back to the 50th character and read ahead 100 characters:
    ipsum_file.seek(50)
    file_text = ipsum_file.read(100)
    print(file_text)
    
ex3()
# ------------------------------------

# Finally, we close the file!
ipsum_file.close()

#Another way we can do this is with the following method.
print('Filtering and using .readlines()')

#We're taking this a step further and filtering out lines from the source file starting with '>'.
def sequence_filter(line):
    return '>' not in line

# Here, we open the dna_sequence.txt file, run .readlines() on it and then print a filtered list from that data.
@separator
def ex4():
    with open('files/dna_sequence.txt') as dna_file:
        lines = dna_file.readlines()
        print(list(filter(sequence_filter, lines)))
        
ex4()    