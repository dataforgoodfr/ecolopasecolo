import streamlit as st
import random

st.write("# Ecolo ou pas écolo ?")
# st.info("Ce site a été construit en inspiration par De gauche ou de droite")
# st.sidebar.info("Copyright Eclaircies")

query = st.text_input("Alors écolo ou pas écolo ?")

if query != "":

    # Algorithme
    result = random.choice(["Ecolo","Pas écolo"])

    # Display result
    st.write(result)

    if result == "Ecolo":
        st.balloons()

    elif result == "Pas écolo":
        st.write("💩💩💩")



