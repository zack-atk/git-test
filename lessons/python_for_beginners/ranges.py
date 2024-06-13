# RANGES
# -------------------------------------
# items - [1,2,3,4,5]

# for item in items:
#     do something
# -------------------------------------
# Example One:

# for n in range(3,10):
#     print(n)
# -------------------------------------
# Example Two:

# for n in range(0,20,4):
#     print(n)
# -------------------------------------
# For examples three and four, use the following line:
burgers = ['beef', 'chicken', 'turkey','veggie','double']
# -------------------------------------
# Example Three:


# for n in range(len(burgers)):
#     print(n,burgers[n])
# -------------------------------------
# Example Four:

for n in range(len(burgers) - 1, -1, -1):
    print(n,burgers[n])
