import streamlit as st

COLORS = {
    "positive": "#00C48C",  # verde
    "negative": "#FF4B4B",  # rojo
    "neutral": "#A0A0A0",  # gris
}


def personalizar():
    # Inyectamos el CSS personalizado
    st.markdown(
        """
        <style>
        /* 2. Estilo del botón (Grande y Visual) */
        .stButton > button {
            width: 150px;
            height: 60px;
            font-size: 16;
            font-weight: bold;
            color: black;
            background-color: #FF4B4B;
            border-radius: 15px;
            border: none;
            transition: all 0.2s ease; /* Transición suave */
        }

        /* 3. Efecto Hover (al pasar el mouse) */
        .stButton > button:hover {
            background-color: #FF7373;
            transform: scale(1.05); /* Se agranda un poquito */
        }

        /* 4. EFECTO AL CLICKAR (Pulsación) */
        .stButton > button:active {
            transform: scale(0.95); /* Se encoge al presionar */
            background-color: #D33636;
            box-shadow: inset 2px 2px 10px rgba(0,0,0,0.3); /* Sombra interna */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style>
        .stTextInput label p {
            font-size: 18px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
