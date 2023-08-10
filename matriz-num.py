import random

# Función de inicialización de la población
def initialize_population(population_size, matrix_size):
    population = []
    for _ in range(population_size):
        individual = [(random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1)) for _ in range(matrix_size)]
        population.append(individual)
    return population

# Función de evaluación de aptitud (fitness)
def fitness_function(individual, matrix):
    max_value = max(matrix[i -1][j - 1] for (i, j) in individual)
    return max_value

# Función de selección de padres mediante torneo
def select_parents(population, matrix):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    return parent1, parent2

# Función de cruce (crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1))
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Función de mutación
def mutate(child, mutation_rate, matrix_size):
    for i in range(len(child)):
        if random.random() < mutation_rate:
            child[i] = (random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1))
    return child

# Algoritmo genético
def genetic_algorithm(matrix, population_size, generations, mutation_rate):
    matrix_size = len(matrix)
    population = initialize_population(population_size, matrix_size)
    for generation in range(generations):
        population.sort(key=lambda individual: fitness_function(individual, matrix), reverse=True)
        print(f"Generación {generation}: {population[0]} - Valor máximo: {fitness_function(population[0], matrix)}")
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, matrix)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate, matrix_size)
            child2 = mutate(child2, mutation_rate, matrix_size)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population

if __name__ == "__main__":
  # Matriz de números
  matrix = [
      [23, 45, 67],
      [12, 89, 34],
      [56, 78, 90]
  ]

  # Parámetros del algoritmo genético
  population_size = 20
  generations = 10
  mutation_rate = 0.1

  # Ejecutar el algoritmo genético
  genetic_algorithm(matrix, population_size, generations, mutation_rate)
