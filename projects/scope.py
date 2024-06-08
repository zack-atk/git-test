# DEFINING VARIABLE SCOPE
# ---------------------------
# When defining a variable, location can affect the output when using functions. Variables defined within functions are local to that function, while global variables defined outside of a funtion can be called anywhere.
# ---------------------------
my_name = 'Global' # GLOBAL VARIABLE

def print_name():
    my_name = 'Local' # LOCAL VARIABLE
    print("Inside the function:", my_name)

print_name()
print('Outside the function:', my_name)
