import random

class GeneticAlgorithm:
    def __init__(self, total, length, pop_size=30, mutation_rate=0.2, generations=200):
        self.total = total
        self.length = length
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.generations = generations

    def create_individual(self):
        parts = [0] * self.length
        remaining = self.total
        for i in range(self.length - 1):
            value = random.randint(0, remaining)
            parts[i] = value
            remaining -= value
        parts[-1] = remaining
        random.shuffle(parts)
        return parts

    def create_population(self):
        return [self.create_individual() for _ in range(self.pop_size)]

    def fitness(self, individual):
        return - (max(individual) - min(individual))

    def selection(self, population):
        population.sort(key=self.fitness, reverse=True)
        return population[0], population[1]

    def crossover(self, p1, p2):
        point = random.randint(1, self.length - 1)
        child = p1[:point] + p2[point:]

        diff = self.total - sum(child)
        child[-1] += diff
        return child

    def mutation(self, individual):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.length), 2)
            if individual[i] > 0:
                individual[i] -= 1
                individual[j] += 1
        return individual

    def run(self):
        population = self.create_population()

        for _ in range(self.generations):
            p1, p2 = self.selection(population)
            new_population = [p1, p2]

            while len(new_population) < self.pop_size:
                child = self.crossover(p1, p2)
                child = self.mutation(child)
                new_population.append(child)

            population = new_population

        return max(population, key=self.fitness)


if __name__ == "__main__":
    total = int(input("Enter total: "))
    length = int(input("Enter length: "))

    ga = GeneticAlgorithm(total, length)
    result = ga.run()

    print("\nResult:")
    print(result)
