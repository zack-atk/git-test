# LAMBDAS


nums = [1,2,3,4,5,6]

def square(n):
    return n*n

# Example 1 - Using a 'map' function:
print('Example 1 - Using a \'map\' fumction:')
print(list(map(square,nums)))
print('---')

# Example 2 - Using a Lambda:
print('Example 2 - Using a lambda:')
print(list(map(lambda n: n*n,nums)))