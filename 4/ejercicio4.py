from deap import creator
from deap import algorithms
from deap import tools
from deap import base

import numpy as np
import pandas as pd
import random as rd
import array

datos = pd.read_csv('matriz.csv', header=0)


def evaluacion(individual):

    dist = distM[individual[-1]][individual[0]]
    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        dist += distM[gene1][gene2]
    return dist,


def main():
    rd.seed(169)

    pop = toolbox.population(n=1000)

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 100, stats=stats,
                        halloffame=hof)

    return pop, stats, hof


pi = []
ka = []
chu = 4

for j in range(4):
    fila = datos.iloc[j]
    for i in range(4):
        ka.append(fila[i])
    pi.append(ka)
    ka = []
print("matriz de rutas: ", pi)
print("\n")

distM = pi

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='i',
               fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", rd.sample, range(chu), chu)
toolbox.register("individual", tools.initIterate,
                 creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=30)
toolbox.register("evaluate", evaluacion)

if __name__ == "__main__":
    pop, stats, hof = main()
    # print(hof)
    # print(evaluacion(hof[0]))
