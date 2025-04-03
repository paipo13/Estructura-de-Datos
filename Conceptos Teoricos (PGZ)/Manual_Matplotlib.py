### Manual Basico Matplotlib ####

# Lo que voy a intentar de hacer es un cronograma lo mas sencillo posible de como instalar y usar matplotlib.
# Pasos a seguir:

# 1. Instalar Matplotlib: pip install matplotlib
# 2. Importar librerías: import matplotlib.pyplot as plt
# 3. Definir los datos: Manualmente, con NumPy o desde CSV
# 4. Elegir el tipo de gráfico: plt.plot(), plt.bar(), plt.scatter(), etc.
# 5. Personalizar el gráfico: Etiquetas, títulos, leyendas
# 6. Mostrar el gráfico: plt.show()
# 7. (Opcional) Guardar el gráfico: plt.savefig("archivo.png")

# Ahora vallamos a cada caso especificamente.

# 1. Instalar Matplotlib:
# Para la matplotlib tenemos que ir a la terminal y escribir textualmente: pip install matplotlib
# y para verificar que efectivamente se instalo bien. Corremos una nueva terminal habienod escrito:
import matplotlib
print(matplotlib.__version__)  
# Lo cual deberia imprimir la versión instalada (Por ejemplo a mi me duvuelve: 3.9.2 )

# 2. Importar librerías:
# Antes de empezar a trabajar y crear graficos o tablas tenemos que importar (donde codeamos) la libreria
# matplotlib.
# Aparte recomiendo ya en este paso importar la libreria de numpy la cual nos permitira trabajar de una forma 
# mas facil, corta (en cuanto a codigo) manteniendo la efectividad, limpia (en el sentido que nos permite 
# tener mas calidad en los graficos). Basicamente usamos numpy por que es mas efectivo y nos permite usar
# funciones matematicas a la hora de crear los graficos.
# Lo que escribiremos sera:
import numpy as np
import matplotlib.pyplot as plt

# 3. Definir los datos:
# Aqui lo que haremos sera crear las listas de las culaes sacaremos los datos para hacer nuestro/s grafico/s.
# Hay 3 fomrmas principales de hacer esto:
# A---> Datos Generado Manualmente: En este caso nosotros mismos agragamos (codeando) los datos a la listas. No 
# vamos a soler usar esta forma ya que es muy engorroso, especialmente cuando trabajamos con listas muy grandes, 
# que sera por ejemplo el caso del TP. Ejemplo:

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# B---> Datos Generados con numpy: En esta se usa numpy para crear (metematicamente) la lista que isaremos para 
# el grafico. Ejemplo:

x = np.linspace(0, 10, 100)
y = np.sin(x)

# C---> Datos Importados: Este es el caso de importar dotos de un archivo csv y traerlos a una lista (muy parecido
# a los que hicieron en informatica general).

# 4. Elegir el tipo de gráfico:
# Basicamente lo que hacemos aqui lo que hacemos es elguir el tipo de grafico que vamos a crear, puede ser
# graficos de torta, barras, lineales, , etc. Ejemplos
#
# Ejemplo: Gráfico de línea simple
plt.plot(x, y, marker="o", linestyle="-", color="b", label="Datos")

# Ejemplo: Gráfico de barras
plt.bar(x, y, color="g")

# Ejemplo: Gráfico de dispersión
plt.scatter(x, y, color="r")

# 5. Personalizacion de los Graficos:
# Es basicamennte tuñear los graficos. Es importante para que se entienda bien. Los ejemplos mas basicos son:

plt.xlabel("Eje X")  # Etiqueta del eje X
plt.ylabel("Eje Y")  # Etiqueta del eje Y
plt.title("Título del Gráfico")  # Título del gráfico
plt.legend()  # Mostrar la leyenda (si hay varias líneas)
plt.grid(True)  # Agregar una grilla


# Aca les adjunto el link para la documentación oficial de matplotlib: https://matplotlib.org/3.3.3/index.html
# Honestamente cuando la curse no lo lei. Pero debe ser bueno. Que se yo es mas opcional que otra cosa.