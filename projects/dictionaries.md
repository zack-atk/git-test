# Dictionaries

A dictionary is a data type consisting of key/value pairs

---
### Type 'python' in your terminal
The following can be done in your python shell.

This is a dictionary:
```
>>> ranger_suits = {"Zack": "black", "Tommy": "white"}
>>> ranger_suits
{"Zack": "black", "Tommy": "white"}
```
*or*
```
>>> ranger = dict(name="Zack", symbol="mastodon", color="black")
>>> ranger
{'name': 'Zack', 'symbol': 'mastodon', 'color': 'black'}
```
You can use the keyword 'in' to determine if a key value exists in a dictionary:
```
>>> 'Billy' in ranger_suits
False

>>> 'Zack' in ranger
True
```
You can see a list of keys for a dectionary by using the '.keys()' method
```
>>> ranger_suits.keys()
dict_keys(['Zack', 'Tommy'])
```
The 'list()' method can refine the output further.
```
>>> list(ranger_suits.keys())
['Zack', 'Tommy']
```
The '.values()' method can be used to see a list of dictionary values
```
>>>list(ranger_suits.values())
['black', 'white']
```
We can then take the list of values and pass it into a variable
```
>>> vals = list(ranger_suits.values())
>>> vals
['black', 'white']
```
We can now use a '.count' method on the variable to see how many instances of somwthing there are
```
>>> vals.count('black')
1
```
We can add to the dictionary like so:
```
ranger_suits['Billy'] = 'blue'
```
