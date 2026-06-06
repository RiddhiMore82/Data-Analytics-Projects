from sklearn.ensemble import IsolationForest


class AnomalyDetector:

    @staticmethod
    def detect(customer_df):

        features = customer_df[
            ["Frequency", "Monetary"]
        ]

        model = IsolationForest(
            contamination=0.02,
            random_state=42
        )

        customer_df["Anomaly"] = (
            model.fit_predict(features)
        )

        return customer_df