# FILTERS

# Example 1: Filters
# ----------------------------------

grades = ['A','B', 'F','C','F', 'A']

def remove_fails(grade):
    return grade != 'F'

print('')
print('Using a Filter:')
print(list(filter(remove_fails, grades)))
print('')

# ---------------------------------


# Example 2: 'For' Loop
# --------------------------------

filtered_grades = []
for grade in grades:
    if grade != 'F':
        filtered_grades.append(grade)
        
print('Using a \'for\' loop:')        
print(filtered_grades)
print('')

# --------------------------------


# Example 3: Comprehension Method
#---------------------------------

print('Using the comprehension method:')
print( [ grade for grade in grades if grade != 'F'] )
print('')

# END