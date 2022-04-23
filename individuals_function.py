from random import *
from decimal import *
from operator import mul
from mutation import *

from genetic_class import Individual

# 個体を生成
def generate_individual(genom_length):
    genom = []

    # バイナリエンコーディングで遺伝子生成
    for i in range(genom_length):
        genom.append(randint(0, 1))

    ind = Individual(genom, 0, 0)
    return ind

# 個体を評価
def evaluate_individual(ind, prices, volumes, max_volume):
    total_volume = sum(map(mul, ind.get_genom(), volumes))
    ind.set_volume(total_volume)

    if total_volume <= max_volume:
        ind.set_evaluation(sum(map(mul, ind.get_genom(), prices)))
    else:
        ind.set_evaluation(0)

    return ind

# 次世代個体集団の決定
def create_next_generation(individuals, elites, progenys, mutation_rate):
    next_individuals = sorted(individuals, key=lambda u: u.get_evaluation())

    for i in range(len(elites) + len(progenys)):
        next_individuals.pop(0)

    next_individuals.extend(elites)
    next_individuals.extend(progenys)

    return mutation(next_individuals, mutation_rate)