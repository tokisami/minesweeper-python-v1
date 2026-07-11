#Primer rebuild del buscaminas con el tablero estatico (6x6 con 3 bombas), luego se realizarala build con el tablero dinamico y despues con GUI

#Libreria random para el randomizer de las minas
import random

#Vamos a setear todas las variables

filas = 6
columnas = 6
minas = 3


def crearTablero():
    return [["." for _ in range(columnas)] for _ in range(filas)]

def agregarMinas(tablero, filaOk, columnaOk):
    colocadas = 0
    while colocadas < minas:
        x = random.randint(0, filas - 1)
        y = random.randint(0, columnas - 1)
        if tablero[x][y] == "*" or (x == filaOk and y == columnaOk):
            continue
        tablero[x][y] = "*"
        colocadas += 1

def contarVecinas(tablero, fila, col):
    contador = 0
    for df in (-1, 0, 1):
        for dc in (-1, 0, 1):
            x, y = fila + df, col + dc
            if (df, dc) != (0, 0) and 0 <= x < filas and 0 <= y < columnas:
                if tablero[x][y] == "*":
                    contador += 1
    return contador

def calcular_numeros(tablero_real):
    for f in range(filas):
        for c in range(columnas):
            if tablero_real[f][c] != "*":
                tablero_real[f][c] = contarVecinas(tablero_real, f, c)
 
 
def destapar(tablero_real, tablero_visible, fila, col):
    if tablero_visible[fila][col] != ".":
        return
    valor = tablero_real[fila][col]
    tablero_visible[fila][col] = valor
    if valor != 0:
        return
    for df in (-1, 0, 1):
        for dc in (-1, 0, 1):
            f, c = fila + df, col + dc
            if (df, dc) != (0, 0) and 0 <= f < filas and 0 <= c < columnas:
                destapar(tablero_real, tablero_visible, f, c)
 
 
def imprimir(tablero_visible):
    print("   " + " ".join(str(c) for c in range(columnas)))
    for f in range(filas):
        print(f, "|", " ".join(str(x) for x in tablero_visible[f]))
    print()
 
 
def hay_victoria(tablero_real, tablero_visible):
    for f in range(filas):
        for c in range(columnas):
            if tablero_real[f][c] != "*" and tablero_visible[f][c] == ".":
                return False
    return True
 
 
def buscaminas():
    tablero_real = crearTablero()
    tablero_visible = crearTablero()
    primera_jugada = True
 
    while True:
        imprimir(tablero_visible)
        fila, col = map(int, input("Fila y columna (ej: 2 3): ").split())
 
        if primera_jugada:
            agregarMinas(tablero_real, fila, col)
            calcular_numeros(tablero_real)
            primera_jugada = False
 
        if tablero_real[fila][col] == "*":
            tablero_visible[fila][col] = "*"
            imprimir(tablero_visible)
            print("Perdiste 💥")
            break
 
        destapar(tablero_real, tablero_visible, fila, col)
 
        if hay_victoria(tablero_real, tablero_visible):
            imprimir(tablero_visible)
            print("Ganaste 🎉")
            break
 
 
if __name__ == "__main__":
    buscaminas()