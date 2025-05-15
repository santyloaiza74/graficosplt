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
def circulo_girando():
    fig, ax = plt.subplots()
    point, = ax.plot([], [], 'ro')
    trail, = ax.plot([], [], 'b-', alpha=0.5)
    xdata, ydata = [], []

    def animate3(i):
        t = i * 0.1
        x = np.cos(t)
        y = np.sin(t)
        xdata.append(x)
        ydata.append(y)
        point.set_data(x, y)
        trail.set_data(xdata, ydata)
        return point, trail

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    plt.title('Movimiento Circular con Cola')
    ani3 = FuncAnimation(fig, animate3, frames=200, interval=50)
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.show()
# ==============================
# 4. Visualización de evolución de datos desde CSV
# ==============================
# Objetivo: Leer un CSV (como el de energías renovables) y animar cómo varía un valor por país o región a lo largo de los años.
# • Cada frame muestra el dato del año siguiente.
# • Ideal para usar tus datos reales.

# Supón que tienes un CSV con columnas: Año, País, Valor
# Ejemplo mínimo ficticio para demo:
def animate_csv():
    data = {
        'Año': [2020, 2020, 2021, 2021, 2022, 2022],
        'País': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Valor': [100, 80, 120, 90, 140, 95]
    }
    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    bar_container = ax.bar(df['País'].unique(), [0]*len(df['País'].unique()))

    def animate4(i):
        year = 2020 + i
        df_year = df[df['Año'] == year]
        for bar, val in zip(bar_container, df_year['Valor']):
            bar.set_height(val)
        ax.set_title(f'Evolución de datos - Año {year}')
        return bar_container

    ani4 = FuncAnimation(fig, animate4, frames=3, interval=1000)
    plt.ylabel('Valor')
    plt.xlabel('País')
    plt.ylim(0, 160)
    plt.show()

# ==============================
# 5. Sistema planetario simple
# ==============================
# Objetivo: Animar planetas girando alrededor de una estrella.
# • Usa ecuaciones de movimiento circular para cada planeta.
# • Cada planeta con un radio y velocidad angular diferentes.
def animate_planetary_system():
    fig, ax = plt.subplots()
    sun = ax.plot(0, 0, 'yo', markersize=10)[0]

    # Configuración de los planetas: radio y velocidad
    planetas = [
        {'radio': 1, 'vel': 0.1, 'color': 'blue'},
        {'radio': 1.5, 'vel': 0.07, 'color': 'green'},
        {'radio': 2, 'vel': 0.05, 'color': 'red'}
    ]

    planet_points = []
    for p in planetas:
        point, = ax.plot([], [], 'o', color=p['color'])
        planet_points.append(point)

    def animate5(i):
        for p, point in zip(planetas, planet_points):
            t = i * p['vel']
            x = p['radio'] * np.cos(t)
            y = p['radio'] * np.sin(t)
            point.set_data(x, y)
        return planet_points

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')
    plt.title('Sistema Planetario Simple')
    plt.grid(True)
    ani5 = FuncAnimation(fig, animate5, frames=300, interval=50)
    plt.show()