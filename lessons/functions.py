## FUNCTIONS

# In order to use a function, you must first define it 
# Default parameters can be assigned in the function
#-------------------------------------------------------
# def greet(name = 'User', time = 'day'):
#     print(f'Good {time} {name}, hope you are well')

# greet()
#--------------------------------------------------------

# ...or, you can get interactive..
#--------------------------------------------------------
def greet(name = 'User', time = 'day'):
    print(f'Good {time} {name}, hope you are well')

name = input('enter your name: ')
time = input('enter the time of day: ')

greet(name, time)
