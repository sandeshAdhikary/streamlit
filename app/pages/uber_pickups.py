import streamlit as st
import pandas as pd
import numpy as np

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


if __name__ == "__main__":
    st.title("Uber pickups in NYC")
    data_load_state = st.text("Loading data...")
    with st.spinner():
        data = load_data(10000)
    data_load_state.text("Done!")

    st.subheader('Raw Data')
    st.dataframe(data)

    st.subheader('Number of pickups by hour')
    bins = st.slider("Bins", 1, 100)
    hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=bins, range=(0,24))[0]
    st.bar_chart(hist_values)

    