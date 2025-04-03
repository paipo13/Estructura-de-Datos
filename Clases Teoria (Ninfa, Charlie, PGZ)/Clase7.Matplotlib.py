### MATPLOTLIB ###
# Matplotlib es una bilioteca de graficos muy flexible y potente.
# Puede soportar una variedad de diferentes plataformas de graficos Phyton y ventanas del sistema operativo.
# Tambien puede generar graficos de salida de una variedad de formatos diferentes. Incluidos PNG, JPEG, SVG y PDF.

### GRAFICOS ###

#Grafico Lineal:
import matplotlib.pyplot as pyplot
pyplot.plot([1,0.25,0.5,2,3,3.75,3.5])
pyplot.show()



# Grafica Barras:
#Ejemplo1
import matplotlib.pyplot as plt

habitantes=[671280,447287,94782,8611122,591630]
ciudades=['Bristol','Cardiff','Bath','Liverpool','Glasgow']

plt.title(label="Grafico habitantes por Ciudad",fontsize=20,color='blue')
plt.xlabel("Ciudades")
plt.ylabel('Poblacion')

plt.bar(ciudades,habitantes,color='green',width=0.5)

plt.show()

# Ejemplo2
import matplotlib.pyplot as plt

x = ["A", "B", "C", "D", "E"]
y = [10, 24, 36, 40, 24]

fig, ax = plt.subplots(figsize=(5, 5))
ax.bar(x, y, color='violet')

ax.set_title('Ejemplo de gráfico de barras')
ax.set_xlabel('Categorías')
ax.set_ylabel('Valores')
plt.show()



#Grafica Torta:
from matplotlib import pyplot as plt

lenguajes=['C','C++','Java','Python']
usuarios=[50,30,70,90]

plt.pie(usuarios,labels=lenguajes, autopct='%1.2f%%')
plt.title(label='Preferencia actual Lenguajes Programacion',loc='center',color='red')

plt.show()



#Graficas Lineales:
import matplotlib.pyplot as plt

a=[1,2,3,4]
b=[11,22,33,44]
c=[2,4,6,8]
d=[24,20,18,21]

plt.title("Grafica Linea")
plt.xlabel("Eje x")
plt.ylabel("Eje y")

# Grafica de lineas
plt.plot(a,b,'o-',color='green',linewidth=3,label="Porcentajes")
plt.plot(c,d,'o-',color='red',linewidth=3,label="Porcentajes")

plt.show()