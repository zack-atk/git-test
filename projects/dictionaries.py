# We'll make a dictionary of rangers via user input

# Defining a function to introduce the rangers:
# --------------------------------------------
# def ranger_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f'{key}, {val.lower()} ranger!')
# --------------------------------------------
# We can, altenatively, use sets and sorting:
# --------------------------------------------
def color_count(dictionary):
    colors = list(dictionary.values())
    for color in set(colors):
        num = colors.count(color)
        print(f'There is(are) {num} {color} ranger(s)')

# Defining the dictionary
ranger_suits = {}

# This loop will enable the input prompts
while True:
    ranger_name = input('enter a ranger name: ')
    ranger_color = input('enter a ranger suit color: ')
    # This assigns the key/value pair:
    ranger_suits[ranger_name] = ranger_color.lower() 
    
# Prompt for adding multiple rangers:
    multiple = input('add another? (y/n): ')
    if multiple == 'y':
# The keyword 'continue' will bring us back the loop start
        continue
    else:
        break
# Finally, we call the ranger_intro function:
# ------------------------------------------
# ranger_intro(ranger_suits)
# ------------------------------------------
# Or, the count function:
color_count(ranger_suits)
