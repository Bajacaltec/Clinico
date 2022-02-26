from string import digits
import streamlit as st
import pandas as pd
import numpy as np
st.title('Censo')
Nombre=st.sidebar.text_input('Nombre')
NSS=st.sidebar.text_input("NSS","",10)
NSS1=int(NSS)

#Falta ver como exigir que sean 10 digitos si no no se puede avanzar

agregado=st.sidebar.text_input("Agregado (resumido, ejem 1F89OR)","",6)
agremayus=agregado.upper()
cama=st.sidebar.number_input('Cama',100,800,300,1)
Genero = "F" in agremayus
if Genero == True:
    Genero = "Femenino"
else:
    Genero = "Masculino"
text=str("Se ingresaron los datos de "+Nombre+' con el género '+Genero)
st.sidebar.subheader(text)
lista=[Nombre,NSS,agremayus,Genero]
st.table(lista)
#No funcniona el download button, seguramente debo actualizar streamlit
# st.download_button('Bajar',lista)

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

#Hacer el censo

#interfaz gráfica para hacer notas, indicaciones, altas, interconsultas

#Generar PDFs de las solicitudes para trabajar