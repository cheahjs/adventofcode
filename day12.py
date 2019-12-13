#!/usr/bin/python3
 
example_1 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
example_2 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
input_state = """<x=7, y=10, z=17>
<x=-2, y=7, z=0>
<x=12, y=5, z=12>
<x=5, y=-8, z=6>"""
 
import re
 
state_regex = re.compile(r'<x=(.+), y=(.+), z=(.+)>')
 
class Moon(object):
    def __init__(self, state):
        matches = state_regex.match(state)
        self.x = int(matches.groups()[0])
        self.y = int(matches.groups()[1])
        self.z = int(matches.groups()[2])
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0
 
    def step_gravity(self, other_moons):
        for other_moon in other_moons:
            if other_moon.x > self.x:
                self.vel_x += 1
            elif other_moon.x < self.x:
                self.vel_x -= 1
            if other_moon.y > self.y:
                self.vel_y += 1
            elif other_moon.y < self.y:
                self.vel_y -= 1
            if other_moon.z > self.z:
                self.vel_z += 1
            elif other_moon.z < self.z:
                self.vel_z -= 1
 
    def step_velocity(self, other_moons):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z
 
    def get_energy(self):
        potential = abs(self.x) + abs(self.y) + abs(self.z)
        kinetic = abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)
        return potential * kinetic
 
    def __str__(self):
        return f"pos=<x={self.x}, y={self.y}, z={self.z}>, vel=<x={self.vel_x}, y={self.vel_y}, z={self.vel_z}>"
 
 
def parse_input(raw_str: str):
    return [Moon(line) for line in raw_str.splitlines()]
 
 
def run_simulation(moons):
    simulation_step = 0
    end = 1000
    while simulation_step <= end:
        # print("After", simulation_step, "steps:")
        # [print(moon) for moon in moons]
        if simulation_step == end:
            total_energy = sum([moon.get_energy() for moon in moons])
            print('Total energy:', total_energy)
            break
        for moon in moons:
            moon.step_gravity(set(moons) - set([moon]))
        for moon in moons:
            moon.step_velocity(set(moons) - set([moon]))
        simulation_step += 1
    pass
 
if __name__ == "__main__":
    moons = parse_input(input_state)
    run_simulation(moons)
    pass