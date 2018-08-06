import random


class DNA:
    fitness = 0

    def __init__(self, num):
        self.genes = []
        for x in range(num):
            self.genes.append(chr(random.randint(32, 126)))

    def getPhrase(self):
        return ''.join(self.genes)

    def calcFitness(self, target):
        score = 0
        for x in range(len(self.genes)):
            if self.genes[x] == target[x]:
                score += 1

        self.fitness = pow(score, 2)
        return self.fitness

    def crossover(self, partner):
        child = DNA(len(self.genes))

        midpoint = random.randint(0, len(self.genes))

        for x in range(len(self.genes)):
            if x > midpoint:
                child.genes[x] = self.genes[x]
            else:
                child.genes[x] = partner.genes[x]

        return child

    def mutate(self, mutationRate):
        for x in range(len(self.genes)):
            if random.random() < mutationRate:
                self.genes[x] = chr(random.randint(32, 126))
