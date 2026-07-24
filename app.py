import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Sky Reader",
    page_icon="skyreader.png",
    layout="wide"
)



# =====================================================
# CSS
# =====================================================

st.markdown(
"""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&display=swap'
);


/* =====================
GLOBAL
===================== */

.stApp {

    background:#FFF4E6;

}


html, body {

    font-family:'Cormorant Garamond', serif;

}


.block-container {

    padding-top:2rem;

    padding-left:5%;

    padding-right:5%;

}


/* =====================
TEXT
===================== */

h1,h2,h3,h4,h5,h6 {

    color:#274156 !important;

    font-family:'Cormorant Garamond', serif !important;

}


p,span,label {

    color:#274156 !important;

}


/* TITLE */

h1 {

    font-size:70px !important;

    text-align:center;

    font-weight:600;

}



/* =====================
SIDEBAR
===================== */


section[data-testid="stSidebar"] {

    background:#FFE8C7;

}


section[data-testid="stSidebar"] * {

    color:#274156 !important;

}



button[kind="header"] {

    background:#FFE8C7 !important;

    border-radius:15px;

}


button[kind="header"] svg {

    fill:#274156 !important;

}




/* =====================
METRIC CARDS
===================== */


.metric-card {


    background:#FFE8C7;


    height:160px;


    width:100%;


    border-radius:35px;


    padding:25px;


    box-sizing:border-box;


    display:flex;


    flex-direction:column;


    justify-content:center;


    align-items:center;



    box-shadow:

    0px 8px 20px rgba(0,0,0,0.08);

}



.metric-title {


    font-size:24px;


    font-weight:500;


    color:#274156 !important;


    text-align:center;


}



.metric-value {


    margin-top:10px;


    font-size:42px;


    font-weight:600;


    color:#274156 !important;


    text-align:center;


}


div[data-testid="column"] {

    display:flex;

    justify-content:center;

}



/* =====================
PLOTLY CONTAINER
===================== */


[data-testid="stPlotlyChart"] {


    background:#FFE8C7;


    border-radius:35px;


    padding:20px;


    box-shadow:

    0px 8px 20px rgba(0,0,0,0.06);

}




/* =====================
EXPANDER
===================== */


[data-testid="stExpander"] {


    background:#FFE8C7;


    border-radius:25px;


    margin-top:30px;


}



[data-testid="stExpander"] summary {


    color:#274156 !important;


    font-size:22px;


}



/* =====================
DATAFRAME
===================== */


[data-testid="stDataFrame"] {

    border-radius:20px;

}




/* =====================
REMOVE DEFAULT
===================== */


#MainMenu {

    visibility:hidden;

}


footer {

    visibility:hidden;

}


</style>

""",
unsafe_allow_html=True
)



# =====================================================
# AUTO REFRESH
# =====================================================


refresh_time = st.sidebar.slider(
    "Fréquence de mise à jour",
    1,
    30,
    5
)


st_autorefresh(
    interval=refresh_time*1000,
    key="refresh"
)



# =====================================================
# HEADER
# =====================================================


logo,title = st.columns([1,5])


with logo:

    st.image(
        "assets/skyreader.png",
        width=150
    )


with title:

    st.markdown(
        "<h1>Sky Reader</h1>",
        unsafe_allow_html=True
    )



st.markdown(
"""
<p style="
text-align:center;
font-size:25px;
">
Station météorologique intelligente Arduino
</p>
""",
unsafe_allow_html=True
)



# =====================================================
# LOAD CSV
# =====================================================


FILE="mesures.csv"


try:

    df=pd.read_csv(FILE)


except FileNotFoundError:

    st.error(
        "Le fichier mesures.csv est introuvable"
    )

    st.stop()



df["horodatage"] = pd.to_datetime(
    df["horodatage"],
    format="%H:%M:%S %m/%d/%y"
)


latest=df.iloc[-1]



# =====================================================
# METRIC CARD
# =====================================================


def metric_card(title,value):

    return f"""

<div class="metric-card">

<div class="metric-title">

{title}

</div>


<div class="metric-value">

{value}

</div>


</div>

"""



# =====================================================
# CURRENT VALUES
# =====================================================


st.markdown(
"<h2>Dernière mesure</h2>",
unsafe_allow_html=True
)



c1,c2,c3,c4 = st.columns(
    4,
    gap="large"
)



with c1:

    st.markdown(
        metric_card(
            "Température",
            f"{latest['temperature']} °C"
        ),
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        metric_card(
            "Pression",
            f"{latest['pression']} hPa"
        ),
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        metric_card(
            "Luminosité",
            f"{latest['luminosite']} lux"
        ),
        unsafe_allow_html=True
    )


with c4:

    st.markdown(
        metric_card(
            "Altitude",
            f"{latest['altitude']} m"
        ),
        unsafe_allow_html=True
    )



# =====================================================
# GRAPH FUNCTION
# =====================================================


def weather_graph(column,title):


    fig=go.Figure()



    fig.add_trace(

        go.Scatter(

            x=df["horodatage"],

            y=df[column],

            mode="lines",

            line=dict(

                color="#274156",

                width=3

            )

        )

    )



    fig.update_layout(

        height=320,


        paper_bgcolor="#FFE8C7",

        plot_bgcolor="#FFE8C7",


        title=dict(

            text=title,

            x=0.05,

            font=dict(

                family="Cormorant Garamond",

                size=28,

                color="#274156"

            )

        ),


        font=dict(

            family="Cormorant Garamond",

            size=16,

            color="#274156"

        ),



        margin=dict(

            l=50,

            r=30,

            t=60,

            b=40

        ),



        xaxis=dict(

            showgrid=False,

            tickfont=dict(

                color="#274156"

            )

        ),



        yaxis=dict(

            showgrid=True,

            gridcolor="#E5CFA8",

            tickfont=dict(

                color="#274156"

            )

        )

    )


    return fig



# =====================================================
# GRAPHS
# =====================================================


st.markdown(
"<h2>Évolution des mesures</h2>",
unsafe_allow_html=True
)



g1,g2 = st.columns(
    2,
    gap="large"
)



with g1:

    st.plotly_chart(

        weather_graph(
            "temperature",
            "Temperature"
        ),

        use_container_width=True

    )



with g2:

    st.plotly_chart(

        weather_graph(
            "pression",
            "Pressure"
        ),

        use_container_width=True

    )




g3,g4 = st.columns(
    2,
    gap="large"
)



with g3:

    st.plotly_chart(

        weather_graph(
            "luminosite",
            "Luminosity"
        ),

        use_container_width=True

    )



with g4:

    st.plotly_chart(

        weather_graph(
            "altitude",
            "Altitude"
        ),

        use_container_width=True

    )




# =====================================================
# DATA
# =====================================================


with st.expander(
    "Données complètes"
):

    st.dataframe(
        df,
        use_container_width=True
    )



st.caption(

    f"Dernière actualisation : "
    f"{pd.Timestamp.now().strftime('%H:%M:%S')}"

)
