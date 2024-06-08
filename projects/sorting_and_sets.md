# Sorting and Sets
### Open a Python shell
From within a new Python shell, we'll need to create a list:
```
>>> numbers = [1,4,3,6,3,8,4,7,5,9]
```
Now, using 'sorted()', we can sort the list:
```
>>> sorted(numbers)
[1, 3, 3, 4, 4, 5, 6, 7, 8, 9]
```
We can also sort lists of strings. In Python, capital letters get a higher 'score' in terms of order.
```
>>> names = ['Jason', 'billy','trini','tommy', 'zack', 'kimberly']
>>> sorted(names)
['Jason', 'billy', 'kimberly', 'tommy', 'trini', 'zack']
```
Sets act similarly to distinct, and removes duplicates from a list, although it returns a non-sorted list:
```
>>> set(numbers)
{1, 3, 4, 5, 6, 7, 8, 9}

>>> set(names)
{'tommy', 'zack', 'Jason', 'billy', 'trini', 'kimberly'}
```
Let's create a dictionary:
```
>>> rangers = {'Jason':'red', 'Zack':'black', 'Billy':'blue', 'Trini':'yellow', 'Kimberly':'pink', 'Tommy':'green'} 
```
Now we can use methods on it:
```
>>> rangers.values()
dict_values(['red', 'black', 'blue', 'yellow', 'pink', 'green'])
```
