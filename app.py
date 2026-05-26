import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")

st.write("elaborado por Maribel Cano")

sesion=st.sidebar.selectbox("Seleccione una sesión",["Sesion 1","Sesion 2","Sesion 3","Sesion 4"])

if sesion=="Sesion 1":
  st.write("Bienvenidos la sesion 1")
  st.image("COLORES.PNG")
elif sesion=="Sesion 2":
  st.write("Bienvenidos a la sesion 2")
elif sesion=="Sesion 3":
  st.write("Bienvenido a la sesion 3 ")
else:
  st.write("Bienvenido a la sesion 4")
    
  precio=st.number_input("Ingrese el precio del producto",min_value=0,max_value=5000,value=1200)
  descuento=st.number_input("Ingrese el dcto del 0 al 100%",min_value=0,max_value=100)
  precio_final_producto=precio-(precio*descuento/100)
  st.write("el precio del producto es:",precio_final_producto)

  

