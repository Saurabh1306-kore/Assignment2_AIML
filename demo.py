import time
import heapq
from collections import deque

graph = {
    "Gateway of India": {
        "Marine Drive": 5,
        "Chhatrapati Shivaji Maharaj Terminus": 4,
        "Elephanta Ferry": 2
    },

    "Marine Drive": {
        "Gateway of India": 5,
        "Juhu Beach": 15,
        "Siddhivinayak Temple": 8
    },

    "Chhatrapati Shivaji Maharaj Terminus": {
        "Gateway of India": 4,
        "Siddhivinayak Temple": 7,
        "Bandra Fort": 12
    },

    "Elephanta Ferry": {
        "Gateway of India": 2
    },

    "Juhu Beach": {
        "Marine Drive": 15,
        "Bandra Fort": 6
    },

    "Siddhivinayak Temple": {
        "Marine Drive": 8,
        "Chhatrapati Shivaji Maharaj Terminus": 7,
        "Bandra Fort": 5
    },

    "Bandra Fort": {
        "Juhu Beach": 6,
        "Siddhivinayak Temple": 5,
        "Chhatrapati Shivaji Maharaj Terminus": 12,
        "Sanjay Gandhi National Park": 25
    },

    "Sanjay Gandhi National Park": {
        "Bandra Fort": 25
    }
}

heuristic = {
    "Gateway of India": 30,
    "Marine Drive": 28,
    "Chhatrapati Shivaji Maharaj Terminus": 27,
    "Elephanta Ferry": 32,
    "Juhu Beach": 22,
    "Siddhivinayak Temple": 20,
    "Bandra Fort": 15,
    "Sanjay Gandhi National Park": 0
}

def print_result(name, path, cost, nodes, execution_time):
    """Display the result of a search algorithm."""

    print("\n" + "-" * 70)
    print("Algorithm:", name)

    if path is not None:
        print("Route:", " -> ".join(path))
        print("Total Travel Cost:", cost, "km")
    else:
        print("Route: No route found")

    print("Nodes Explored:", nodes)
    print("Execution Time:", f"{execution_time:.8f}", "seconds")

def bfs(start, goal):
    """
    BFS explores the graph level by level.
    It finds a route with the minimum number of edges.
    """

    queue = deque([(start, [start])])
    visited = {start}
    nodes_explored = 0

    while queue:

        current, path = queue.popleft()
        nodes_explored += 1

        if current == goal:

            cost = 0

            for i in range(len(path) - 1):
                cost += graph[path[i]][path[i + 1]]

            return path, cost, nodes_explored

        for neighbour in graph[current]:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append(
                    (neighbour, path + [neighbour])
                )

    return None, 0, nodes_explored

def dfs(start, goal):
    """
    DFS explores one branch deeply before backtracking.
    """

    stack = [(start, [start])]
    visited = set()
    nodes_explored = 0

    while stack:

        current, path = stack.pop()
        nodes_explored += 1

        if current == goal:

            cost = 0

            for i in range(len(path) - 1):
                cost += graph[path[i]][path[i + 1]]

            return path, cost, nodes_explored

        if current in visited:
            continue

        visited.add(current)
        neighbours = list(graph[current].keys())
        neighbours.reverse()

        for neighbour in neighbours:

            if neighbour not in visited:

                stack.append(
                    (neighbour, path + [neighbour])
                )

    return None, 0, nodes_explored

def greedy_best_first(start, goal):
    """
    Greedy Best-First Search selects the location
    having the smallest heuristic value.
    """

    priority_queue = [
        (heuristic[start], start, [start], 0)
    ]

    visited = set()
    nodes_explored = 0

    while priority_queue:

        h_value, current, path, cost = heapq.heappop(
            priority_queue
        )

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        # Goal test
        if current == goal:
            return path, cost, nodes_explored

        for neighbour, distance in graph[current].items():

            if neighbour not in visited:

                heapq.heappush(
                    priority_queue,
                    (
                        heuristic[neighbour],
                        neighbour,
                        path + [neighbour],
                        cost + distance
                    )
                )

    return None, 0, nodes_explored

def a_star(start, goal):
    """
    A* uses:

        f(n) = g(n) + h(n)

    g(n) = actual cost from start
    h(n) = estimated cost to goal
    f(n) = total estimated cost
    """

    priority_queue = [
        (heuristic[start], 0, start, [start])
    ]

    best_cost = {
        start: 0
    }

    nodes_explored = 0

    while priority_queue:

        f_value, current_cost, current, path = heapq.heappop(
            priority_queue
        )

        nodes_explored += 1

        if current_cost > best_cost.get(current, float("inf")):
            continue

        if current == goal:
            return path, current_cost, nodes_explored
        for neighbour, distance in graph[current].items():

            new_cost = current_cost + distance

            if new_cost < best_cost.get(
                    neighbour,
                    float("inf")
            ):

                best_cost[neighbour] = new_cost

                new_f = (
                    new_cost +
                    heuristic[neighbour]
                )

                heapq.heappush(
                    priority_queue,
                    (
                        new_f,
                        new_cost,
                        neighbour,
                        path + [neighbour]
                    )
                )

    return None, 0, nodes_explored

def hill_climbing(start, goal):
    """
    Hill Climbing selects the neighbouring location
    having a lower heuristic value.

    The algorithm stops when:
    - Goal is reached, OR
    - No better neighbouring location exists.
    """

    current = start
    path = [current]
    cost = 0
    nodes_explored = 0
    visited = {current}

    while current != goal:

        nodes_explored += 1

        neighbours = []

        for neighbour, distance in graph[current].items():

            if neighbour not in visited:

                neighbours.append(
                    (
                        heuristic[neighbour],
                        neighbour,
                        distance
                    )
                )
        if not neighbours:

            return None, 0, nodes_explored
        neighbours.sort()

        best_h, next_city, distance = neighbours[0]

        if best_h >= heuristic[current]:

            return None, 0, nodes_explored

        current = next_city

        visited.add(current)

        path.append(current)

        cost += distance

    nodes_explored += 1

    return path, cost, nodes_explored

activities = [
    "Gateway of India",
    "Sanjay Gandhi National Park",
    "Juhu Beach",
    "Marine Drive"
]

time_slots = [
    "Morning",
    "Afternoon",
    "Evening",
    "Night"
]


def is_schedule_valid(schedule):
    """
    Check whether all constraints are satisfied.
    """

    # Constraint 1
    if (
        "Gateway of India" in schedule
        and schedule["Gateway of India"] != "Morning"
    ):
        return False

    # Constraint 2
    if (
        "Sanjay Gandhi National Park" in schedule
        and schedule["Sanjay Gandhi National Park"] != "Afternoon"
    ):
        return False

    # Constraint 3
    if (
        "Juhu Beach" in schedule
        and "Marine Drive" in schedule
    ):
        if (
            schedule["Juhu Beach"]
            == schedule["Marine Drive"]
        ):
            return False

    # Constraint 4
    assigned_slots = list(schedule.values())

    if len(assigned_slots) != len(set(assigned_slots)):
        return False

    return True


def solve_tourist_schedule():
    """
    Solve the Tourist Schedule CSP using Backtracking.
    """

    schedule = {}
    nodes_explored = 0

    def backtrack(index):

        nonlocal nodes_explored

        nodes_explored += 1

        # All activities assigned
        if index == len(activities):
            return True

        activity = activities[index]

        for slot in time_slots:

            schedule[activity] = slot

            if is_schedule_valid(schedule):

                if backtrack(index + 1):
                    return True

            # Backtrack
            del schedule[activity]

        return False

    start_time = time.perf_counter()

    solved = backtrack(0)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    if solved:
        return (
            schedule.copy(),
            nodes_explored,
            execution_time
        )

    return (
        None,
        nodes_explored,
        execution_time
    )

def run_search_test(name, algorithm, start, goal):
    """
    Run an algorithm and measure execution time.
    """

    start_time = time.perf_counter()

    path, cost, nodes = algorithm(
        start,
        goal
    )

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    print_result(
        name,
        path,
        cost,
        nodes,
        execution_time
    )

    return {
        "algorithm": name,
        "path": path,
        "cost": cost,
        "nodes": nodes,
        "time": execution_time
    }

def main():

    start_location = "Gateway of India"
    goal_location = "Sanjay Gandhi National Park"

    print("=" * 70)
    print("AI-BASED TOURIST ROUTE AND TRIP PLANNING SYSTEM")
    print("=" * 70)

    print("\nStart Location:",
          start_location)

    print("Destination:",
          goal_location)

    print("\nSEARCH ALGORITHM RESULTS")

    results = []

    results.append(
        run_search_test(
            "Breadth First Search",
            bfs,
            start_location,
            goal_location
        )
    )

    results.append(
        run_search_test(
            "Depth First Search",
            dfs,
            start_location,
            goal_location
        )
    )

    results.append(
        run_search_test(
            "Greedy Best First Search",
            greedy_best_first,
            start_location,
            goal_location
        )
    )

    results.append(
        run_search_test(
            "A* Search",
            a_star,
            start_location,
            goal_location
        )
    )

    results.append(
        run_search_test(
            "Hill Climbing",
            hill_climbing,
            start_location,
            goal_location
        )
    )

    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON")
    print("=" * 70)

    print(
        f"{'Algorithm':<30}"
        f"{'Cost(km)':<12}"
        f"{'Nodes':<10}"
        f"{'Time(s)':<15}"
    )

    print("-" * 70)

    for result in results:

        cost_text = (
            str(result["cost"])
            if result["path"] is not None
            else "N/A"
        )

        print(
            f"{result['algorithm']:<30}"
            f"{cost_text:<12}"
            f"{result['nodes']:<10}"
            f"{result['time']:.8f}"
        )

    print("\n" + "=" * 70)
    print("CONSTRAINT SATISFACTION - TOURIST DAY SCHEDULE")
    print("=" * 70)

    schedule, nodes, execution_time = (
        solve_tourist_schedule()
    )

    if schedule:

        print("\nValid Tourist Schedule:")

        for activity in activities:

            print(
                f"{schedule[activity]:<12}"
                f" : {activity}"
            )

        print(
            "\nNodes Explored:",
            nodes
        )

        print(
            "Execution Time:",
            f"{execution_time:.8f}",
            "seconds"
        )

        print(
            "\nStatus: Valid schedule found"
        )

    else:

        print(
            "\nNo valid schedule found."
        )

    print("\n" + "=" * 70)
    print("FINAL OBSERVATION")
    print("=" * 70)

    print(
        "BFS searches level by level and finds a route "
        "with minimum number of edges."
    )

    print(
        "DFS explores one branch deeply before "
        "backtracking."
    )

    print(
        "Greedy Best First Search uses heuristic "
        "information to select promising locations."
    )

    print(
        "A* combines actual travel cost and heuristic "
        "information using f(n) = g(n) + h(n)."
    )

    print(
        "Hill Climbing moves toward a neighbouring "
        "location with a better heuristic value."
    )

    print(
        "Backtracking finds a valid tourist schedule "
        "while satisfying all constraints."
    )

if __name__ == "__main__":
    main()