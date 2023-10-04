from collections import deque

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def round_robin(processes, quantum):
    n = len(processes)
    queue = deque(processes)
    time = 0
    waiting_time = [0] * n

    while queue:
        process = queue.popleft()
        if process.burst_time <= quantum:
            # El proceso se ejecuta completamente antes de que expire el quantum.
            time += process.burst_time
            waiting_time[process.name] = time - process.arrival_time - process.burst_time
        else:
            # El proceso se ejecuta durante el quantum y luego se encola nuevamente.
            time += quantum
            process.burst_time -= quantum
            queue.append(process)

    total_waiting_time = sum(waiting_time)
    average_waiting_time = total_waiting_time / n
    return average_waiting_time

if __name__ == "__main__":
    # Definir los procesos con formato (nombre, tiempo de llegada, tiempo de ejecución)
    processes = [Process(0, 0, 4), Process(1, 1, 3), Process(2, 2, 1), Process(3, 3, 2)]
    quantum = 2

    average_wait_time = round_robin(processes, quantum)
    print("Tiempo promedio de espera:", average_wait_time)