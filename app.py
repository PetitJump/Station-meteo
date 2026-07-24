import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# -------------------------
# Configuration
# -------------------------

st.set_page_config(
    page_title="Une Station Météo",
    page_icon="🌦️",
    layout="wide"
)


st.title("🌦️ Une Station Météo")

st.write(
    "Visualisation des données météorologiques Arduino"

)
st_autorefresh(
    interval=5000,   # milliseconds
    key="data_refresh"
)

refresh_time = st.sidebar.slider(
    "Fréquence de mise à jour (secondes)",
    1,
    30,
    5
)


st_autorefresh(
    interval=refresh_time*1000,
    key="refresh"
)

st.caption(
    f"Dernière actualisation : {pd.Timestamp.now().strftime('%H:%M:%S')}"
)
# ------------------------
# Load CSV
# -------------------------

FILE = "data.csv"


try:
    df = pd.read_csv(FILE)

except FileNotFoundError:
    st.error("Le fichier data.csv est introuvable")
    st.stop()



# Convert date

df["horodatage"] = pd.to_datetime(
    df["horodatage"],
    format="%H:%M:%S %m/%d/%y"
)



# -------------------------
# Latest values
# -------------------------

derniere = df.iloc[-1]


st.subheader("📌 Dernière mesure")


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "🌡️ Température",
    f"{derniere['temperature']} °C"
)


col2.metric(
    "🌬️ Pression",
    f"{derniere['pression']} hPa"
)


col3.metric(
    "☀️ Luminosité",
    f"{derniere['luminosite']} lux"
)


col4.metric(
    "⛰️ Altitude",
    f"{derniere['altitude']} m"
)



st.divider()



# -------------------------
# Graphs
# -------------------------


st.subheader("📈 Évolution des mesures")


col1, col2 = st.columns(2)


with col1:

    fig = px.line(
        df,
        x="horodatage",
        y="temperature",
        title="🌡️ Température"
    )

    st.plotly_chart(fig, use_container_width=True)



with col2:

    fig = px.line(
        df,
        x="horodatage",
        y="pression",
        title="🌬️ Pression"
    )

    st.plotly_chart(fig, use_container_width=True)



col3, col4 = st.columns(2)


with col3:

    fig = px.line(
        df,
        x="horodatage",
        y="luminosite",
        title="☀️ Luminosité"
    )

    st.plotly_chart(fig, use_container_width=True)



with col4:

    fig = px.line(
        df,
        x="horodatage",
        y="altitude",
        title="⛰️ Altitude"
    )

    st.plotly_chart(fig, use_container_width=True)



# -------------------------
# Table
# -------------------------

st.subheader("📋 Données complètes")

st.dataframe(
    df,
    use_container_width=True
)
