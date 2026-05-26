import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")

st.write("elaborado por Maribel Cano")

sesion=st.selectbox("Seleccione una sesión",["Sesion 1","Sesion 2","sesion 3],"Sesion 4")

