import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


class CustomerSegmenter:

    @staticmethod
    def create_customer_features(df):
        df["InvoiceDate"] = pd.to_datetime(
            df["InvoiceDate"]
        )

        reference_date = (
            df["InvoiceDate"].max()
        )

        customer_df = (
            df.groupby("CustomerID")
            .agg(
                Recency=(
                    "InvoiceDate",
                    lambda x: (
                        reference_date - x.max()
                    ).days
                ),
                Frequency=(
                    "InvoiceNo",
                    "nunique"
                ),
                Monetary=(
                    "Revenue",
                    "sum"
                )
            )
            .reset_index()
        )

        return customer_df

    @staticmethod
    def perform_clustering(customer_df):

        features = customer_df[
            [
            "Recency",
            "Frequency",
            "Monetary"
            ]
        ]

        scaler = StandardScaler()

        scaled_features = scaler.fit_transform(features)

        kmeans = KMeans(
            n_clusters=4,
            random_state=42,
            n_init=10
        )

        customer_df["Cluster"] = (
            kmeans.fit_predict(scaled_features)
        )

        return customer_df  
    
    @staticmethod
    def get_cluster_summary(customer_df):

        return (
            customer_df
            .groupby("Cluster")
            [
                [   "Recency",
                    "Frequency",
                    "Monetary"
                ]
            ]
            .mean()
        )