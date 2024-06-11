# WRITING TO FILES

# We can use a .write() method to write to a file:

# First, we open the file and specify write access:
with open('write.txt', 'w') as write_file: # The 'w' is the write access command
    write_file.write('We love writing with Python')
    
# Next, we can append details to the file, otherwise the file will be overwritten:    
with open('write.txt', 'a') as write_file: # The 'a' is the append access command  
    write_file.write('\nso much that we dream about it!')
    
# Let's say we have a list we want to write to a file like this one:
quotes = [
    '\n"I can resist everything except temptation."',
    '\n"We are all in the gutter, but some of us are looking at the stars."',
    '\n"Always forgive your enemies - nothing annoys the so much."'
]

# We can use .writelines() to write from a list:
with open('write.txt', 'a') as write_file:
    write_file.writelines(quotes)