import streamlit as st
from notebooks.backend import prediction, ScrapTool, clean_text
from data.database import create_database, add_customer, delete_predict, view_customers, search_customer


def main():
    st.title('WEB CLASSIFICATION')
   
    # Pide al usuario que ingrese una URL 
    # url1 ="https://www.bbc.com/sport/live/football/64405195"
    url1 = st.text_input("Ingrese la URL para la predicción")
    
    create_database()
    
    # Cuando se presiona el botón, ejecuta la predicción
    # try:   
    if st.button("Predecir"):
        pred = prediction(url1)
        # Muestra la predicción en la interfaz
        st.write((pred))
        titulo = ScrapTool().get_website_name(url1)
        url = url1
        add_customer(titulo, url, pred)
        
    st.sidebar.header("Configuración")
    try:  
        if st.sidebar.button("Delete"):
            b1 = st.sidebar.text_input("Ingrese el titulo")
            b2 = st.sidebar.text_input("Ingrese el id")
            customers = delete_predict(b1, b2)
            st.table(customers)
        elif st.sidebar.button("Search"):
            b1=st.sidebar.text_input("Ingrese el titulo")
            b2=st.sidebar.text_input("Ingrese el id")
            customers = search_customer(b1, b2)
            st.header("predicciones File")
            st.table(customers)   
        elif st.sidebar.button("View"):
            customers = view_customers()
            st.header("predicciones File")
            st.table(customers)
    except:
     st.write("Por favor ingresa una UR1L")   
    # except:
        # st.write("Por favor ingresa una URL")


if __name__ == '__main__':
    main()
