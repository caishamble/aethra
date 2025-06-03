import random

# DO NOT CHANGE THIS
random.seed(10)

NUM_GENERATIONS = 200
NUM_POPULATION = 100
PROBABILITY_MUTATION = 0.2
PROBABILITY_CROSSOVER = 0.8
ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

BANNER = """
**************************************************************
Welcome to GeneticGuess Sentencer!
This program will attempt to guess a sentence that you input.
Simply input a sentence and the program will attempt to guess it!
**************************************************************
"""

INPUT = "\nWould you like to continue? (y/n) "

"\nPlease input the sentence you would like the program to guess: "
"\nIncorrect input. Please try again.\n"
"\n\nGeneticGuess results:"
"Generation: "
"I found the sentence early!"
"\nBest Individual: "
"\n\nThank you for using GeneticGuess Sentencer!"


# a
def make_population(target):
    population = ''
    len_population = NUM_POPULATION * len(target)
    for i in range(len_population):
        population += random.choice(ALPHABET)
    return population


# b
def fitness(target, individual):
    similar = 0
    ans = 0
    for i in range(len(target)):
        if individual[i] == target[i]:
            similar += 1
        ans = similar / len(target)
    return ans


# d
def mutation(individual):
    for i in range(len(individual)):
        chosen_number = random.random()
        if chosen_number <= PROBABILITY_MUTATION:
            if i == 0:
                individual = random.choice(ALPHABET) + individual[1:]
            else:
                individual = individual[:i] + random.choice(ALPHABET) + individual[i+1:]
        else:
            continue
    return individual



def single_point_crossover(individual1, individual2):
    judge_number = random.random()
    if judge_number <= PROBABILITY_CROSSOVER:
        point_to_cross = random.randint(1, len(individual1))
        new_individual1 = individual1[:point_to_cross] + individual2[point_to_cross:]
        new_individual2 = individual2[:point_to_cross] + individual1[point_to_cross:]
        return new_individual1, new_individual2
    else:
        return individual1, individual2


# c
def five_tournament_selection(population, target):
    individual_fitness = -1
    individual = ''

    best_individual = ''

    p = 0

    while p < 5:

        k = random.randint(0, NUM_POPULATION - 1)
        if k == NUM_POPULATION - 1:
            individual = population[k * len(target):]

        elif k < NUM_POPULATION - 1:
            beginning_index = k * len(target)
            end_index = beginning_index + len(target)
            individual = population[beginning_index:end_index]

        if fitness(target, individual) > individual_fitness:
            individual_fitness = fitness(target, individual)
            best_individual = individual
        p += 1
    return best_individual

def find_best_individual(population, target):
    individual = ''
    individual_fitness = -1
    best_individual = ''
    p = 0
    while p <= NUM_POPULATION - 1:
        if p <= NUM_POPULATION - 2:
            beginning_index = p * len(target)
            end_index = beginning_index + len(target)
            individual = population[beginning_index:end_index]

        elif p == NUM_POPULATION - 1:
            individual = population[p * len(target):]

        if fitness(target, individual) > individual_fitness:
            individual_fitness = fitness(target, individual)
            best_individual = individual
        p += 1
    return best_individual




def main():
    print(BANNER)
    while True:

        user_input = input(INPUT)
        if user_input == 'y' or user_input == 'Y':

            while True:
                target_input = input("\nPlease input the sentence you would like the program to guess: ").lower()
                if all(char in ALPHABET for char in target_input):
                    target = target_input
                    break
                else:
                    print("\nIncorrect input. Please try again.\n")

            population = make_population(target)

            print("\n\nGeneticGuess results:")
            sentence_found = False
           # new_population = ''
            for i in range(NUM_GENERATIONS):

                print("Generation: ", i)
                new_population = ''
                for j in range(NUM_POPULATION):
                    new_individual1 = five_tournament_selection(population, target)
                    new_individual2 = five_tournament_selection(population, target)

                    new_individual1 = mutation(new_individual1)
                    new_individual2 = mutation(new_individual2)

                    more_new_individual1, more_new_individual2 = single_point_crossover(new_individual1,new_individual2)

                    fitness1 = fitness(target, more_new_individual1)
                    fitness2 = fitness(target, more_new_individual2)
                    if fitness1 > fitness2:
                        most_new_individual = more_new_individual1
                    else:
                        most_new_individual = more_new_individual2
                    new_population += most_new_individual


                    if fitness1 == 1 or fitness2 == 1:
                        print("I found the sentence early!")
                        print("\nBest Individual: ", most_new_individual)
                        sentence_found = True
                        break

                population = new_population
                if sentence_found:
                    break
            if not sentence_found:
                print("\nBest Individual: ", find_best_individual(population, target))
        else:
            print("\n\nThank you for using GeneticGuess Sentencer!")
            break

if __name__ == '__main__':
    main()