import random

# Función de evaluación (maximizar)
def fitness_function(individual):
    return sum(individual)

# Inicialización de la población
def initialize_population(pop_size, ind_size):
    population = []
    for _ in range(pop_size):
        individual = [random.randint(0, 9) for _ in range(ind_size)]
        population.append(individual)
    return population

# Cruzamiento de dos individuos
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutación de un individuo
def mutate(individual):
    mutation_point = random.randint(0, len(individual) - 1)
    individual[mutation_point] = random.randint(0, 9)
    return individual

# Algoritmo genético
def genetic_algorithm(pop_size, ind_size, generations):
    population = initialize_population(pop_size, ind_size)
    for _ in range(generations):
        population.sort(key=lambda x: fitness_function(x), reverse=True)
        new_population = []
        for i in range(0, pop_size, 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
    return population[0]

if __name__ == "__main__":
  # Parámetros del algoritmo genético
  population_size = 10
  individual_size = 5
  num_generations = 5

  # Ejecutar el algoritmo genético
  result = genetic_algorithm(population_size, individual_size, num_generations)
  print("Resultado:", result)
  print("Valor máximo:", fitness_function(result))
