import pil
import streamlit as st
import src.pages.about
import src.pages.dataAnalysis
import src.pages.dashboard
import src.pages.homePage

PAGE_PY = {
    "Home": src.pages.homePage,
    "About": src.pages.about,
    "Statistics About COVID": src.pages.dataAnalysis,
    "Dashboard": src.pages.dashboard
}


def main():
    st.sidebar.title("Menu")
    choices = st.sidebar.radio("Navigate", list(PAGE_PY.keys()))
    PAGE_PY[choices].main()
    st.sidebar.title("About")
    st.sidebar.info("""
    This simple dashboard is maintained by Utkarsh Sharma. You can learn more about me at [https://github.com/SharmaLlama]. """)


if __name__ == "__main__":
    main()
