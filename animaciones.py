import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import os
# 1. Seno animado con fase desplazada
# Objetivo: Animar una onda seno que cambia de fase a lo largo del tiempo.
# • Animar una función sin(x + t).
# • Usar FuncAnimation.
# • Mostrar cómo la onda se desplaza hacia la izquierda o derecha.
def sin_animated():
    fig, ax = plt.subplots()
    x = np.linspace(0, 2 * np.pi, 100)
    line, = ax.plot(x, np.sin(x), color='blue')
    ax.set_ylim(-1.5, 1.5)
    ax.set_title('Seno Animado')
    ax.set_xlabel('X')
    ax.set_ylabel('sin(X + t)')

    def update(frame):
        line.set_ydata(np.sin(x + frame / 10))
        return line,

    ani = FuncAnimation(fig, update, frames=100, interval=50)
    ani.save('./graficos/seno_animated.gif', writer='pillow', fps=20)
    plt.show()
# 2. Puntos aleatorios moviéndose (ruido)
# Objetivo: Simular partículas que se mueven aleatoriamente en el plano.
# • Usar scatter para graficar puntos.
# • En cada frame, mover cada punto un poco en una dirección aleatoria.
# • Ideal para introducir dinámicas 2D básicas.
def puntos_aleatorios():
    fig, ax = plt.subplots()
    num_puntos = 100
    x = np.random.rand(num_puntos)
    y = np.random.rand(num_puntos)
    scatter = ax.scatter(x, y, color='blue')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Puntos Aleatorios')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    def update(frame):
        nonlocal x, y
        x += (np.random.rand(num_puntos) - 0.5) * 0.01
        y += (np.random.rand(num_puntos) - 0.5) * 0.01
        scatter.set_offsets(np.c_[x, y])
        return scatter,

    ani = FuncAnimation(fig, update, frames=100, interval=50)
    ani.save('./graficos/puntos_aleatorios.gif', writer='pillow', fps=20)
    plt.show()
# 3. Círculo girando alrededor del origen
# Objetivo: Animar un punto que describe un círculo.
# • Posición del punto: (cos(t), sin(t)).
# • También puedes dibujar la trayectoria si quieres agregar un efecto de “cola”.
# • Buena práctica para sistemas coordenados.
#  Ejercicios Avanzados (4 al 6)
# 4. Visualización de evolución de datos desde CSV
# Objetivo: Leer un CSV (como el de energías renovables) y animar cómo varía un valor por
# país o región a lo largo de los años.
# • Cada frame muestra el dato del año siguiente.
# • Opción: mostrar una barra que crece con los años.
# • Ideal para usar tus datos reales.
# 5. Sistema planetario simple
# Objetivo: Animar planetas girando alrededor de una estrella.
# • Usa ecuaciones de movimiento circular para cada planeta.
# • Cada planeta con un radio y velocidad angular diferentes.
# • Opción: dejar trayectorias visibles.