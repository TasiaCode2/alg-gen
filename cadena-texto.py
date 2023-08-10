import random

# Función de inicialización de la población
def initialize_population(population_size, target):
    population = []
    for _ in range(population_size):
        individual = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ ") for _ in range(len(target))]
        population.append(individual)
    return population

# Función de evaluación de aptitud (fitness)
def fitness_function(individual, target):
    fitness = sum(1 for a, b in zip(individual, target) if a == b)
    return fitness

# Función de selección de padres mediante torneo
def select_parents(population, target):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    return parent1, parent2

# Función de cruce (crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Función de mutación
def mutate(child, mutation_rate):
    for i in range(len(child)):
        if random.random() < mutation_rate:
            child[i] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    return child

# Algoritmo genético
def genetic_algorithm(target, population_size, generations, mutation_rate):
    population = initialize_population(population_size, target)
    for generation in range(generations):
        population.sort(key=lambda individual: fitness_function(individual, target), reverse=True)
        print(f"Generación {generation}: {population[0]} - Aptitud: {fitness_function(population[0], target)}")
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, target)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population

if __name__ == "__main__":
  # Cadena objetivo
  target = "HELLO WORLD"

  # Parámetros del algoritmo genético
  population_size = 20
  generations = 10
  mutation_rate = 0.1

  # Ejecutar el algoritmo genético
  genetic_algorithm(target, population_size, generations, mutation_rate)
