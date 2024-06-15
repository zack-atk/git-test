# Functions

# function_name('argument')

# print('a value')
# input('ask for a value')

# print(input('Provide a value: '))

# --------------------------------

# Methods -> functions of datatypes

# lil_value = 'lil_value'
# big_value = 'BIG_VALUE'
# print(lil_value.upper())
# print(big_value.lower())
# print(lil_value.replace('lil', 'little'))

# # new functions
# print(abs(-1)) # absolute value
# print(max(10,5)) # maximum value
# print(min(0,1)) # minimum value
# print(len('test')) # string length

# Pythagorean Theorem Calculator:
leg_a = int(input('Enter the length of leg \'a\': '))
leg_b = int(input('Enter the length of leg \'b\': '))
hypotenuse = (leg_a ** 2 + leg_b ** 2) ** (1/2)
print('The length of the hypotenuse is:', round(hypotenuse,2))
