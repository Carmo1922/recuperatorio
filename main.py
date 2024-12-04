import menu
import random

# Función para inicializar la matriz
def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

# Función para cargar las notas de los participantes
def cargar_notas(matriz):
    for i in range(len(matriz)):
        print(f"Ingresando notas para el Participante {i + 1}")
        matriz[i][0] = i + 1  # Se guarda el numero del participante

        for j in range(3): #Se guarda el voto de los jurados para cada participante
            while True:
                try:
                    nota = int(input(f"Ingrese la nota del Jurado {j + 1} (1-100): "))
                    if 1 <= nota <= 100:
                        matriz[i][j + 1] = nota  
                        break
                    else:
                        print("Error: La nota debe estar entre 1 y 100. Intente de nuevo.")
                except ValueError:
                    print("\nError: Por favor ingrese un número válido.\n")

# Función para mostrar las notas y los promedios
def mostrar_votos(matriz):
    print("\nParticipantes y sus notas:")
    for i in range(len(matriz)):
        participante = matriz[i][0]
        nota1 = matriz[i][1]
        nota2 = matriz[i][2]
        nota3 = matriz[i][3]
        promedio = (nota1 + nota2 + nota3) / 3
        print(f"Participante {participante}: | Nota Jurado 1: {nota1} | Nota Jurado 2: {nota2} | Nota Jurado 3: {nota3} | Promedio: {promedio:.2f}")

# Función para ordenar los participantes por promedio
def ordenar_por_promedio(orden, matriz):
    promedios = [[i, (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3] for i in range(len(matriz))]
    for i in range(len(promedios) - 1):
        for j in range(i + 1, len(promedios)):
            if (orden == 'asc' and promedios[i][1] > promedios[j][1]) or (orden == 'desc' and promedios[i][1] < promedios[j][1]):
                promedios[i], promedios[j] = promedios[j], promedios[i]

    print("\nParticipantes ordenados por promedio:")
    for p in promedios:
        i = p[0]
        participante = matriz[i][0]
        promedio = p[1]
        print(f"Participante {participante}: Promedio: {promedio:.2f}")

# Función para mostrar los 3 peores participantes
def peores_3(matriz):
    promedios = [[i, (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3] for i in range(len(matriz))]
    for i in range(len(promedios) - 1):
        for j in range(i + 1, len(promedios)):
            if promedios[i][1] > promedios[j][1]:
                promedios[i], promedios[j] = promedios[j], promedios[i]

    print("\nPeores 3 participantes:")
    for i in range(3):
        idx = promedios[i][0]
        participante = matriz[idx][0]
        promedio = promedios[i][1]
        print(f"Participante {participante}: Promedio: {promedio:.2f}")

# Función para mostrar los participantes con un promedio mayor al promedio total
def mayores_promedio(matriz):
    total_promedio = sum((matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3 for i in range(len(matriz))) / len(matriz)
    print(f"\nPromedio total: {total_promedio:.2f}")
    print("Participantes con promedio mayor al total:")
    for i in range(len(matriz)):
        promedio = (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3
        if promedio > total_promedio:
            participante = matriz[i][0]
            print(f"Participante {participante}: Promedio: {promedio:.2f}")

# Función para determinar cuál jurado fue el peor
def jurado_malo(matriz):
    promedios_jurados = [0, 0, 0]  # Inicializamos los promedios de los tres jurados
    
    for i in range(5):  # Recorremos los 5 participantes
        promedios_jurados[0] += matriz[i][1] 
        promedios_jurados[1] += matriz[i][2]  
        promedios_jurados[2] += matriz[i][3]  
    
    # Dividimos cada suma entre el número de participantes (5)
    promedios_jurados[0] /= 5
    promedios_jurados[1] /= 5
    promedios_jurados[2] /= 5

    # Determinar el peor promedio manualmente
    peor_promedio = promedios_jurados[0]
    peor_jurado = 1
    for j in range(1, 3):
        if promedios_jurados[j] < peor_promedio:
            peor_promedio = promedios_jurados[j]
            peor_jurado = j + 1

    # Mostrar el resultado
    print("\nJurado(s) con la peor calificación promedio:")
    print(f"Jurado {peor_jurado}: Promedio: {peor_promedio:.2f}")

# Función para buscar participantes por la suma de sus tres notas
def suma_notas(matriz):
    suma = int(input("\nIngrese un número entre 3 y 300: "))
    if suma < 3 or suma > 300:
        print("Número fuera de rango.")
        return
    encontrado = False
    for i in range(len(matriz)):
        if matriz[i][1] + matriz[i][2] + matriz[i][3] == suma:
            participante = matriz[i][0]
            print(f"Participante {participante}: Suma de notas: {suma}")
            encontrado = True
    if not encontrado:
        print("No se encontraron participantes con esa suma de notas.")


def definir_ganador(matriz):
    indices = [0] * 5
    promedios = [0] * 5

    # Calcular los promedios de cada participante
    for i in range(5):
        promedio = (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3
        indices[i] = i  
        promedios[i] = promedio  

    mayor_promedio = promedios[0]
    for i in range(1, 5):
        if promedios[i] > mayor_promedio:
            mayor_promedio = promedios[i]

    ganadores = [0] * 5 
    numero_ganadores = 0
    for i in range(5):
        if promedios[i] == mayor_promedio:
            ganadores[numero_ganadores] = indices[i]
            numero_ganadores += 1

    # Mostrar los ganadores
    print(f"\nGanadores con el mejor promedio ({mayor_promedio:.2f}):")
    for g in range(numero_ganadores):
        print(f"Participante {matriz[ganadores[g]][0]}")

    # Manejo del desempate
    if numero_ganadores > 1:
        print("\nDesempate entre los ganadores:")
        votos = [0, 0, 0]  # Votos de los 3 jurados
        for j in range(3):  
            eleccion = int(input(f"Jurado {j + 1}, elija el número del participante ganador: "))
            # Validar elección
            while eleccion not in [matriz[ganadores[g]][0] for g in range(numero_ganadores)]:
                print("Participante no válido. Elija entre los ganadores.")
                eleccion = int(input(f"Jurado {j + 1}, elija el número del participante ganador: "))
            votos[j] = eleccion

        votos_contados = [0] * 5 

        for voto in votos:
            for g in range(numero_ganadores):
                if voto == matriz[ganadores[g]][0]:
                    votos_contados[ganadores[g]] += 1

        # Encontrar al participante con más votos
        max_votos = votos_contados[ganadores[0]]  # Empezamos con el primer ganador
        ganador_final = ganadores[0]

        for g in range(1, numero_ganadores):
            if votos_contados[ganadores[g]] > max_votos:
                max_votos = votos_contados[ganadores[g]]
                ganador_final = ganadores[g]

        
        posibles_ganadores = [g for g in range(numero_ganadores) if votos_contados[ganadores[g]] == max_votos]

        if len(posibles_ganadores) == 1:
            print(f"\nEl ganador final es el Participante {matriz[ganadores[posibles_ganadores[0]]][0]}")
        else:
            ganador_final = random.choice(posibles_ganadores)  # Desempate aleatorio
            print(f"\nEl ganador final (por sorteo) es el Participante {matriz[ganadores[posibles_ganadores[0]]][0]}")
    else:
        print("El ganador es único y no requiere desempate.")





# Función principal
def main():
    matriz = inicializar_matriz(5, 4, 0)
    cargar_notas(matriz)
    

    while True:
        menu.mostrar_menu()
        opcion = input("Su opción: ")
        if opcion == "1":
            mostrar_votos(matriz)
        elif opcion == "2":
            orden = input("Ingrese 'asc' para ascendente o 'desc' para descendente: ")
            ordenar_por_promedio(orden, matriz)
        elif opcion == "3":
            peores_3(matriz)
        elif opcion == "4":
            mayores_promedio(matriz)
        elif opcion == "5":
            jurado_malo(matriz)
        elif opcion == "6":
            suma_notas(matriz)
        elif opcion == "7":
            definir_ganador(matriz)
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("\nOpción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
