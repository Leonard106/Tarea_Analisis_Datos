import matplotlib.pyplot as plt


class Vista:

    def grafico_barras(self, datos, titulo, xlabel, ylabel):

        try:
            datos_float = datos.astype(str).str.replace("%", "").astype(float)
        except:
            datos_float = datos

        ax = datos_float.plot(kind="bar", color="skyblue")

        # Ajuste del eje Y para ver mejor diferencias pequeñas
        margen = (datos_float.max() - datos_float.min()) * 0.1  # 10% margen
        ax.set_ylim(datos_float.min() - margen, datos_float.max() + margen)

        plt.title(titulo)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.tight_layout()
        plt.show()

    def grafico_linea(self, datos, titulo, xlabel, ylabel):

        try:
            datos = datos.astype(str).str.replace("%", "").astype(float)
        except:
            pass

        datos.plot(kind="line", marker="o")

        plt.title(titulo)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.grid(True)

        plt.tight_layout()
        plt.show()