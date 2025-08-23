import streamlit as st
import pandas as pd
import numpy as np

## Title of the aplication
st.title("Hello Streamlit")

## Display a Simple Text
st.write("This is a simple text")

## Create a simple DataFrame
df = pd.DataFrame({
  'first column': [1,2,3,4],
  'second column':[10,20,30,40]
})

## Display the Dataframe
st.write("Here is the dataFrame")
st.write(df)

## Create a linechart

chart_data=pd.DataFrame(
  np.random.randint(1,21,size=(20,3)),columns=['a','b','c']
)
st.line_chart(chart_data)

st.write(chart_data)