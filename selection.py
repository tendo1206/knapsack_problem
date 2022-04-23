from random import *

def roulette(individuals):
    accum = 0
    accums = []

    for ind in individuals:
        accum += ind.get_evaluation()
        accums.append(accum)

    r = random.random() * accum

    for i, accum in enumerate(accums):
        if r < accum:
            return individuals[i]


def ranking(individuals):
    ranked_individuals = sorted(individuals, reverse=True, key=lambda u: u.get_evaluation())
    accum = 0
    accums = []

    for i in individuals:
        accum += 1 / i
        accums.append(accum)

    r = random.random() * accum

    for i, accum in enumerate(accums):
        if r < accum:
            return ranked_individuals[i]

def tournament(individuals, tournament_size):
    if (tournament_size > len(individuals)):
        tournament_size = len(individuals)

    participants = random.sample(individuals, tournament_size)
    ranked_participants = sorted(participants, reverse=True, key=lambda u: u.get_evaluation())
    return ranked_participants[0]

# エリート主義
def elitism(individuals, elite_length):
    sorted_individuals = sorted(individuals, reverse=True, key=lambda u: u.get_evaluation())
    return [sorted_individuals.pop(0) for i in range(elite_length)]