# My first GitHub project
This is my first GitHub project. I published this directly from VS Code.
The below is still just notes and should not be viewed as instructions.

Activate the Virtual Environment:
env\Scripts\activate

Deactivate the Virtual Environment:
deactivate

View packages in the current environment:
pip list

Install "Requests":
pip install requests

Install requirements.txt:
pip install -r requirements.txt

To start python in a shell:
python

Mathematical Operators:
+, -, *, / (returns float), // (returns int), ** (exponents), % (modulus or remainder)

Pulling text from within a string:
greet = 'hello'
greet[1]
returns: 'e'

greet[0:3]
returns: 'hel'

greet * 3
returns: 'hellohellohello'

Methods:
upper()
greet.upper()
returns: 'HELLO'

split()
cheeses = 'brie, cheddar, stilton'
cheeses.split(',')
returns: ['brie','cheddar','stilton']

len()
greet = 'hello'
len(greet)
returns: 5