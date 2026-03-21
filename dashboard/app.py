import streamlit as st
import requests
from custom import personalizar, COLORS
import pandas as pd
import plotly.express as px

API_URL = "https://valentin003-newsense-api.hf.space"

st.set_page_config(
    page_title="Newsense",
)


def header():
    personalizar()
    st.markdown("<h1 style='text-align: center;'>Newsense</h1>", unsafe_allow_html=True)
    st.markdown("")


def show_metrics(df):
    cols = st.columns(len(df))
    for i in range(len(df)):
        sentiment = df.index[i]
        color = COLORS.get(sentiment, "#FFFFFF")
        with cols[i]:
            st.markdown(
                f"<span style='color:{color}; font-size:24px; font-weight:bold'>● {sentiment}</span>",
                unsafe_allow_html=True,
            )
            st.metric(label="", value=df.values[i])


def show_chart(df):
    fig = px.pie(
        values=df.values,
        names=df.index,
        color=df.index,
        color_discrete_map={
            "positive": "#00C48C",
            "negative": "#FF4B4B",
            "neutral": "#A0A0A0",
        },
    )
    fig.update_layout(
        title="Pie chart",
    )

    st.plotly_chart(fig, width="stretch")


def show_articles(df_sentiments):
    df_sentiments["score"] = round(df_sentiments["score"], 2)
    # Filtro 1 — sentimiento
    sentimientos = st.multiselect(
        "Filter by sentiment",
        options=["positive", "negative", "neutral"],
        default=["positive", "negative", "neutral"],
    )

    # Filtro 2 — búsqueda por palabra
    busqueda = st.text_input("Search in titles")

    # Filtro 3 — ordenar por score
    orden = st.selectbox(
        "Sort by score", options=["Highest to lowest", "Lowest to highest"]
    )
    df_filtrado = df_sentiments[df_sentiments["sentiment"].isin(sentimientos)]
    df_filtrado = df_filtrado[
        df_filtrado["title"].str.contains(busqueda, case=False, na=False)
    ]
    if orden == "Highest to lowest":
        df_filtrado = df_filtrado.sort_values(by="score", ascending=False)
    elif orden == "Lowest to highest":
        df_filtrado = df_filtrado.sort_values(by="score", ascending=True)

    st.write(df_filtrado)


def main():
    header()
    topic = st.text_input(label="Enter a topic")
    if st.button("Analyze"):
        with st.spinner("Fetching and analyzing news..."):
            requests.get(f"{API_URL}/news", params={"topic": topic})
            response = requests.post(f"{API_URL}/analyze", json={"topic": topic})
            requests.get(f"{API_URL}/news", params={"topic": topic})
            requests.post(f"{API_URL}/analyze", json={"topic": topic})
            analyze_data = response.json()
            st.session_state["results"] = analyze_data["results"]  # guardás

    if "results" in st.session_state:
        df_sentiments = pd.DataFrame(st.session_state["results"])
        df_result = df_sentiments["sentiment"].value_counts()
        st.divider()
        show_metrics(df_result)
        st.markdown("")
        show_chart(df_result)
        st.markdown("")
        show_articles(df_sentiments)


if __name__ == "__main__":
    main()
