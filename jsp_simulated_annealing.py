import random
import math

def calculate_completion_time(solution):
    machines = set(machine for _, machine in solution)
    completion_times = [sum(duration for duration, m in solution if m == machine) for machine in machines]
    return max(completion_times)

def generate_initial_solution(job_durations, num_machines):
    machines = list(range(num_machines))
    machines_control = []
    done = False
    while not done:
        initial_solution = [(duration, random.choice(machines)) for duration in job_durations]
        for s in initial_solution:
            if s[1] not in machines_control:
                machines_control.append(s[1])
        if len(machines_control) == num_machines or len(job_durations) < num_machines:
            done = True
        else:
            initial_solution.clear()
            machines_control.clear()
    return initial_solution

def generate_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()

            first_change = (neighbor[i][0], neighbor[j][1])
            second_change = (neighbor[j][0], neighbor[i][1])
            old_tuple1 = neighbor[i]
            old_tuple2 = neighbor[j]
            neighbor.remove(old_tuple1)
            neighbor.remove(old_tuple2)
            neighbor.append(first_change)
            neighbor.append(second_change)
            neighbors.append(neighbor)
    return neighbors

def acceptance_probability(delta_E, temperature):
    if delta_E < 0:
        return 1.0
    return math.exp(-delta_E / temperature)

def simulated_annealing(job_durations, num_machines, max_iterations, initial_temperature, cooling_rate):
    current_solution = generate_initial_solution(job_durations, num_machines)
    best_solution = current_solution.copy()

    temperature = initial_temperature

    for iteration in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        neighbor = min(neighbors, key=lambda x: calculate_completion_time(x))
        current_cost = calculate_completion_time(current_solution)
        neighbor_cost = calculate_completion_time(neighbor)

        delta_E = neighbor_cost - current_cost

        if delta_E < 0 or random.random() < acceptance_probability(delta_E, temperature):
            current_solution = neighbor

        if calculate_completion_time(current_solution) < calculate_completion_time(best_solution):
            best_solution = current_solution

        temperature *= cooling_rate

    return best_solution

# Esempio di utilizzo:
# job_durations = [3, 4, 2, 5, 3]
# num_machines = 3
# max_iterations = 1000
# initial_temperature = 1000
# cooling_rate = 0.95

# best_solution = simulated_annealing(job_durations, num_machines, max_iterations, initial_temperature, cooling_rate)
# print("Best solution:", best_solution)
# print("Completion time:", calculate_completion_time(best_solution))
