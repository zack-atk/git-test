# DECORATORS

def cough_dec(func): # We define the 'cough_dec' decorator here
    
    def func_wrapper(): # Here, we create the wrapping function for our decorator
        
        print('*cough*')
        func()           # Here, we print '*cough*' on either side of decorated function
        print('*cough*')
        
    return func_wrapper  # ...and finally call the function

@cough_dec #Here, we call the decorator

def question(): # ...and make our question function to wrap with our decorator.
    print('Are you offering any discounts on that?')
    
@cough_dec #Here, we call the decorator again on our answer function.    
def answer():
    print('On the one dollar soda...? No.')

# Finally, we call the question function, which is now being decorated by @cough_dec    
question()

# ...and do the same with the answer function:
answer()