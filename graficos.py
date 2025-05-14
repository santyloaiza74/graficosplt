import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Parte 1: Visualización con Matplotlib (4 ejercicios)
# 1. Gráfico de línea simple
# Escribe un programa que grafique la siguiente lista de valores:
# valores = [3, 7, 1, 5, 12]
# Agrega título, etiquetas de ejes y una cuadrícula.
def parte_uno_1():
    plt.figure()
    valores = [3, 7, 1, 5, 12]
    plt.plot(valores, marker='o', color='blue')
    plt.title('Gráfico de Línea Simple')
    plt.xlabel('Índice')
    plt.ylabel('Valores')
    plt.savefig('./graficos/grafico_linea_simple.png')
    plt.show()
parte_uno_1()
# 2. Gráfico de barras
# Grafica la cantidad de estudiantes en 5 cursos:
# cursos = ['A', 'B', 'C', 'D', 'E']
# cantidad = [30, 25, 40, 20, 35]
def parte_uno_2():
    plt.figure()
    cursos = ['A', 'B', 'C', 'D', 'E']
    cantidad = [30, 25, 40, 20, 35]
    plt.bar(cursos, cantidad, color='orange')
    plt.title('Cantidad de Estudiantes por Curso')
    plt.xlabel('Cursos')
    plt.ylabel('Cantidad de Estudiantes')
    plt.savefig('./graficos/grafico_barras.png')
    plt.show()
# 3. Gráfico de dispersión (scatter plot)
# Genera dos listas de números aleatorios de 50 elementos y haz un gráfico de dispersión.
def parte_uno_3():
    plt.figure()
    x = np.random.rand(50)
    y = np.random.rand(50)
    plt.scatter(x, y, color='green')
    plt.title('Gráfico de Dispersión')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig('./graficos/grafico_dispersion.png')
    plt.show()
# 4. Subplots
# Crea un figure con 2 subgráficos:
# • Uno con una línea senoidal.
# • Otro con una función cuadrática.
def parte_uno_4():
    x = np.linspace(0, 2 * np.pi, 100)
    y1 = np.sin(x)
    y2 = x**2

    fig, axs = plt.subplots(2)
    axs[0].plot(x, y1, color='purple')
    axs[0].set_title('Senoidal')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('sin(X)')

    axs[1].plot(x, y2, color='red')
    axs[1].set_title('Función Cuadrática')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('X^2')

    plt.tight_layout()
    plt.savefig('./graficos/grafico_subplots.png')
    plt.show()
#  Parte 2: Cálculos y gráficos con NumPy (4 ejercicios)
# 5. Generar datos y graficar una función
# Usa np.linspace() para generar valores x entre -10 y 10, y grafica y = x² - 3x + 2.
def parte_dos_5():
    x= np.linspace(-10, 10)
    y = ((x**2) - (3*x)) + 2
    plt.plot(x, y, color='blue')
    plt.title('Gráfico de la función y = x² - 3x + 2')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig('./graficos/grafico_funcion.png')
    plt.show()
# 6. Comparación de funciones
# En el mismo gráfico, traza las funciones sin(x) y cos(x) para x entre 0 y 2π.
def parte_dos_6():
    x = np.linspace(0, 2 * np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label='sin(x)', color='blue')
    plt.plot(x, y2, label='cos(x)', color='orange')
    plt.title('Comparación de funciones: sin(x) y cos(x)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.savefig('./graficos/grafico_comparacion_funciones.png')
    plt.show()
# 7. Operaciones entre arrays
# Genera dos vectores de 100 valores aleatorios entre 0 y 100 y calcula:
# • La suma total.
# • El valor máximo.
# • La desviación estándar.
def parte_dos_7():
    v1= np.random.randint(0, 100, 100)
    v2= np.random.randint(0, 100, 100)
    suma_total = np.sum(v1 + v2)
    valor_maximo = np.max(v1 + v2)
    desviacion_estandar = np.std(v1 + v2)
    print(f'Suma total: {suma_total}')
    print(f'Valor máximo: {valor_maximo}')
    print(f'Desviación estándar: {desviacion_estandar}')
# 8. Histograma con NumPy
# Genera 1000 números aleatorios con distribución normal y muestra un histograma con
# plt.hist().
def parte_dos_8():
    datos = np.random.normal(0, 1, 1000)
    plt.hist(datos, bins=30, color='purple', alpha=0.7)
    plt.title('Histograma de Números Aleatorios')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.savefig('./graficos/grafico_histograma.png')
    plt.show()
#  Parte 3: Lectura de archivos con Pandas (4
# ejercicios)
# Usa un archivo .csv llamado datos_ventas.csv con las siguientes columnas:
# Producto, Ventas, Precio, Fecha
# 9. Cargar archivo
# Carga el archivo y muestra las primeras 5 filas con head().
# 10. Estadísticas básicas
# Muestra:
# • Total de ventas (Ventas.sum())
# • Promedio de precio
# • Producto más vendido

# 11. Filtrar datos
# Muestra solo los productos vendidos en el mes de enero (Fecha empieza por 2025-01).
# 12. Gráfica de barras con Pandas
# Grafica la cantidad total vendida por producto. (Agrupa por Producto y suma las ventas).
def parte_tres():
    dt= pd.read_csv('./data/datos_ventas.csv')
    print(dt.head())
    print(f'Total de ventas: {dt["Ventas"].sum()}')
    print(f'Promedio de precio: {dt["Precio"].mean()}')
    print(f'Producto más vendido: {dt["Producto"].mode()[0]}')
    print(dt[dt['Fecha'].str.startswith('2025-01')])
    dt.groupby('Producto')['Ventas'].sum().plot(kind='bar', color='orange')
    plt.title('Ventas Totales por Producto')
    plt.xlabel('Producto')
    plt.ylabel('Ventas Totales')
    plt.savefig('./graficos/grafico_ventas_producto.png')
    plt.show()