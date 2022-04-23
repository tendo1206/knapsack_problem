from random import *
from decimal import Decimal
from genetic_class import Individual
from main import GENOM_LENGTH

def mutation(individuals, mutation_rate):
    new_individuals = []
    for ind in individuals:
        if mutation_rate > (randint(0, 100) / Decimal(100)):
            ind = substitution(ind)

        new_individuals.append(ind)

    return new_individuals

def substitution(ind):
    genom = ind.get_genom()

    point1 = randint(0, GENOM_LENGTH-1)
    point2 = randint(point1, GENOM_LENGTH-1)

    tmp = genom[point1]
    genom[point1] = genom[point2]
    genom[point2] = tmp

    mutant = Individual(genom, 0, 0)

    return mutant


def inversion(ind):
    genom = ind.get_genom()

    point1 = randint(0, GENOM_LENGTH)
    point2 = randint(point1, GENOM_LENGTH)

    section = genom[point1:point2]
    section.reverse()

    new_genom = genom[:point1] + section + genom[point2:]
    mutant = Individual(new_genom, 0, 0)

    return mutant


def scramble(ind):
    genom = ind.get_genom()

    point1 = randint(0, GENOM_LENGTH)
    point2 = randint(point1, GENOM_LENGTH)

    section = genom[point1:point2]
    section.shuffle()

    new_genom = genom[:point1] + section + genom[point2:]
    mutant = Individual(new_genom, 0, 0)

    return mutant


def translocation(ind):
    genom = ind.get_genom()

    point1 = randint(0, GENOM_LENGTH)
    point2 = randint(point1, GENOM_LENGTH)

    section = genom[point1:point2]
    remaining = genom[:point1] + genom[point2:]

    insert_point = randint(0, len(remaining))

    remaining[insert_point:insert_point] = section
    mutant = Individual(remaining, 0, 0)

    return mutant