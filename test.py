import random, time
import matplotlib.pyplot as plt
from jsp_tabu_search import *
from jsp_local_search import *
from jsp_simulated_annealing import *
import numpy as np

def genera_lista_jobs(n, valore_massimo, valore_minimo):
    return [random.randint(valore_minimo, valore_massimo) for _ in range(n)]

def lower_bound_generator(jobs, num_machines) :
    tot = 0
    for j in jobs :
        tot = tot + j
    return tot/num_machines

with open("output.txt", "w") as file:
    print("file aperto")
    for i in range(10) :
        print(i)
        print("TEST", i, file=file)
        print(" ", file=file)
        # Esempio di utilizzo
        job_durations = genera_lista_jobs(100, 10, 1)  # Durate dei job
        num_machines = 3  # Numero di macchine
        lower_bound = lower_bound_generator(job_durations, num_machines)
        max_iterations = 1000
        tabu_list_size = 5  # Dimensione della lista tabù
        # Registra il tempo di inizio
        tempo_inizio = time.time()
        best_solution = tabu_search(job_durations, num_machines, max_iterations, tabu_list_size)
        # Registra il tempo di fine
        tempo_fine = time.time()
        tempo_totale = tempo_fine - tempo_inizio
        print("TABU", file=file)
        print("Migliore soluzione:", best_solution, file=file)
        print("Tempo di completamento totale:", calculate_completion_time(best_solution), file=file)
        print("tempo di esecuzione: ", tempo_totale, file=file)
        print("Lower bound:", lower_bound, file=file)
        # Registra il tempo di inizio
        tempo_inizio = time.time()
        best_solution = local_search(job_durations, num_machines, max_iterations)
        # Registra il tempo di fine
        tempo_fine = time.time()
        tempo_totale = tempo_fine - tempo_inizio
        print("LOCAL", file=file)
        print("Migliore soluzione:", best_solution, file=file)
        print("Tempo di completamento totale:", calculate_completion_time(best_solution), file=file)
        print("tempo di esecuzione: ", tempo_totale, file=file)
        print("Lower bound:", lower_bound, file=file)
        initial_temperature = 1000
        cooling_rate = 0.95
        # Registra il tempo di inizio
        tempo_inizio = time.time()
        best_solution = simulated_annealing(job_durations, num_machines, max_iterations, initial_temperature, cooling_rate)
        # Registra il tempo di fine
        tempo_fine = time.time()
        tempo_totale = tempo_fine - tempo_inizio
        print("SIMULATED", file=file)
        print("Migliore soluzione:", best_solution, file=file)
        print("Tempo di completamento totale:", calculate_completion_time(best_solution), file=file)
        print("tempo di esecuzione: ", tempo_totale, file=file)
        print("Lower bound:", lower_bound, file=file)
        print(" ", file=file)
        print(" ", file=file)

# Calcola il tempo totale trascorso

#Dizionario per memorizzare la somma dei valori per ciascuna chiave
# sum_dict = {}

# for value, key in best_solution:
#     if key in sum_dict:
#         sum_dict[key] += value
#     else:
#         sum_dict[key] = value

# # Estrai chiavi e valori dal dizionario
# keys = list(sum_dict.keys())
# values = list(sum_dict.values())

# # Crea il grafico a barre
# plt.bar(keys, values)

# # Imposta i ticks dell'asse x come numeri interi
# plt.xticks(np.arange(0, len(keys), step=1), keys.sort())

# # Aggiungi etichette
# plt.xlabel('# macchina')
# plt.ylabel('Tempo in secondi')
# plt.title('scheduling parallelo su 3 macchine')

# # Mostra il grafico
# plt.show()