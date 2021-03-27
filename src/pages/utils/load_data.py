import pandas as pd
import streamlit as st


def load_data(date, rows=None, country=None):
    DATA_URL = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/"
                "csse_covid_19_daily_reports/{}.csv".format(date.date().strftime("%m-%d-%Y")))

    if country == "US":
        DATA_URL = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/"
                    "csse_covid_19_daily_reports_us/{}.csv".format(date.date().strftime("%m-%d-%Y")))

    df = pd.read_csv(DATA_URL, nrows=rows)

    return df
