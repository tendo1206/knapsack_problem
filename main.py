from individuals_function import *
from selection import *
from crossover import *
import pandas as pd

# 遺伝子長
GENOM_LENGTH = 100

# 個体数
NUM_OF_INDIVIDUALS = 100

# 選択数
SELECT_NUM = 10

# 突然変異率
MUTATION_RATE = 0.001

# 世代数
MAX_GENERATION = 50

# ナップザックの容積
MAX_VOLUME = 1000

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv('goods.csv')
    prices = list(df['price'])
    volumes = list(df['volume'])

    current_individuals = []
    next_individuals = []

    for i in range(NUM_OF_INDIVIDUALS):
        current_individuals.append(generate_individual(GENOM_LENGTH))

    evaluations = []
    for count in range(1, MAX_GENERATION):
        for i in range(NUM_OF_INDIVIDUALS):
            current_individuals[i] = evaluate_individual(current_individuals[i], prices, volumes, MAX_VOLUME)

        elites = elitism(current_individuals, SELECT_NUM)

        progenys = []
        for i in range(1, SELECT_NUM):
            progenys.extend(two_point(elites[i-1], elites[i], GENOM_LENGTH))

        next_individuals = create_next_generation(current_individuals, elites, progenys, MUTATION_RATE)

        fits = [ind.get_evaluation() for ind in current_individuals]

        min_ = min(fits)
        max_ = max(fits)
        avg_ = sum(fits) / Decimal(len(fits))

        print(f'-----第{count}世代の結果-----')
        print(f' Min:{min_}')
        print(f' Max:{max_}')
        print(f' Avg:{avg_}')
        print('')

        current_individuals = next_individuals

        print(f'最も高い価値は{elites[0].get_evaluation()}、そのときの体積は{elites[0].get_volume()}')
        print('------------------------')
        print('')
