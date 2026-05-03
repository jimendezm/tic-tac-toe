# Semana 5 - Minimax (Tic Tac Toe)

En esta semana se implementa el algoritmo **Minimax** aplicado al juego Tic Tac Toe.

---

## Descripción

Minimax permite tomar decisiones óptimas en juegos de dos jugadores.
La idea es que:

* **X** intenta maximizar el resultado
* **O (IA)** intenta minimizarlo

El algoritmo evalúa todos los posibles movimientos y elige el mejor.

Valores:

* `1` → gana X
* `-1` → gana O
* `0` → empate

---

## Interfaz

Se hizo una interfaz con **Pygame** donde:

* El usuario juega como **X**
* La IA juega automáticamente como **O**
* Se puede reiniciar la partida

---

## Archivos

* `minimax.py`: lógica del algoritmo
* `utils.py`: funciones auxiliares
* `minimax_ui.py`: interfaz gráfica

---

## Cómo ejecutar

Instalar pygame:

```
pip install pygame
```

Ejecutar:

```
python minimax_ui.py
```

---

# Semana 8 - Alpha-Beta Pruning (Tic Tac Toe)

En esta semana se implementa el algoritmo **Alpha-Beta Pruning** como una optimización de Minimax aplicada al mismo juego Tic Tac Toe.

---

## Descripción

Alpha-Beta Pruning mejora Minimax eliminando ramas del árbol de búsqueda que no pueden influir en la decisión final, reduciendo el número de nodos evaluados sin alterar el resultado óptimo.

La idea es que:

* **Alpha** representa el mejor valor que puede garantizar el jugador maximizador (X)
* **Beta** representa el mejor valor que puede garantizar el jugador minimizador (O)
* Si `alpha >= beta`, se poda la rama (no se evalúa más)

Valores:

* `1` → gana X
* `-1` → gana O
* `0` → empate

---

## Interfaz

Se hizo una interfaz de **consola** donde:

* El usuario elige si jugar como **X** (primero) o **O** (segundo)
* La IA juega automáticamente usando Alpha-Beta Pruning
* Se puede volver a jugar al terminar la partida

---

## Archivos

* `alpha_beta_pruning.py`: lógica del algoritmo
* `utils.py`: funciones auxiliares (compartido con Minimax)
* `main.py`: interfaz de consola

---

## Cómo ejecutar

```
python main.py
```