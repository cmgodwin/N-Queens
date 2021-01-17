# N-Queens-Problem

#This code uses an evolutionary algorithm to solve the N-Queens problem. More specifically, candidate solutions have corresponding fitness scores, and an evolutionary process ensues in which lower fitness-score individuals are unlikely to survive. Of those that survive, some are mutated to search the problem space for higher fitness solutions. Ultimately, the 
algorithm can be arbitrarily stopped at any point and the highest-fitness individual will be the closest candidate to a solution. 

The solutions are formatted as lists of n unique numbers. Since there must be a queen on each file, the number at each index in the list serves as the position within that file where the queen sits. The fitness scores are calculated based on the number of shared diagonals between queens in a given solution. Starting at 100, each candidate is penalized 10 points for each instance of queens sharing diagonals. 

This means that if our algorithm finds a 100-fitness individual, it has found a solution.
