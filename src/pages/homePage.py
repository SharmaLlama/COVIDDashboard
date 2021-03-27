import pil
from pil import Image
import streamlit as st


def main():
    img = Image.open("img.png")
    st.image(img)
    st.title("COVID-19 Dashboard")

    st.write("""
    This simple application will help to keep track of the COVID-19 virus that is spreading across the world. It was first 
    discovered in December 2019 in the province of Wuhan, China.""")
    st.markdown("## Symptoms")
    st.markdown("### Most Common Symptoms:")
    st.markdown("* Fevers \n * Dry Coughs \n * Tiredness")
    st.markdown("### Less Common Symptoms:")
    st.markdown("* aches and pains \n * sore throat \n * diarrhoea \n * conjunctivitis \n"
                "* headache \n * loss of taste or smell")
