import streamlit as st
import pandas as pd

# Verificar se o DataFrame está no session_state
if "df_spotify" in st.session_state:
    df_spotify = st.session_state["df_spotify"]
    st.write(df_spotify)
else:
    st.write("O DataFrame não foi inicializado. Por favor, execute a página 1 primeiro.")

