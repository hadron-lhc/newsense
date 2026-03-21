import streamlit as st
import requests
from custom import personalizar, COLORS
import pandas as pd

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


def main():
    header()
    topic = st.text_input(label="Ingrese una tematica")
    if st.button("Analizar"):
        requests.get("http://localhost:8000/news", params={"topic": topic})
        response = requests.post("http://localhost:8000/analyze", json={"topic": topic})
        analyze_data = response.json()
        df_sentiments = pd.DataFrame(analyze_data["results"])
        df_result = df_sentiments["sentiment"].value_counts()
        st.divider()
        show_metrics(df_result)


if __name__ == "__main__":
    main()
