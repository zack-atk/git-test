# # **Uncomment each block individually for walkthrough**

# # -------------------------------

# #         If Statements

# # Feel free to change the variable to adjust the result
# var = 1

# # "If this is true, do this:

# if var > 4:
#     print('if true result')

# # If not, and if this is true, do this: 

# elif var > 1:
#     print('elif result')

# # Otherwise, do this: 

# else:
#     print('false result')

# # ALWAYS do this:

# print('always result')

# # -----------------------------

# #          While Loop

# counter = 1
# while counter <= 10:
#     print(counter)
    
# # complicating the while loop with an if statement:

#     if counter == 5:
#         print('Halfway there!')

# # without adjusting the variable after each cycle, the loop would run infinitely.

#     counter += 1
    
# print('end of while loop')

# # ------------------------------

# #         For Loop

# test_list =[1,2,3,4,5]
# test_dict = {1:'one', 2:'two', 3:'three'}

# # Simple:
# for x in test_list:
#     print(x)
    
# # Calling out specific part of a dictionary with .keys(), .values(), & .items()
# for x in test_dict.items():
#     print(x)
    
# # If you know the number of items in a container, you can assign them variables and call them directly in the for loop like so:
# for k,v in test_dict.items():
#     print(v)

# # -------------------------------

# Exercise:
# Create a list = (1,2,3,4,5) and run code for every item.

my_list = (1,2,3,4,5)
n = 0
num_ends = 3

for x in my_list:
    if x == 5:
        print('MAX')
    else:
        print('Run Again')

while n < num_ends:
    print('END')
    n += 1

