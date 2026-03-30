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

```id="instminimax2"
pip install pygame
```

Ejecutar:

```id="runminimax2"
python minimax_ui.py
```
