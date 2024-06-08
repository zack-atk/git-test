# PYTHON NOTES
The below is still just notes and should not be viewed as instructions.

---
### Activate the Virtual Environment:
```
env\Scripts\activate
```
### Deactivate the Virtual Environment:
```
deactivate
```
### View packages in the current environment:
```
pip list
```
### Install "Requests":
```
pip install requests
```
### Install requirements.txt:
```
pip install -r requirements.txt
```
### To start python in a shell:
```
python
```
### Mathematical Operators:
| OPERATOR | RETURNS |
|----------|---------|
| +, -, *, / | float | 
| // (divide w/o remainder) | int |
| ** (exponents) | float |
| % (modulus or remainder) | int |

### Pulling text from within a string:
**Example 1:**
```
greet = 'hello'
greet[1]
``` 
*returns:* 
```
'e'
```
**Example 2:**
```
greet[0:3]
```
*returns:* 
```
'hel'
```
**Example 3:**
```
greet * 3
```
*returns:*
```
'hellohellohello'
```
### Methods:

**upper()**
```
greet.upper()
```
*returns:*
```
'HELLO'
```
**split()**
```
cheeses = 'brie, cheddar, stilton'
cheeses.split(',')
```
*returns:* 
```
['brie','cheddar','stilton']
```
**len()**
```
greet = 'hello'
len(greet)
```
*returns:* 
```
5
```