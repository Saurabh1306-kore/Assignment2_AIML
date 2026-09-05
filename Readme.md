# Practical-Assignment-2-Problem-Solving-through-Search

Implementation and performance evaluation of Uninformed, Informed, Local Search, and Constraint Satisfaction algorithms for tourist route planning and day scheduling.

## Practical Title

**Problem Solving through Search**

---

# 1. Aim

To implement and evaluate different Artificial Intelligence search algorithms and compare their performance based on:

- Path found
- Total travel cost
- Number of nodes explored
- Execution time

The practical implements:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Greedy Best-First Search
- A* Search
- Hill Climbing
- Tourist Day Scheduling using Backtracking

---

# 2. Problem Statement

Implement various search algorithms used in Artificial Intelligence for solving a tourist route planning problem.

The algorithms are categorized as:

| Category | Algorithm |
|----------|-----------|
| Uninformed Search | Breadth First Search |
| Uninformed Search | Depth First Search |
| Informed Search | Greedy Best-First Search |
| Informed Search | A* Search |
| Local Search | Hill Climbing |
| Constraint Satisfaction | Tourist Day Scheduling using Backtracking |

The algorithms are evaluated using a tourist route planning problem, where the objective is to find a route from **Gateway of India** to **Sanjay Gandhi National Park**.

Backtracking is also used to generate a valid tourist day schedule while satisfying the defined constraints.

---

# 3. Objectives

- To understand different search strategies used in Artificial Intelligence.
- To implement Uninformed Search algorithms.
- To implement Informed Search algorithms using heuristic functions.
- To implement Local Search using Hill Climbing.
- To solve a Constraint Satisfaction Problem using Backtracking.
- To compare search algorithms based on nodes explored, travel cost, and execution time.

---

# 4. Algorithms Implemented

## 4.1 Breadth First Search (BFS)

BFS explores the search space level by level.

It uses a **Queue (FIFO)** data structure.

### Characteristics:

- Uninformed search
- Explores nodes level by level
- Finds a solution with minimum number of edges
- Does not guarantee minimum travel cost when edge costs are different

---

## 4.2 Depth First Search (DFS)

DFS explores one branch as deeply as possible before backtracking.

It uses a **Stack (LIFO)** data structure.

### Characteristics:

- Uninformed search
- Explores one branch deeply before another
- Can use less memory than BFS in some cases
- Does not guarantee an optimal path

---

## 4.3 Greedy Best-First Search

Greedy Best-First Search uses a heuristic function to select the location that appears closest to the destination.

The evaluation function is:

**f(n) = h(n)**

where:

- **h(n)** = estimated cost from the current location to the destination

### Characteristics:

- Informed search
- Uses heuristic information
- Guides the search toward the destination
- Can reach the goal quickly
- Does not always guarantee the optimal path

---

## 4.4 A* Search

A* Search uses both the actual travel cost and the estimated cost to the destination.

The evaluation function is:

**f(n) = g(n) + h(n)**

where:

- **g(n)** = actual travel cost from the start
- **h(n)** = estimated cost from the current location to the destination
- **f(n)** = total estimated cost

### Characteristics:

- Informed search
- Uses both actual cost and heuristic
- Can find a minimum-cost route with a suitable heuristic
- More systematic than Greedy Best-First Search

---

## 4.5 Hill Climbing

Hill Climbing is a **Local Search** algorithm that selects a neighbouring location with a better heuristic value.

In this practical, the neighbouring location with the lowest heuristic value is selected.

### Characteristics:

- Local search algorithm
- Uses heuristic information
- Requires less memory
- Can be fast for simple problems
- May get stuck when no better neighbouring state is available

---

## 4.6 Tourist Day Scheduling using Backtracking

Backtracking is used to solve the tourist day scheduling problem as a **Constraint Satisfaction Problem (CSP)**.

The objective is to assign tourist locations to different time slots while satisfying the defined constraints.

### Tourist Activities:

- Gateway of India
- Sanjay Gandhi National Park
- Juhu Beach
- Marine Drive

### Time Slots:

- Morning
- Afternoon
- Evening
- Night

### Constraints:

1. Gateway of India must be scheduled in the Morning.
2. Sanjay Gandhi National Park must be scheduled in the Afternoon.
3. Juhu Beach and Marine Drive must not have the same time slot.
4. Each tourist activity must have a different time slot.

For this practical, Backtracking successfully generates a valid tourist schedule.

---

# 5. Tourist Locations and Heuristic Values

The program uses a manually defined graph containing tourist locations in Mumbai.

The tourist locations used are:

| Tourist Location |
|------------------|
| Gateway of India |
| Marine Drive |
| Chhatrapati Shivaji Maharaj Terminus |
| Elephanta Ferry |
| Juhu Beach |
| Siddhivinayak Temple |
| Bandra Fort |
| Sanjay Gandhi National Park |

The heuristic values used in the program are:

| Location | Heuristic h(n) |
|----------|---------------:|
| Gateway of India | 30 |
| Marine Drive | 28 |
| Chhatrapati Shivaji Maharaj Terminus | 27 |
| Elephanta Ferry | 32 |
| Juhu Beach | 22 |
| Siddhivinayak Temple | 20 |
| Bandra Fort | 15 |
| Sanjay Gandhi National Park | 0 |

The distances between tourist locations are manually defined in the program.

---

# 6. Performance Evaluation

The algorithms are evaluated using the following parameters:

| Parameter | Description |
|-----------|-------------|
| Path Found | Route obtained by the algorithm |
| Total Travel Cost | Total distance travelled |
| Nodes Explored | Number of nodes processed by the algorithm |
| Execution Time | Time required to execute the algorithm |

Execution time is measured using:

```python
time.perf_counter()
