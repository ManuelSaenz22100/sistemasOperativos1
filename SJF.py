class Proceso:
    def __init__(self, nombre, tiempo_llegada, tiempo_ejecucion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion

def planificacion_sjf(procesos):
    tiempo_actual = 0
    procesos_ordenados = sorted(procesos, key=lambda x: x.tiempo_ejecucion)
    tiempo_espera_total = 0

    for proceso in procesos_ordenados:
        if tiempo_actual < proceso.tiempo_llegada:
            tiempo_actual = proceso.tiempo_llegada
        tiempo_espera = tiempo_actual - proceso.tiempo_llegada
        tiempo_espera_total += tiempo_espera
        tiempo_actual += proceso.tiempo_ejecucion

        print(f"Proceso {proceso.nombre}: Tiempo de llegada = {proceso.tiempo_llegada}, Tiempo de espera = {tiempo_espera}, Tiempo de finalización = {tiempo_actual}")

    tiempo_promedio_espera = tiempo_espera_total / len(procesos)
    print(f"Tiempo promedio de espera = {tiempo_promedio_espera}")

if __name__ == "__main__":
    procesos = [
        Proceso("P1", 0, 6),
        Proceso("P2", 1, 8),
        Proceso("P3", 2, 7),
        Proceso("P4", 3, 3)
    ]

    print("Planificación SJF:")
    planificacion_sjf(procesos)
