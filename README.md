# Evolutionary Approach to the N-Queens Problem

The 8-Queens problem is a classic puzzle whose goal is to place 8 queens on a chessboard and have none of them threatening another. The N-Queens problem is a generalization
of this problem to an NxN sized board.

This code uses an evolutionary algorithm to tackle the N-Queens problem. More specifically, candidate solutions have corresponding fitness scores, and an evolutionary process ensues in which lower-fitness candidates are unlikely to survive. Of those that survive, some are mutated to search the problem space for higher-fitness candidates. The algorithm can be arbitrarily stopped at any point and the highest-fitness individual will be the closest candidate to a solution. 

The solutions are formatted as lists of n unique numbers. Since there must be a queen on each column (or "file" in chess lingo), the number at each index in the list serves as the position within that column where the queen sits. This ensures that no candidate solutions will have queens standing on the same row or column as another queen, but they can still have queens sharing diagonals.

Since our setup prevents faulty solutions other than those involving shared diagonals, the fitness scores are calculated based on the number of shared diagonals between queens in a given solution. Starting at 100, each candidate is penalized 10 points for each instance of queens sharing diagonals. This means that if our algorithm finds a 100-fitness individual, it has found a solution.

As an example for the output format, here is a solution (100-fitness individual) found by the algorithm for N=15:

[(1, 6), (2, 9), (3, 5), (4, 14), (5, 8), (6, 15), (7, 3), (8, 7), (9, 13), (10, 10), (11, 12), (12, 2), (13, 4), (14, 11), (15, 1)]
