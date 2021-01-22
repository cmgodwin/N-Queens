#this import allows us to set our directory to the location of the current file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import random
from quick_sort import Sorts

## the candidate class contains information and functions pertaining to a
## particular candidate within the N_Queens solution space;
## candidates are represented as size-N lists containing size-2 lists of
## coordinates--the x-coordinates are always in order while the y-coordinates
## are flexible -- therefore candidate solutions are represented as
## permutations of y

class Candidate():

    # variables for each candidate
    permutation=[]
    fitness=0
    num_queens = 8

    def __init__(self, permutation=None, num_queens=None):
        if num_queens is not None:
            self.num_queens = num_queens
        if permutation is not None:
            self.permutation = permutation
        else:
            self.permutation = self.generate_permutation()
        self.fitness = self.determine_fitness(self.permutation)


    ## generate_permutation() generates a permutation of the numbers between 0 and n
    def generate_permutation(self):

        ## define number of queens as n for readability
        n = self.num_queens

        ## make an ordered list of size n to be shuffled
        unshuffled_list = []
        for i in range(n):
            unshuffled_list.append(i)

        # now shuffle the list into a permutation
        permutation = []
        for i in range(n):
            #first choose a remaining available index randomly
            random_index = random.randint(0,n-1-i)
            # append the value at the randomly chosen index to the permutation
            permutation.append((i+1,unshuffled_list[random_index]+1))
            # delete the the value at the randomly chosen index
            del unshuffled_list[random_index]
        return permutation

    # determine_fitness calculates the fitness of a given permutation;
    # the only penalized quality in this implementation is the sharing of
    # diagonals between coordinates-- this is calculated for each point
    # based on where it holds true that the change in X equals the
    # change in Y -- every coordinate is compared to every other coordinate,
    # requiring a nested loop
    def determine_fitness(self, permutation):
        fitness = 100
        for first_point in permutation:
            for second_point in permutation:
                if first_point != second_point:
                # if the change in X is equal to the change in Y,
                # a diagonal is shared and the fitness is penalized by 20;
                # this happens twice for each diagonal, which is not a
                # problem since it happens for all candidates, so the
                # fitness is still generalized
                    if abs(first_point[0]-second_point[0]) == abs(first_point[1]-second_point[1]) :
                        fitness -= 10
        return fitness

    # performs an order-preserving crossover with the current candidate and the
    # the chosen second parent and returns a single child
    def generate_child(self, other_candidate,num_units,cities=None):
        child_permutation = [0 for x in range(num_units)]
        seg_end = random.randint(1, num_units-1)
        seg_start = random.randint(0, seg_end-1)
        #print(seg_start)
        #print(seg_end)
        keep_seg = []
        deciding_value = random.randint(0,99)
        if deciding_value<75:
            chosen_permutation = self.permutation
            other_permutation = other_candidate.permutation
        else:
            chosen_permutation = other_candidate.permutation
            other_permutation = self.permutation
        for i in range(seg_start,seg_end):
            keep_seg.append(chosen_permutation[i][1])

        #print(keep_seg)
        #print(chosen_permutation)
        #print(other_permutation)
        j = seg_end
        for i in range(seg_end, num_units):
            if j == num_units:
                j=0
            if other_permutation[i][1] not in keep_seg:
                child_permutation[j] = other_permutation[i]
                j += 1

        for i in range(0, seg_end):
            if j == num_units:
                j=0
            if i >= seg_start and i < seg_end:
                child_permutation[i] = i,keep_seg[i-seg_start]
            if other_permutation[i][1] not in keep_seg:
                child_permutation[j] = other_permutation[i]
                j += 1

        for i in range(0,num_units):
            child_permutation[i] = (i+1, child_permutation[i][1])

        child_candidate = Candidate(child_permutation)
        return child_candidate
