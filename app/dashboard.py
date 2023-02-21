import streamlit as st

st.title("Air Quality Index in the United States!")

st.write("Here is the Air Quality Index of the United States:")
st.image("..\data.png")

st.write("")

st.write("The safety level distribution for the Air Quality in the United States:")
st.image("..\AQIStatus.png")

st.write("")

st.write("The rolling mean graph of the AQI Levels in the US:")
st.image(r"..\rolling.png")

st.write("")

st.write("The Time Series Forecast in the next 100 days:")
st.image("..\TimeSeriesDay.png")

st.write("")

st.write("The Time Series Forecast in the next 100 months:")
st.image("..\TimeSeriesMonth.png")
