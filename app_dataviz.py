import streamlit as st
import pandas as pd
import seaborn as sns #necessaire pour la heatmap
import matplotlib.pyplot as plt #idem

#Charger le CSV (impossible d'y arriver avec l'url...)
dataframe_fligh = pd.read_csv("CSV/flights.csv")

# Titre
st.title("Analyse de Flights.csv de Seaborn Data")

# Afficher le dataframe
st.dataframe(dataframe_fligh.head()) #Juste pour voir les colonnes du df

#Filtrer par année
annee = st.slider("Choisissez une année: ", min_value=1949, max_value=1960, value=(1949,1960))
st.write(annee)
# Le slider crée la barre avec deux poignées (debut et fin)
#annee garde les deux années choisies
#st.write(annee) permet d'afficher la barre
debut,fin = annee # mets la 1ère année dans début, la deuxème dans fin
flights_annees = dataframe_fligh[(dataframe_fligh["year"] >= debut) & (dataframe_fligh["year"] <= fin)] 
# Dans la table, garde que les lignes qui ont une date >= à début ET <= fin

# Voir la dt filtrée
st.dataframe(flights_annees)

# Pour filtrer selon les mois
mois= dataframe_fligh["month"].dropna().unique()
options_mois = ["Tous les mois"] + list(mois)
mois_choisit = st.selectbox("Choisissez un mois", options_mois)
if mois_choisit == "Tous les mois":
    flights_mois = flights_annees
else:    
    flights_mois = flights_annees[flights_annees["month"] == mois_choisit]
st.dataframe(flights_mois)

#Calcul de la somme de passager
somme_passagers = flights_mois["passengers"].sum()
st.metric(label = f"Somme des passagers sur la période choisie: {mois_choisit}", value = somme_passagers)

#Pour le graphique
annual_passengers = flights_mois.groupby("year")["passengers"].sum()
st.subheader("Evolution du trafic aérien (Line Chart natif)")
st.line_chart(annual_passengers)

# Pour la heatmap
afficher_heatmap = st.checkbox ("Afficher Heatmap")
if afficher_heatmap:
    heatmap_flights = flights_annees.pivot( index = 'month', columns = 'year', values = 'passengers')
    fig, ax = plt.subplots(figsize =(20,10))
    sns.heatmap(heatmap_flights, annot = True, annot_kws={"size":12}, cmap="coolwarm", fmt="d", ax=ax)
    ax.tick_params(labelsize = 12)
    st.pyplot(fig)