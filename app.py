import streamlit as st
import pandas as pd

# Titre principal de la page
st.title("Mon Premier Dashboard Streamlit")

# Texte de présentation
st.write("Bienvenue sur cette application intéractive dédiée à l'analyse de données.")

if st.button("Cliquez ici"):
    st.success("Bouton cliqué avec succès !")