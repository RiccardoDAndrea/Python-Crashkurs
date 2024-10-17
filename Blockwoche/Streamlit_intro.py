import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Python Crash Kurs",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Welcome to my Page")

# File uploader
upload_file = st.sidebar.file_uploader("Upload your data", type=["csv"])

# Separator selection
file_separator = st.sidebar.selectbox("Pick your separator", 
                                      [",", ";", ":", " "])

# Check if a file is uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file, 
                     sep=file_separator)

else:
    df = None
    st.sidebar.info('Please upload your dataset')
    st.info(""" **Start by uploading your own data or using the data stored for you.** 📁""")
    st.stop()

    

# General Information about the data
# Display the DataFrame
st.subheader("Your DataFrame: ")
st.dataframe(df, use_container_width=True)
st.divider()

##Contiune with VIS


        