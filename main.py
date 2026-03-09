import tkinter as tk
from logica import AnalisisAcademico
from vista import Vista


archivo = "datos_rendimiento_universidad.csv"

modelo = AnalisisAcademico(archivo)
vista = Vista()


def mostrar_materias():

    datos = modelo.materias_mas_reprobadas()

    vista.grafico_barras(
        datos,
        "Materias con mayor índice de reprobación",
        "Materia",
        "Porcentaje de reprobación"
    )


def mostrar_carreras():

    datos = modelo.carreras_mejor_promedio()

    vista.grafico_barras(
        datos,
        "Carreras con mayor promedio",
        "Carrera",
        "Promedio"
    )


def mostrar_tendencias():

    datos = modelo.promedio_por_semestre()

    vista.grafico_linea(
        datos,
        "Promedio de calificación por semestre",
        "Semestre",
        "Promedio"
    )


def mostrar_riesgo():

    datos = modelo.riesgo_academico()

    vista.grafico_linea(
        datos,
        "Riesgo académico (% reprobados por semestre)",
        "Semestre",
        "Porcentaje"
    )


# ----------- INTERFAZ -----------

ventana = tk.Tk()
ventana.title("Análisis de Rendimiento Académico")
ventana.geometry("400x300")


titulo = tk.Label(
    ventana,
    text="Sistema de Análisis Académico",
    font=("Arial", 16)
)

titulo.pack(pady=20)


boton1 = tk.Button(
    ventana,
    text="Materias con mayor reprobación",
    command=mostrar_materias,
    width=30
)

boton1.pack(pady=5)


boton2 = tk.Button(
    ventana,
    text="Carreras con mayor promedio",
    command=mostrar_carreras,
    width=30
)

boton2.pack(pady=5)


boton3 = tk.Button(
    ventana,
    text="Tendencia de promedio por semestre",
    command=mostrar_tendencias,
    width=30
)

boton3.pack(pady=5)


boton4 = tk.Button(
    ventana,
    text="Riesgo académico",
    command=mostrar_riesgo,
    width=30
)

boton4.pack(pady=5)


boton5 = tk.Button(
    ventana,
    text="Salir",
    command=ventana.quit,
    width=30
)

boton5.pack(pady=20)


ventana.mainloop()