import streamlit as st
import pandas as pd
# Charger le CSV dans le fichier app_taxis.py
taxis = pd.read_csv("CSV/taxis.csv")

#Titre
st.title("Dashboard Analyse Taxis- Florian")

#Menu déroulant pour choisir les quartiers
quartiers = taxis["pickup_borough"].dropna().unique()
quartier_choisi = st.selectbox("Choisissez un quartier de prise en charge:", quartiers)

#Filtrer le Dataframe en fonction du Quartier choisit
taxis_filtres = taxis[taxis["pickup_borough"]== quartier_choisi]
st.dataframe(taxis_filtres.head())

#Calcul des metriques
nb_course_arrondissement = len(taxis_filtres)
st.metric(label= f"Nombre total de courses dans ce quartier: {quartier_choisi}", value = nb_course_arrondissement)