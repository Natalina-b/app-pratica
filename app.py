import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import openpyxl
#import matplotlib.pyplot as plt
#import time
st.title("Introduzindo os elimentes de streamlit")
menu = option_menu(menu_title="Menu",
                 options=["Inicio", "Gráfico", "Estatísticas", "Gráficos dinâmicos", "Widgets","Formulário"],
                 icons=["bar-chart", "bar-chart-line", "toogles", "bar-chart"],
                 menu_icon="cast",
                 default_index=0,
                 orientation="horizontal"
                 )

with st.sidebar:
    st.success("**UPLOAD DE DADOS**")
    dados = st.file_uploader(
    "CAREGA O FICHEIRO...",
    type=["xlsx", "xls"]
    )

if dados:
   def carregar_dados(dados):
      try:
        df = pd.read_excel(dados)
        return df
      except FileNotFoundError:
        return pd.DataFrame()
      
else:
    st.info("Carregue um ficheiro excel para começar")
 
if menu == "Inicio":
  with st.expander("**Sobre o Istituto Nacional de Estatística**"):
    st.write("ACESSE O SITE WWW.INE.CV")
    st.image("Logo-1.png")
      
if menu == "widgets":
  bt = st.button("Dê um clique")
  
if bt:
  st.info("Nova o ponto de slider!", min_value=25,\
           max_value=35, value=30, step=1
           )

texto= f"Eu tenho {sd} anos!"
st.success(texto)
