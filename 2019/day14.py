#!/usr/bin/env python3

import sys
import math

# Map from result -> reaction
reactions = {}


class Reaction():
    def __init__(self, raw_string: str):
        self.produced_amount = 0
        self.used_amount = 0
        if raw_string == 'ORE':
            self.result_ingredient = 'ORE'
            return
        [raw_ingredients, raw_result] = [part.strip()
                                         for part in raw_string.split('=>')]
        raw_ingredients_parts = raw_ingredients.split(', ')
        self.result_amount, self.result_ingredient = Reaction._extract_amounts(
            raw_result)
        self.ingredients = {}
        for part in raw_ingredients_parts:
            ingredient_amount, ingredient = Reaction._extract_amounts(part)
            self.ingredients[ingredient] = ingredient_amount

    def produce(self, amount: int, depth: int):
        padding = '  '*depth
        print(f'{padding}Producing {amount} of {self.result_ingredient}')
        if self.result_ingredient == 'ORE':
            self.produced_amount += amount
            return

        # required_amount is how much more we need to produce given spare ingredients
        additional_required_amount = float(
            amount - (self.produced_amount - self.used_amount))
        print(
            f'{padding}Additonal required amount: {int(additional_required_amount)} [{amount} - ({self.produced_amount} - {self.used_amount})]')
        # How many rounds of the reaction to perform
        num_of_rounds = math.ceil(
            additional_required_amount/self.result_amount)
        print(f'{padding}Number of rounds: {num_of_rounds}')
        self.used_amount += amount
        self.produced_amount += num_of_rounds * self.result_amount
        print(f'{padding}Produced: {self.produced_amount} Used: {self.used_amount}')

        for ingredient, ingredient_amount in self.ingredients.items():
            reactions[ingredient].produce(
                ingredient_amount * num_of_rounds, depth+1)

    @staticmethod
    def _extract_amounts(raw_string: str):
        [amount, ingredient] = raw_string.split(' ')
        return int(amount), ingredient

    def __repr__(self):
        return f'Result: {self.result_amount} {self.result_ingredient}, Ingredients: {self.ingredients}'


def parse_input(file: str):
    # Read file
    lines = [line.strip() for line in open(file).readlines()]
    for line in lines:
        reaction = Reaction(line)
        reactions[reaction.result_ingredient] = reaction
    print(reactions)


def main():
    if len(sys.argv) != 2:
        print("Requires path to input file")
        exit(1)
    input_path: str = sys.argv[1]
    parse_input(input_path)
    # ORE is special cased, it doesn't need to a reaction to be produced
    reactions['ORE'] = Reaction('ORE')
    # Produce one of FUEL
    reactions['FUEL'].produce(1, 0)
    print('ORE required:', reactions['ORE'].produced_amount)


if __name__ == "__main__":
    main()
