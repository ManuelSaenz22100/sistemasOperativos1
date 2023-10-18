def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    total_waiting_time = 0

    for i in range(1, n):
        waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1]
        total_waiting_time += waiting_time[i]

    average_waiting_time = total_waiting_time / n
    return average_waiting_time

if __name__ == "__main__":
    # Definir los procesos con formato (tiempo de llegada, tiempo de ejecución)
    processes = [(0, 6), (1, 4), (2, 8)]

    average_wait_time = fcfs(processes)
    print("Tiempo promedio de espera:", average_wait_time)