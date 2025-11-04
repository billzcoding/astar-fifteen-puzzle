A* Search Implementation for the 15-Puzzle

This repository contains an implementation of the A* search algorithm in Python, applied specifically to solve the classic 15-Puzzle problem (4x4 grid).

The code is structured into several modules to separate the search algorithm logic, node structure, and problem-specific details.

Repository Structure

The project consists of four main Python files:

File Name

Description

Status

node.py

Defines the abstract Node class. (Do Not Modify)

Provided

search.py

Contains the complete implementation of the core Astar search algorithm.

Completed

problems.py

Implements the problem-specific logic for the FifteensNode class, including heuristic calculation (Manhattan Distance), goal testing, and child generation.

Completed

test.py

A script containing unit tests to verify the correctness of the FifteensNode and Astar implementation.

Provided

Implementation Details

search.py

The Astar(root) function uses a priority queue (heapq) to manage the fringe and a set (evaluated_states) to keep track of visited node states, ensuring the algorithm finds the optimal (lowest-cost) path.

problems.py (FifteensNode)

The following core methods were implemented for the 15-Puzzle:

is_goal(): Checks if the current board state matches the solved configuration.

generate_children(): Expands the current node by finding the position of the empty tile (0) and generating new states by swapping it with adjacent tiles (up, down, left, right).

evaluate_heuristic(): Calculates the Manhattan Distance heuristic (h(n)), which sums the distance of every misplaced tile from its goal position. This heuristic is admissible and consistent, guaranteeing the A* algorithm finds an optimal solution.

How to Run Tests

To test the implementation and verify all required functionalities are working correctly, run the provided test.py file using the Python unittest module from your terminal:

python -m unittest test.py


A successful run will show output indicating that all tests passed, confirming the A* algorithm and the 15-Puzzle logic are functioning as expected.
