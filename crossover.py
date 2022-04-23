from random import *
from genetic_class import Individual

def two_point(ind1, ind2, genom_length):
    point1 = randint(0, genom_length)
    point2 = randint(point1, genom_length)

    genom1 = ind1.get_genom()
    genom2 = ind2.get_genom()

    progeny_genom1 = genom1[:point1] + genom2[point1:point2] + genom1[point2:]
    progeny_genom2 = genom2[:point1] + genom1[point1:point2] + genom2[point2:]

    progeny_ind1 = Individual(progeny_genom1, 0, 0)
    progeny_ind2 = Individual(progeny_genom2, 0, 0)

    return progeny_ind1, progeny_ind2


def uniform(ind1, ind2, genom_length):
    genom1 = ind1.get_genom()
    genom2 = ind2.get_genom()

    for i in range(len(genom_length)):
        if randint(0, 1) == 0:
            tmp = genom1[i]
            genom1[i] = genom2[i]
            genom2[i] = tmp

    progeny_ind1 = Individual(genom1, 0, 0)
    progeny_ind2 = Individual(genom2, 0, 0)

    return progeny_ind1, progeny_ind2