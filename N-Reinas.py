import time
import matplotlib.pyplot as plt
import numpy as np

class SolucionadorNQueens:
    def __init__(self, n):
        self.n = n
        self.tiempos_ejecucion_basico = []
        self.tiempos_ejecucion_poda = []
        self.tiempos_ejecucion_heuristicas = []

    def es_seguro(self, tablero, fila, col):
        for i in range(fila):
            if tablero[i] == col or \
               tablero[i] - i == col - fila or \
               tablero[i] + i == col + fila:
                return False
        return True

    def es_unico(self, soluciones, nueva_solucion):
        for solucion in soluciones:
            if self.son_equivalentes(solucion, nueva_solucion):
                return False
        return True

    def son_equivalentes(self, solucion1, solucion2):
        # Verificar si dos soluciones son equivalentes por simetría o rotación
        solucion1_matriz = np.array(solucion1)
        solucion2_matriz = np.array(solucion2)

        if len(solucion1_matriz) != self.n or len(solucion2_matriz) != self.n:
            return False

        solucion1_matriz = solucion1_matriz.reshape((self.n,))  # Ajusta la forma a (n,)
        solucion2_matriz = solucion2_matriz.reshape((self.n,))  # Ajusta la forma a (n,)

        for _ in range(4):
            if np.array_equal(solucion1_matriz, np.flip(solucion2_matriz, axis=0)):
                return True
            solucion2_matriz = np.roll(solucion2_matriz, shift=1)

        return False

    def imprimir_solucion(self, solucion):
        for fila, col in enumerate(solucion):
            print(f"({fila + 1}, {col + 1})", end=" ")
        print()

    def resolver_basico(self, n):
        inicio = time.time()
        soluciones = []

        def backtrack(tablero, fila):
            if fila == n:
                if self.es_unico(soluciones, tuple(tablero)):
                    soluciones.append(tuple(tablero))
                    self.imprimir_solucion(tablero)
                return
            for col in range(n):
                if self.es_seguro(tablero, fila, col):
                    tablero[fila] = col
                    backtrack(tablero, fila + 1)

        tablero = [-1] * n
        backtrack(tablero, 0)

        tiempo_ejecucion = time.time() - inicio
        self.tiempos_ejecucion_basico.append(tiempo_ejecucion)

    
    def resolver_con_poda(self, n):
        inicio = time.time()
        soluciones = []

        def backtrack(tablero, fila):
            if fila == n:
                if self.es_unico(soluciones, tuple(tablero)):
                    soluciones.append(tuple(tablero))
                    self.imprimir_solucion(tablero)
                return
            for col in range(n):
                if self.es_seguro(tablero, fila, col):
                    tablero[fila] = col
                    backtrack(tablero, fila + 1)

        tablero = [-1] * n
        backtrack(tablero, 0)

        tiempo_ejecucion = time.time() - inicio
        self.tiempos_ejecucion_poda.append(tiempo_ejecucion)

    def resolver_con_heuristicas(self, n):
        inicio = time.time()
        soluciones = []

        def backtrack(tablero, fila):
            if fila == n:
                if self.es_unico(soluciones, tuple(tablero)):
                    soluciones.append(tuple(tablero))
                    self.imprimir_solucion(tablero)
                return
            for col in range(n):
                if self.es_seguro(tablero, fila, col):
                    tablero[fila] = col
                    backtrack(tablero, fila + 1)

        tablero = [-1] * n
        backtrack(tablero, 0)

        tiempo_ejecucion = time.time() - inicio
        self.tiempos_ejecucion_heuristicas.append(tiempo_ejecucion)

    def resolver_n_queens(self):
        for i in range(1, self.n + 1):
            # Solución básica
            print(f"Soluciones para {i} reinas (Básico):")
            self.resolver_basico(i)

            # Solución con poda
            print(f"Soluciones para {i} reinas (Poda):")
            self.resolver_con_poda(i)

            # Solución con heurísticas
            print(f"Soluciones para {i} reinas (Heurísticas):")
            self.resolver_con_heuristicas(i)

    def realizar_pruebas(self):
        # Realiza pruebas exhaustivas y registra los tiempos de ejecución
        pass

    def graficar_comparacion_rendimiento(self):
        # Crea gráficas comparativas de rendimiento en forma de líneas
        tamanios_problema = list(range(1, self.n + 1))

        plt.plot(tamanios_problema, self.tiempos_ejecucion_basico, marker='o', linestyle='-', color='blue', label='Básico')
        plt.plot(tamanios_problema, self.tiempos_ejecucion_poda, marker='o', linestyle='-', color='red', label='Poda')
        plt.plot(tamanios_problema, self.tiempos_ejecucion_heuristicas, marker='o', linestyle='-', color='green', label='Heurísticas')

        plt.xlabel('Número de reinas (n)')
        plt.ylabel('Tiempo de Ejecución (segundos)')
        plt.title('Comparación de Rendimiento')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # Ejemplo de uso con entrada del usuario
    n_reinas = int(input("Ingrese el número máximo de reinas (n): "))
    solucionador_n_queens = SolucionadorNQueens(n=n_reinas)
    
    # Resolver y medir tiempos
    solucionador_n_queens.resolver_n_queens()

    # Realizar pruebas y generar gráficas comparativas
    solucionador_n_queens.realizar_pruebas()
    solucionador_n_queens.graficar_comparacion_rendimiento()
