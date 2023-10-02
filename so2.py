print("Sistemas Operativos")
def ingresar_procesos():
    n = int(input("Ingrese el número de procesos: "))
    procesos = []

    for i in range(n):
        proceso = {}
        proceso['id'] = str(input(f"Ingrese el ID del proceso {i + 1}: "))
        proceso['ArrivalTime'] = int(input(f"Ingrese Arrival Time para el proceso {i + 1}: "))
        proceso['BurstTime'] = int(input(f"Ingrese Burst Time para el proceso {i + 1}: "))
        procesos.append(proceso)
    return procesos

def calcular_turnaround_waiting_time(procesos):
    n = len(procesos)
    tiempo_actual = 0
    turnaround_times = []
    waiting_times = []

    for proceso in procesos:
        if tiempo_actual < proceso['ArrivalTime']:
            tiempo_actual = proceso['ArrivalTime']

        turnaround_time = tiempo_actual + proceso['BurstTime'] - proceso['ArrivalTime']
        waiting_time = turnaround_time - proceso['BurstTime']

        turnaround_times.append(turnaround_time)
        waiting_times.append(waiting_time)

        tiempo_actual += proceso['BurstTime']

    return turnaround_times, waiting_times

def mostrar_turnaround_waiting_time(procesos, turnaround_times, waiting_times):
    print("\nID\tArrival Time\tBurst Time\tTurnaround Time\tWaiting Time")
    for i, proceso in enumerate(procesos):
        print(f"{proceso['id']}\t{proceso['ArrivalTime']}\t\t{proceso['BurstTime']}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")

if __name__ == "__main__":
    print("Turnaround Time y Waiting Time")
    procesos = ingresar_procesos()
    turnaround_times, waiting_times = calcular_turnaround_waiting_time(procesos)

    print("\nTurnaround Time y Waiting Time de los procesos:")
    mostrar_turnaround_waiting_time(procesos, turnaround_times, waiting_times)