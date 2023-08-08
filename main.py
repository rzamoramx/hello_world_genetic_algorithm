
import random

# Function to generate a random string of characters from the alphabet
def generate_random_string(length):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    return ''.join(random.choice(alphabet) for _ in range(length))

# Fitness function to evaluate the similarity between the string and the target "Hello world"
def calculate_fitness(string):
    target = "Hello world"
    fitness = sum(1 for a, b in zip(string, target) if a == b)
    return fitness

# Function to select individuals based on their fitness (roulette wheel approach)
def roulette_selection(population, num_parents):
    fitness_values = [calculate_fitness(c) for c in population]
    total_fitness = sum(fitness_values)
    selection_probabilities = [fitness / total_fitness for fitness in fitness_values]
    parents = random.choices(population, weights=selection_probabilities, k=num_parents)
    return parents

# Function to crossover two strings and produce a new offspring
def crossover(string1, string2):
    crossover_point = random.randint(1, len(string1) - 1)
    offspring = string1[:crossover_point] + string2[crossover_point:]
    return offspring

# Function to apply mutation to a string with a certain probability
def mutation(string, mutation_probability):
    mutated_string = ''.join(c if random.random() > mutation_probability else random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ") for c in string)
    return mutated_string

# Genetic algorithm parameters
population_size = 1000
num_generations = 1000
crossover_probability = 0.8
mutation_probability = 0.1

# Create initial population
population = [generate_random_string(len("Hello world")) for _ in range(population_size)]

# Evolution of the genetic algorithm
for generation in range(num_generations):
    # Select parents
    parents = roulette_selection(population, num_parents=int(population_size / 2))

    # Crossover parents to generate new offspring
    offspring = []
    while len(offspring) < population_size - len(parents):
        parent1, parent2 = random.sample(parents, 2)
        if random.random() < crossover_probability:
            child = crossover(parent1, parent2)
            offspring.append(child)

    # Combine parents and new offspring
    population = parents + offspring

    # Apply mutation
    population = [mutation(string, mutation_probability) for string in population]

    # Sort population by fitness (highest to lowest)
    population.sort(key=lambda x: calculate_fitness(x), reverse=True)

    # Display the best string in each generation
    print(f"Generation {generation}: {population[0]} (Fitness: {calculate_fitness(population[0])})")

# Display the string with the best fitness at the end
print("Best string found:", population[0])

