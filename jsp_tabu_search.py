import random

def calculate_completion_time(solution):
    machines = set(machine for _, machine in solution)
    completion_times = [sum(duration for duration, m in solution if m == machine) for machine in machines]
    return max(completion_times)

def generate_initial_solution(job_durations, num_machines):
    machines = list(range(num_machines))
    machines_control = []
    done = False
    while done == False :
        initial_solution = [(duration, random.choice(machines)) for duration in job_durations]
        for s in initial_solution :
            if s[1] not in machines_control :
                machines_control.append(s[1])
        if len(machines_control) == num_machines or len(job_durations) < num_machines :
            done = True
        else :
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

def is_tabu(move, tabu_list):
    return move in tabu_list

def update_tabu_list(tabu_list, tabu_list_size):
    # Aggiorna la lista tabù rimuovendo la mossa più vecchia
    if len(tabu_list) >= tabu_list_size:
        tabu_list.pop(0)

def tabu_search(job_durations, num_machines, max_iterations, tabu_list_size):
    current_solution = generate_initial_solution(job_durations, num_machines)
    best_solution = current_solution
    tabu_list = []

    for iteration in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        feasible_neighbors = [neighbor for neighbor in neighbors if not is_tabu(neighbor, tabu_list)]

        if not feasible_neighbors:
            break

        # Trova il vicino migliore
        best_neighbor = min(feasible_neighbors, key=lambda x: calculate_completion_time(x))
        current_solution = best_neighbor

        # Aggiorna la lista tabù
        tabu_list.append(best_neighbor)
        update_tabu_list(tabu_list, tabu_list_size)

        # Aggiorna la migliore soluzione trovata finora
        if calculate_completion_time(current_solution) < calculate_completion_time(best_solution):
            best_solution = current_solution

    return best_solution

# # Esempio di utilizzo
# job_durations = [2, 1, 4]  # Durate dei job
# num_machines = 3  # Numero di macchine
# max_iterations = 10000  # Numero massimo di iterazioni
# tabu_list_size = 5  # Dimensione della lista tabù

# best_solution = tabu_search(job_durations, num_machines, max_iterations, tabu_list_size)
# print("Migliore soluzione:", best_solution)
# print("Tempo di completamento totale:", calculate_completion_time(best_solution))
