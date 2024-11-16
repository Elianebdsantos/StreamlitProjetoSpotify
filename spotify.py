import streamlit as st
import pandas as pd 
import time
from streamlit_player import st_player

st.set_page_config(
    layout="wide",
    page_title="spotify songs"
)

@st.cache_data
def load_data():
    df = pd.read_csv("01 Spotify.csv")
    time.sleep(5)
    #Operação pesasda
    return df

df= load_data()
st.session_state["df_spotify"]= df

# Gráfico de linha
df_line = df[df["Stream"] > 1000000000].set_index("Artist")

display = st.checkbox("Display")
if display:
    st.bar_chart(df_line["Stream"])





# Gráfico de barras
artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists)
df_bar = df[df["Artist"] == artist].set_index("Track")
display = st.checkbox("Diplay")

if display:
    st.bar_chart(df_bar["Stream"])

col1, col2, col3 = st.columns(3)
col1.bar_chart(df_bar["Stream"])
col2.line_chart(df_bar["Danceability"])
col3.bar_chart(df_bar["Likes"])



st.write(artist)

st_player('https://www.youtube.com/watch?v=DwckUSF67TY')

# Exibir DataFrame
#st.dataframe(df)
