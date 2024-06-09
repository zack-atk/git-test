class Planet:
    
    shape = 'round'
    
    def __init__(self, name, radius, gravity, moons):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.moons = moons
          
    def orbit(self):
        return f'{self.moons} orbits {self.name}'
    
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} due to gravity'
    
    @staticmethod
    def spin(speed = '2000 mph'):
        return f'The planet spins at {speed}'