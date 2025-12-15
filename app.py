import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
st.title("Introduzindo os elimentes de streamlit")
menu= option_menu(menu_title="Menu",
                 options=["Inicio", "Gráfico", "Estatísticas", "Gráficos dinâmicos", "Widgets","Formulário"],
                 icons=["bar-chart", "bar-chart-line", "toogles", "bar-chart"],
                 menu_icon="cast",
                 default_index=0,
                 orientation="horinzantal"

                 )
with st.sidebar:
  st.sucess("**UPLOAD DE DADOS")
