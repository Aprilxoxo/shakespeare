from shakespeare.Population import Population

target = "Das Internet ist fuer uns alle Neuland"
popmax = 250
mutationRate = 0.01

population = Population(target, mutationRate, popmax)

while not population.finished:
    population.naturalSelection()
    population.generate()
    population.calcuFitness()
    print("best of generation " + str(population.generations) + " : " + str(population.getBest()))
    print("average fitness: " + str(population.getAverageFitness()))

