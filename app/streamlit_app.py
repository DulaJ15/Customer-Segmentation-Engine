import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.cluster_utils import preprocess_data, perform_clustering, reduce_dimensions

st.set_page_config(page_title="Customer Segmentation Engine", layout="wide")
st.title("🧠 Customer Segmentation Engine")

uploaded_file = st.file_uploader("Upload Customer Transaction CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

    with st.spinner("Preprocessing and Clustering in progress..."):
        preprocessed_df = preprocess_data(df)
        clustered_df, model = perform_clustering(preprocessed_df)
        reduced_df = reduce_dimensions(preprocessed_df)
        clustered_df[['PCA1', 'PCA2']] = reduced_df

    st.subheader("Clustered Customers (2D Projection)")
    fig, ax = plt.subplots()
    sns.scatterplot(
        x='PCA1', y='PCA2', hue='Cluster', palette='tab10', data=clustered_df, ax=ax
    )
    plt.title("Customer Segments")
    st.pyplot(fig)

    st.subheader("Cluster Summary Table")
    st.dataframe(clustered_df.groupby('Cluster').mean())

    st.success("Clustering Complete. Persona report generation coming next...")
else:
    st.info("Please upload a CSV file to begin.")
