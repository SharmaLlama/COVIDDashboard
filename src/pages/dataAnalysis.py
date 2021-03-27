import streamlit as st
from datetime import datetime, timedelta
from .utils.load_data import load_data
from pil import Image


def main():
    date = datetime.today()
    df = None
    while True:
        try:
            df = load_data(date)
        except Exception as e:
            date = date - timedelta(days=1)
            continue
        break

    if st.checkbox("Display raw data"):
        st.subheader('Raw data')
        st.write(df)
    st.subheader("The stats:")
    st.markdown("* Number of countries affected by the virus: **{}**".format(len(df["Country_Region"].unique())))
    st.markdown("* The virus has affected **{:.2f}M** people and caused **{:.2f}K** deaths.".format(df["Confirmed"].sum()/1000000,
                                                                                                df["Deaths"].sum()/1000))
    h_confirmed = df.groupby("Country_Region").agg({"Confirmed": "sum"}).nlargest(1,"Confirmed")
    st.markdown("* **{}** has the largest number of confirmed cases with **{:.2f}M** confirmed cases.".format(h_confirmed.index.values[0],
                                                                                      h_confirmed["Confirmed"].values[0]/1000000))

    h_confirmed_small = df.groupby("Country_Region").agg({"Confirmed": "sum"}).nsmallest(1,"Confirmed")
    st.markdown("* **{}** has the smallest number of confirmed cases with **{:.2f}M** confirmed cases.".format(h_confirmed_small.index.values[0],
                                                                                      h_confirmed_small["Confirmed"].values[0]/1000000))

    h_deaths = df.groupby("Country_Region").agg({"Deaths": "sum"}).nlargest(1,"Deaths")
    st.markdown("* **{}** has the largest number of deaths with **{:.2f}K** deaths.".format(h_deaths.index.values[0],
                                                                                                      h_deaths["Deaths"].values[0]/1000))

    h_deaths_small = df.groupby("Country_Region").agg({"Deaths": "sum"}).nlargest(1,"Deaths")
    st.markdown("* **{}** has the smallest number of deaths with **{:.2f}K** deaths.".format(h_deaths_small.index.values[0],
                                                                                                      h_deaths_small["Deaths"].values[0]/1000))
    h_recovered = df.groupby("Country_Region").agg({"Recovered": "sum"}).nlargest(1,"Recovered")
    st.markdown("* **{}** has the largest number of recoveries with **{:.2f}M** recovered.".format(h_recovered.index.values[0],
                                                                                           h_recovered["Recovered"].values[0]/1000000))