#### Manual Básico Streamlit ####

# # Lo que voy a intentar hacer es un cronograma lo más sencillo posible de cómo instalar y usar Streamlit.

# # Pasos a seguir:

# 1. Instalar Streamlit: pip install streamlit
# 2. Importar la librería: import streamlit as st
# 3. Crear una interfaz básica: Uso de st.title(), st.header(), st.text(), etc.
# 4. Agregar widgets interactivos: Uso de st.button(), st.slider(), st.text_input(), etc.
# 5. Mostrar datos y gráficos: st.dataframe(), st.bar_chart(), st.pyplot(), etc.
# 6. Ejecutar la aplicación: streamlit run archivo.py



# 1. Instalar Streamlit

    # Para instalar Streamlit, abrimos una terminal y escribimos:

    # pip install streamlit

    # Para verificar que la instalación fue correcta, ejecutamos:

    # import streamlit as st
    # st.write("Streamlit está instalado correctamente!")

    # O bien podemos escribir en la terminal streamlit --version
    # a lo que deberia devolver la version del stremlit que tenemos descargado...

    # Si no hay errores, la instalación fue exitosa.


# 2. Importar la librería

    # Antes de empezar a trabajar con Streamlit, importamos la librería:

    # import streamlit as st

# 3. Crear una interfaz básica

    # Podemos agregar títulos, encabezados y texto a nuestra aplicación:

    # st.title("Mi primera app con Streamlit")
    # st.header("Encabezado secundario")
    # st.text("Este es un texto básico en Streamlit.")
    

# 4. Agregar widgets interactivos

    # Streamlit permite agregar elementos interactivos muy fácilmente:

    # if st.button("Presióname"):
    #     st.write("¡Botón presionado!")

    # nombre = st.text_input("Ingresa tu nombre")
    # st.write(f"Hola, {nombre}!")

    # valor = st.slider("Selecciona un valor", 0, 100, 50)
    # st.write(f"Valor seleccionado: {valor}")

    # Otros ejemplos serian:
    # opcion = st.selectbox("Selecciona una opción", ["Opción 1", "Opción 2", "Opción 3"])
    # st.write(f"Elegiste: {opcion}")

    # subir_archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])
    # if subir_archivo:
    #     st.write("Archivo cargado exitosamente")

# 5. Mostrar datos y gráficos

    # Podemos mostrar datos en tablas y gráficos:

    # import pandas as pd ("¡NO SE USAN EN ESTA MATERIA! POR LO QUE LOS ARCHIVOS CSV SE DEBEN CARGAR MANUALMENTE")
    # import numpy as np
    # import matplotlib.pyplot as plt

    # # Crear datos
    # datos = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
    # st.dataframe(datos)  # Mostrar tabla interactiva

    # # Mostrar un gráfico de barras
    # st.bar_chart(datos)

    # # Mostrar un gráfico con Matplotlib
    # fig, ax = plt.subplots()
    # ax.plot([1, 2, 3, 4], [10, 20, 15, 25])
    # st.pyplot(fig)

    # Otros ejemplos serian:
    # import plotly.express as px

    # df = pd.DataFrame({
    #     "Categoría": ["A", "B", "C", "D"],
    #     "Valores": [10, 20, 15, 25]
    # })

    # fig = px.bar(df, x="Categoría", y="Valores", title="Gráfico interactivo con Plotly")
    # st.plotly_chart(fig)

# 6. Ejecutar la aplicación

    # Para ver nuestra aplicación en el navegador, guardamos nuestro archivo como "app.py" (nombre del archivo)
    # y ejecutamos en la terminal:

    # streamlit run app.py

    # Esto abrirá la aplicación en el navegador de forma automática.



















# Ejemplos(Para correrlos copienlos y ponglaos en un archivo nuevo!!!):
# 1. Esto es un ejmeplo basico de como funciona...
import streamlit as st

st.title("Hello, world!")
st.write("Esta es mi primera aplicación web en Python con Streamlit.")


# 2. Ejemplo basico de como funciona dado por la pagina oficial de matplotlib.

import streamlit as st

st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()

    
#  3. El codigo ahora crea unapagina que tiene dos botones interactivos uno en el cual ingresamos
#  un nombre ( el de la persona) y luego eligue una edad (numero entero, mayor a 0 y menor a 101).
#   Nos devuelve la edad que tendremos en 10 años.

import streamlit as st

st.title("Calculadora de Edad")

nombre = st.text_input("Ingresa tu nombre")
edad = st.number_input("Ingresa tu edad", min_value=1, max_value=100)

if st.button("Mostrar mensaje"):
    st.write(f"Hola {nombre}, en 10 años tendrás {edad + 10} años.")


# 4. Devuelve una pagina con la funcion seno. Usamos numpy.

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Gráfico de una Función Seno")

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)



#  5. Esta pagina lo que hace es generar un boton interactivo con el usuario que al presionarlo uno 
# puede entrar a los archivos de la computadora y buscar un archivo csv el cual sera procesado para 
# crear diferentes graficos de barra (podriamos crear otras cosas...).


import streamlit as st
import csv
import matplotlib.pyplot as plt

st.title(" Carga y visualización de un archivo CSV ")

# Subir archivo CSV
archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])

if archivo is not None:
    # Leer el archivo CSV manualmente
    contenido = archivo.read().decode("utf-8").splitlines()
    lector_csv = csv.reader(contenido)
    
    # Convertir los datos en una lista
    datos = list(lector_csv)
    
    # Mostrar primeras filas (máximo 5)
    st.write("### Vista previa de los datos:")
    for fila in datos[:6]:  # Se muestran 6 filas: 1 de encabezado + 5 de datos
        st.write(fila)

    # Seleccionar columna para graficar
    columnas = datos[0]  # Encabezados
    seleccion_columna = st.selectbox("Selecciona una columna numérica", columnas)

    # Obtener índice de la columna seleccionada
    indice_columna = columnas.index(seleccion_columna)

    # Extraer valores numéricos de la columna (omitiendo el encabezado)
    valores = []
    for fila in datos[1:]:
        try:
            valores.append(float(fila[indice_columna]))
        except ValueError:
            continue  # Ignorar valores no numéricos

    # Graficar los datos
    if valores:
        fig, ax = plt.subplots()
        ax.hist(valores, bins=20, color="blue", alpha=0.7)
        ax.set_title(f"Distribución de {seleccion_columna}")
        ax.set_xlabel(seleccion_columna)
        ax.set_ylabel("Frecuencia")
        st.pyplot(fig)
    else:
        st.write(" No hay datos numéricos en la columna seleccionada.")


# 6. Si bien usa pandas, esto es un ejemplo del techo que tiene streamlit (ninguno...usemos la imaginacion)
# Nos devuelve la altura de edificios, casas, etc de un punto eleguido. Elegi la ciudad de San Fransisco
# , si se figan en google erath pueden ver com coincide lo dado en la pagina creada con la vida real. Los
# datos los tomamos de una pagina (oviamente...)


import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.write("Streamlit has lots of fans in the geo community. 🌍 It supports maps from PyDeck, Folium, Kepler.gl, and others.")

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))