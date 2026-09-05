AI-Based Tourist Route and Trip Planning System
Project Description

The **AI-Based Tourist Route and Trip Planning System** is a Python-based application that demonstrates different **Artificial Intelligence search algorithms** for solving tourist route planning and scheduling problems.

The system finds routes between tourist locations using different search techniques and compares their performance based on:

- Total travel cost
- Number of nodes explored
- Execution time

The project also uses **Backtracking** to create a valid tourist day schedule while satisfying predefined constraints.

---

Objectives

The main objectives of this project are:

1. To understand problem-solving through search algorithms.
2. To implement different search algorithms using Python.
3. To find routes between tourist locations.
4. To compare the performance of different search techniques.
5. To solve a tourist scheduling problem using Constraint Satisfaction and Backtracking.

---

Search Algorithms Implemented

The following algorithms are implemented in this project:

1. Breadth First Search (BFS)

BFS explores the search space **level by level**.

It is an example of an **Uninformed Search Algorithm**.

2. Depth First Search (DFS)

DFS explores one branch deeply before backtracking.

It is also an **Uninformed Search Algorithm**.

3. Greedy Best First Search

Greedy Best First Search uses a **heuristic value** to select the most promising location.

It is an **Informed Search Algorithm**.

4. A* Search

A* Search considers both the actual travel cost and the estimated cost to the destination.

The evaluation function used is:

`f(n) = g(n) + h(n)`

where:

- `g(n)` = actual travel cost
- `h(n)` = estimated cost to the destination

5. Hill Climbing

Hill Climbing is a **Local Search Algorithm**.

It moves to a neighboring location that has a better heuristic value.

6. Backtracking

Backtracking is used as a **Constraint Satisfaction technique** to create a valid tourist day schedule.

---

Tourist Locations Used

The project uses a manually defined graph containing tourist locations in Mumbai.

Some of the locations are:

- Gateway of India
- Marine Drive
- Chhatrapati Shivaji Maharaj Terminus
- Elephanta Ferry
- Juhu Beach
- Siddhivinayak Temple
- Bandra Fort
- Sanjay Gandhi National Park

The distances between locations are manually defined in the Python program.

---

Problem Statement

To implement different problem-solving search algorithms using Python and evaluate their performance for solving a tourist route and trip planning problem.

---

Technologies Used

- **Programming Language:** Python
- **IDE:** Visual Studio Code
- **Version Control:** Git and GitHub
Python Libraries

The project uses the following built-in Python libraries:

- `time` – Used to measure execution time.
- `heapq` – Used for priority queues in Greedy Best First Search and A* Search.
- `collections` – Used for the queue required by BFS.

No external Python libraries are required.
