from shakespeare.DNA import *


class Population:
    mutationrate = 0
    population = []
    matingPool = []
    target = ""
    generations = 0
    finished = False
    perfectScore = 0

    def __init__(self, p, m, num):
        self.target = p
        self.mutationrate = m
        for x in range(num):
            self.population.append(DNA(len(self.target)))
        self.calcuFitness()

        self.perfectScore = pow(len(self.target), 2)

    def calcuFitness(self):
        for x in range(len(self.population)):
            self.population[x].calcFitness(self.target)

    def naturalSelection(self):
        self.matingPool.clear()

        maxFitness = 0
        for x in range(len(self.population)):
            if self.population[x].fitness > maxFitness:
                maxFitness = self.population[x].fitness

        for x in range(len(self.population)):
            fitness = (self.population[x].fitness / maxFitness)
            n = int(fitness * 100)
            for y in range(0, n):
                self.matingPool.append(self.population[x])

    def generate(self):
        for x in range(len(self.population)):
            a = random.randint(0, len(self.matingPool)-1)
            b = random.randint(0, len(self.matingPool)-1)
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutationrate)
            self.population[x] = child
        self.generations += 1

    def getBest(self):
        worldrecord = 0.0
        index = 0
        for x in range(len(self.population)):
            if self.population[x].fitness > worldrecord:
                index = x
                worldrecord = self.population[x].fitness

        if worldrecord == self.perfectScore:
            self.finished = True
        return self.population[index].getPhrase()

    def getAverageFitness(self):
        total = 0.0
        for x in range(len(self.population)):
            total += self.population[x].fitness
        return total / len(self.population)
