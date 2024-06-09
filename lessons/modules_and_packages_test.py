from space.planet import Planet
from space.calc import planet_mass, planet_vol

aquator = Planet('Aquator', 15299, 11.15, 'nothing')

aquator_mass = planet_mass(aquator.gravity, aquator.radius)
aquator_vol = planet_vol(aquator.radius)

print(f'{aquator.name} has a mass of {aquator_mass} and a volume of {aquator_vol}')