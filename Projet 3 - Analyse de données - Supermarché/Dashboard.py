#import librarie to handle dashborad ui
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('Graphicloads-Colorful-Long-Shadow-Cart.ico')
st.set_page_config(
    page_title="supermarker dashboard",
    page_icon=im,
    layout="wide",
)

#pour afficher les tableau sans index
# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)


data =  pd.read_csv(r"E:\Machine Learning & Business Intelligence\Analyse de donnée - Supermarché\supermarket_sales.csv")
db =  pd.read_csv(r"E:\Machine Learning & Business Intelligence\Analyse de donnée - Supermarché\supermarket_sales.csv")


st.title("Supermarket Analysis Dashboard")



#creer un sidebar avec des onglets pour naviguer entre les dashboards
st.sidebar.title("Navigation")
dash = st.sidebar.radio(
    "Choisir un dashboard",
    ("Accueil", "Ventes Global", "Ville", "Produits")
)

def mois(x) :
    return x.split('/')[0]
#mois('04/19/19 08:46') ==> ['04', '19', '19 08:46'] ----> sa c'est pour x.split('/')
data['Mois'] = data['Date'].apply(mois) #Ajout d'un champs mois creer a partir de la fonction mois
data['Mois'] = data['Mois'].astype(int)
mois = data['Mois'].unique() #---> liste des valeurs dans le champs mois en sql distinct, on constate qu'il y a 3 mois


#data sans certaine colonne
table = db.drop(['Rating','Time','cogs','gross income','gross margin percentage'],axis=1).drop_duplicates()



if dash =="Accueil":
    st.metric("Chiffre D'affaire", data["Total"].sum())
    st.write("Le Supermarket a fais un total de ", data.shape[0], "ventes en ",len(mois), "mois")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Le Supermarket vend ", data['Product line'].nunique(), ": ")
        for i in data['Product line'].unique():
            st.write(i)
    with col2:
        st.write("Le Supermarket se situe dans ", data['City'].nunique(), "ville : ")
        for i in data['City'].unique():
            st.write(i) 
    st.write(" ")
    st.write("vous trouverez ci-dessous elements lignes du dataset")
    st.table(table.sort_values(by='Date', ascending=False))




    
if dash =="Ventes Global":
    st.header("Ventes Global")
    #creer une selection des produits
    prod = st.multiselect("Choisir un produit", data['Product line'].unique())
    
    
    #bar chart of sales by month in function of product
    if prod:
        data_prod = data[data['Product line'].isin(prod)]
        data_prod = data_prod.groupby('Mois')['Total'].sum()
        data_prod = pd.DataFrame(data_prod)
        data_prod = data_prod.reset_index()
        plt.bar(data_prod['Mois'], data_prod['Total'])
        plt.title('Ventes par mois en fonction du produit')
        plt.xlabel('Mois')
        plt.ylabel('Total')
        st.pyplot(plt)
    else:
        data_prod = data.groupby('Mois')['Total'].sum()
        data_prod = pd.DataFrame(data_prod)
        data_prod = data_prod.reset_index()
        plt.bar(data_prod['Mois'], data_prod['Total'])
        plt.title('Ventes par mois')
        plt.xlabel('Mois')
        plt.ylabel('Total')
        st.pyplot(plt)
        



    
if dash =="Ville":
    st.write("Ville")
    
if dash =="Produits":
    st.write("Produits")