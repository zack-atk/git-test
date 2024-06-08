# CLASSES
# We can define a class and then assign properties to objects of that class:

# Here, we define the class and the properties of that class:
class Planet:
# When we define the init funciton, the values we pass in will be assigned as properties of the object.    
    def __init__(self, name, radius, gravity, moons):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.moons = moons
# We can define a function and pass in properties of our new object:        
    def orbit(self):
        return f'{self.moons} orbits {self.name}'

#Let's use planets from Borderlands in this example:        
pandora = Planet('Pandora', '3958.8 mi', '9.8 m/s\u00b2', 'Elpis')
print(f'Name is: {pandora.name}')
print(f'Radius is: {pandora.radius}')
print(f'Gravity is: {pandora.gravity}')
print(pandora.orbit())

aquator = Planet('Aquator', '15,299 mi', '11.15 m/s\u00b2', 'nothing')
print(f'Name: {aquator.name}')
print(f'Radius: {aquator.radius}')
print(f'Gravity: {aquator.gravity}')
print(aquator.orbit())