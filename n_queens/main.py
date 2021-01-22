"""
Code written by Curtis Godwin -- cmg39658@uga.edu
"""

import random
from candidate import Candidate
from quick_sort import Sorts

#choose number of queens AKA board size
num_queens = 15

#set hyperparameters
max_iterations = 10000
pop_size = 127

#generate our initial population of candidates
population = []
for i in range(pop_size):
    candidate = Candidate(num_queens = num_queens)
    fitness = candidate.fitness
    #print(candidate.permutation)
    #print(candidate.fitness)
    population.append([candidate, fitness])

# sort population in order of fitness
quick_sort = Sorts()
quick_sort.quick_sort_easy(population, wide=True)

fitness_calculations = 0
while fitness_calculations < max_iterations:
    # pull 5 random candidates and pick the best two to be parents for the next child
    random_indices = []
    for i in range(0,5):
        random_indices.append(random.randint(0,pop_size-1))
    quick_sort.quick_sort_easy(random_indices, wide=False)
    random_indices.reverse()

    # use generate_child to create a new child out of the two chosen parents
    child = population[random_indices[0]][0].generate_child(population[random_indices[1]][0], num_queens)

    #flip a coin to determine whether to perform a swap mutation
    #this helps to preserve diversity in the population
    if random.randint(0,2) == 1:
        num_units = child.num_queens
        random_index_1 = random.randint(0,num_units-1)
        random_index_2 = random.randint(0,num_units-1)
        new_entry_1 = (random_index_1+1, child.permutation[random_index_2][1])
        new_entry_2 = (random_index_2+1,child.permutation[random_index_1][1])
        #print(new_entry_1)
        #print(new_entry_2)
        child.permutation[random_index_1] = new_entry_1
        child.permutation[random_index_2] = new_entry_2

    #sort the new child into the population and then remove the lowest fitness individual
    population.append([child,child.fitness])
    quick_sort.quick_sort_easy(population,wide=True)
    population.remove(population[0])

    #increment fitness calculations
    fitness_calculations += 1

    #termination condidtion for finding a solution
    if child.fitness == 100:
        break

#print the best found individual
print(population[pop_size-1][0].permutation, population[pop_size-1][1])

#print the worst individual left in the population for fun
print(population[0][0].permutation, population[0][1])
