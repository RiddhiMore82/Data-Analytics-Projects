class InsightGenerator:

    @staticmethod
    def generate(cleaned_df, customer_df):

        insights = []

        # ==================================
        # Total Revenue
        # ==================================

        total_revenue = cleaned_df["Revenue"].sum()

        insights.append(
            f"Total revenue generated: "
            f"${total_revenue:,.2f}"
        )

        # ==================================
        # Country Analysis
        # ==================================

        country_revenue = (
            cleaned_df.groupby("Country")["Revenue"]
            .sum()
        )

        top_country = country_revenue.idxmax()

        top_country_pct = (
            country_revenue.max()
            / total_revenue
        ) * 100

        insights.append(
            f"{top_country} contributes "
            f"{top_country_pct:.1f}% of total revenue."
        )

        # ==================================
        # Cluster Summary
        # ==================================

        cluster_summary = (
            customer_df
            .groupby("Cluster")
            [["Recency", "Frequency", "Monetary"]]
            .mean()
        )

        # ==================================
        # VIP Customers
        # ==================================

        vip_cluster = (
            cluster_summary["Monetary"]
            .idxmax()
        )

        vip_customers = customer_df[
            customer_df["Cluster"] == vip_cluster
        ]

        vip_pct = (
            len(vip_customers)
            / len(customer_df)
        ) * 100

        insights.append(
            f"Cluster {vip_cluster} represents "
            f"{vip_pct:.1f}% of customers and "
            f"contains the highest-value buyers."
        )

        # ==================================
        # Dormant Customers
        # ==================================

        dormant_cluster = (
            cluster_summary["Recency"]
            .idxmax()
        )

        dormant_customers = customer_df[
            customer_df["Cluster"] == dormant_cluster
        ]

        dormant_pct = (
            len(dormant_customers)
            / len(customer_df)
        ) * 100

        insights.append(
            f"Cluster {dormant_cluster} represents "
            f"{dormant_pct:.1f}% of customers and "
            f"shows dormant purchasing behavior."
        )

        # ==================================
        # Pareto Analysis
        # ==================================

        sorted_customers = (
            customer_df
            .sort_values(
                by="Monetary",
                ascending=False
            )
        )

        top_n = max(
            1,
            int(len(sorted_customers) * 0.20)
        )

        top_revenue = (
            sorted_customers.head(top_n)
            ["Monetary"]
            .sum()
        )

        top_revenue_pct = (
            top_revenue
            / sorted_customers["Monetary"].sum()
        ) * 100

        insights.append(
            f"Top 20% of customers generate "
            f"{top_revenue_pct:.1f}% of total revenue."
        )

        # ==================================
        # Anomaly Detection Summary
        # ==================================

        anomaly_count = (
            customer_df["Anomaly"] == -1
        ).sum()

        anomaly_pct = (
            anomaly_count
            / len(customer_df)
        ) * 100

        insights.append(
            f"{anomaly_count} anomalous customers "
            f"were detected ({anomaly_pct:.2f}% of customers)."
        )

        metrics = {
            "total_revenue": round(
                total_revenue, 2
            ),
            "top_country": top_country,
            "top_country_pct": round(
                top_country_pct, 2
            ),
            "vip_cluster": int(
                vip_cluster
            ),
            "vip_customer_pct": round(
                vip_pct, 2
            ),
            "dormant_cluster": int(
                dormant_cluster
            ),
            "dormant_customer_pct": round(
                dormant_pct, 2
            ),
            "top_20pct_revenue_share": round(
                top_revenue_pct, 2
            ),
            "anomaly_count": int(
                anomaly_count
            ),
            "anomaly_pct": round(
                anomaly_pct, 2
            )
        }

        return insights, metrics