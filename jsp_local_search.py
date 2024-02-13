import random

def calculate_completion_time(solution):
    # Calcola il tempo di completamento totale sommando le durate dei job su ogni macchina
    machines = set(machine for _, machine in solution)
    completion_times = [sum(duration for duration, m in solution if m == machine) for machine in machines]
    return max(completion_times)

def generate_initial_solution(job_durations, num_machines):
    machines = list(range(num_machines))
    machines_control = []   #check all the machines at least one job
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

def local_search(job_durations, num_machines, max_iterations):
    current_solution = generate_initial_solution(job_durations, num_machines)
    best_solution = current_solution

    for iteration in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        
        # Trova il primo vicino che migliora la soluzione corrente
        for neighbor in neighbors:
            if calculate_completion_time(neighbor) < calculate_completion_time(current_solution):
                current_solution = neighbor
                break

        # Aggiorna la migliore soluzione trovata finora
        if calculate_completion_time(current_solution) < calculate_completion_time(best_solution):
            best_solution = current_solution

    return best_solution

# # Esempio di utilizzo
# job_durations = [2, 1, 4, 3, 7, 4, 1]  # Durate dei job
# num_machines = 3  # Numero di macchine
# max_iterations = 10000  # Numero massimo di iterazioni

# best_solution = local_search(job_durations, num_machines, max_iterations)
# print("Migliore soluzione:", best_solution)
# print("Tempo di completamento totale:", calculate_completion_time(best_solution))
