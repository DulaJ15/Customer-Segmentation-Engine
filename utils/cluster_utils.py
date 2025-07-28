# utils/cluster_utils.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA


def preprocess_and_cluster(df, n_clusters=3):
    df = df.copy()
    df = df.dropna()

    numeric_features = ['Age', 'PurchaseFreq', 'TotalSpend']
    categorical_features = ['Region']

    # Transformers
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('cluster', KMeans(n_clusters=n_clusters, random_state=42))
    ])

    df['Cluster'] = pipeline.fit_predict(df)
    return df, pipeline


def reduce_dimensions(df, pipeline):
    features = pipeline.named_steps['preprocessor'].transform(df)
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(features)
    df['PCA1'] = reduced[:, 0]
    df['PCA2'] = reduced[:, 1]
    return df
