import pandas as pd
import math


class AnalisisAcademico:

    def __init__(self, ruta_csv):
        self.datos = pd.read_csv(ruta_csv)

    # ----------- UTILIDAD -----------

    def truncar_2_decimales(self, serie):
        return serie.apply(lambda x: math.trunc(x * 100) / 100)

    # ----------- ANALISIS -----------

    def materias_mas_reprobadas(self):

        total = self.datos.groupby("materia").size()
        reprobados = self.datos[self.datos["calificacion"] < 6].groupby("materia").size()

        porcentaje = (reprobados / total) * 100
        porcentaje = porcentaje.fillna(0)

        porcentaje = self.truncar_2_decimales(porcentaje)
        porcentaje = porcentaje.sort_values(ascending=False)

        return porcentaje.astype(str) + "%"

    def carreras_mejor_promedio(self):

        promedios = self.datos.groupby("carrera")["calificacion"].mean()

        promedios = self.truncar_2_decimales(promedios)

        return promedios.sort_values(ascending=False)

    def promedio_por_semestre(self):

        promedio = self.datos.groupby("semestre")["calificacion"].mean()

        promedio = self.truncar_2_decimales(promedio)

        return promedio.sort_index()

    def riesgo_academico(self):

        total = self.datos.groupby("semestre").size()
        reprobados = self.datos[self.datos["calificacion"] < 6].groupby("semestre").size()

        porcentaje = (reprobados / total) * 100
        porcentaje = porcentaje.fillna(0)

        porcentaje = self.truncar_2_decimales(porcentaje)

        return porcentaje.astype(str) + "%"
