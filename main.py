import menu  # Importamos el archivo menu.py

# Función para inicializar la matriz
def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]  # Usamos += solo en la inicialización
    return matriz

# Función para cargar las notas de los participantes
def cargar_notas(matriz):
    for i in range(len(matriz)):  # Iterar sobre los participantes
        print(f"Ingresando notas para el Participante {i + 1}")
        matriz[i][0] = i + 1  # Asignar el número del participante

        for j in range(3):  # 3 jurados
            while True:
                try:
                    nota = int(input(f"Ingrese la nota del Jurado {j + 1} (1-100): "))
                    if 1 <= nota <= 100:
                        matriz[i][j + 1] = nota  # Asignar la nota en la posición correspondiente
                        break
                    else:
                        print("Error: La nota debe estar entre 1 y 100. Intente de nuevo.")
                except ValueError:
                    print("Error: Por favor ingrese un número válido.")

# Función para mostrar las notas y los promedios
def mostrar_votos(matriz):
    print("\nParticipantes y sus notas:")
    for i in range(len(matriz)):
        participante = matriz[i][0]
        nota1 = matriz[i][1]
        nota2 = matriz[i][2]
        nota3 = matriz[i][3]
        promedio = (nota1 + nota2 + nota3) / 3
        print(f"Participante {participante}: Nota Jurado 1: {nota1}, Nota Jurado 2: {nota2}, Nota Jurado 3: {nota3}, Promedio: {promedio:.2f}")

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
    promedios_jurados = [
        sum(matriz[i][1] for i in range(len(matriz))) / len(matriz),
        sum(matriz[i][2] for i in range(len(matriz))) / len(matriz),
        sum(matriz[i][3] for i in range(len(matriz))) / len(matriz)
    ]
    minimo = min(promedios_jurados)
    print("\nJurado(s) con la peor calificación promedio:")
    for i, promedio in enumerate(promedios_jurados):
        if promedio == minimo:
            print(f"Jurado {i + 1}: Promedio: {promedio:.2f}")

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

# Función para definir al ganador de la competencia
def definir_ganador(matriz):
    promedios = [[i, (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3] for i in range(len(matriz))]
    mayor_promedio = max(p[1] for p in promedios)
    ganadores = [p[0] for p in promedios if p[1] == mayor_promedio]

    print(f"\nGanadores con el mejor promedio ({mayor_promedio:.2f}):")
    for g in ganadores:
        print(f"Participante {matriz[g][0]}")

    if len(ganadores) > 1:
        print("\nDesempate entre los ganadores:")
        votos = [0, 0, 0]
        for j in range(3):
            eleccion = int(input(f"Jurado {j + 1}, elija el número del participante ganador: "))
            while eleccion not in [matriz[g][0] for g in ganadores]:
                print("Participante no válido. Elija entre los ganadores.")
                eleccion = int(input(f"Jurado {j + 1}, elija el número del participante ganador: "))
            votos[j] = eleccion

        ganador_final = max(set(votos), key=votos.count)
        print(f"\nEl ganador final es el Participante {ganador_final}")
    else:
        print("El ganador es único y no requiere desempate.")

# Función principal
def main():
    matriz = inicializar_matriz(5, 4, 0)
    cargar_notas(matriz)
    mostrar_votos(matriz)

    while True:
        menu.mostrar_menu()
        opcion = input("Opción: ")
        if opcion == "1":
            orden = input("Ingrese 'asc' para ascendente o 'desc' para descendente: ")
            ordenar_por_promedio(orden, matriz)
        elif opcion == "2":
            peores_3(matriz)
        elif opcion == "3":
            mayores_promedio(matriz)
        elif opcion == "4":
            jurado_malo(matriz)
        elif opcion == "5":
            suma_notas(matriz)
        elif opcion == "6":
            definir_ganador(matriz)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
