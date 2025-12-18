import random

# -------------------- Fitness Function --------------------
def fitness(chromosome):
    """Counts number of non-attacking queen pairs"""
    n = len(chromosome)
    non_attacking = 0
    max_pairs = n * (n - 1) // 2

    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] != chromosome[j] and \
               abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking += 1

    return non_attacking, max_pairs


# -------------------- Genetic Algorithm --------------------
def genetic_n_queens(n, pop_size=100, mutation_rate=0.2, max_generations=1000):

    max_fitness = n * (n - 1) // 2

    # Initial population
    population = [random.sample(range(n), n) for _ in range(pop_size)]

    for generation in range(max_generations):

        population.sort(key=lambda c: fitness(c)[0], reverse=True)

        best = population[0]
        best_fit, _ = fitness(best)

        print(f"Generation {generation} | Fitness: {best_fit}")

        if best_fit == max_fitness:
            print("\n✅ Solution Found")
            return best

        # Selection (Top 50%)
        parents = population[:pop_size // 2]

        # Create next generation
        new_population = parents[:]

        while len(new_population) < pop_size:
            p1, p2 = random.sample(parents, 2)

            # Crossover
            cut = random.randint(1, n - 2)
            child = p1[:cut] + [x for x in p2 if x not in p1[:cut]]

            # Mutation
            if random.random() < mutation_rate:
                i, j = random.sample(range(n), 2)
                child[i], child[j] = child[j], child[i]

            new_population.append(child)

        population = new_population

    return None


# -------------------- Run --------------------
if __name__ == "__main__":
    N = 8
    solution = genetic_n_queens(N)

    if solution:
        print("\nQueen Positions (Column → Row):")
        print(solution)
