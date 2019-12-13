#!/usr/bin/python3

import numpy as np
 
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
        self.pos = [int(matches.groups()[0]), int(matches.groups()[1]), int(matches.groups()[2])]
        self.vel = [0, 0, 0]
 
    def step_gravity(self, other_moons):
        for other_moon in other_moons:
            if other_moon.pos[0] > self.pos[0]:
                self.vel[0] += 1
            elif other_moon.pos[0] < self.pos[0]:
                self.vel[0] -= 1
            if other_moon.pos[1] > self.pos[1]:
                self.vel[1] += 1
            elif other_moon.pos[1] < self.pos[1]:
                self.vel[1] -= 1
            if other_moon.pos[2] > self.pos[2]:
                self.vel[2] += 1
            elif other_moon.pos[2] < self.pos[2]:
                self.vel[2] -= 1
 
    def step_velocity(self, other_moons):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]
 
    def get_state(self, axis):
        return (self.pos[axis], self.vel[axis])
 
    def get_energy(self):
        potential = abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
        kinetic = abs(self.vel[0]) + abs(self.vel[1]) + abs(self.vel[2])
        return potential * kinetic
 
    def __str__(self):
        return f"pos=<x={self.pos[0]}, y={self.pos[1]}, z={self.pos[2]}>, vel=<x={self.vel[0]}, y={self.vel[1]}, z={self.vel[2]}>"
 
 
def parse_input(raw_str: str):
    return [Moon(line) for line in raw_str.splitlines()]
 
 
def run_simulation(moons, axis):
    simulation_step = 0
    initial_state = [moon.get_state(axis) for moon in moons]
    while True:
        for moon in moons:
            moon.step_gravity(set(moons) - set([moon]))
        for moon in moons:
            moon.step_velocity(set(moons) - set([moon]))
        current_state = [moon.get_state(axis) for moon in moons]
        simulation_step += 1
        if np.array_equal(initial_state, current_state):
            print(axis, 'repeated at step', simulation_step, current_state)
            return simulation_step
 
if __name__ == "__main__":
    moons = parse_input(input_state)
    repeats = []
    for i in range(3):
        repeats.append(run_simulation(moons, i))
    print("The LCM of", repeats, "is", np.lcm.reduce(repeats))
