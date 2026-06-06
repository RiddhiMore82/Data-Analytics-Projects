from pathlib import Path

import matplotlib.pyplot as plt


class DataVisualizer:

    OUTPUT_DIR = Path("visualizations")

    @classmethod
    def create_directory(cls):
        cls.OUTPUT_DIR.mkdir(exist_ok=True)

    @classmethod
    def revenue_by_country(cls, df):

        cls.create_directory()

        country_revenue = (
            df.groupby("Country")["Revenue"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure(figsize=(10, 6))

        country_revenue.plot(kind="bar")

        plt.title("Top 10 Countries by Revenue")
        plt.ylabel("Revenue")
        plt.tight_layout()

        plt.savefig(
            cls.OUTPUT_DIR / "revenue_by_country.png"
        )

        plt.close()

    @classmethod
    def top_customers(cls, df):

        cls.create_directory()

        top_customers = (
            df.groupby("CustomerID")["Revenue"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure(figsize=(10, 6))

        top_customers.plot(kind="bar")

        plt.title("Top 10 Customers by Revenue")
        plt.ylabel("Revenue")
        plt.tight_layout()

        plt.savefig(
            cls.OUTPUT_DIR / "top_customers.png"
        )

        plt.close()

    @classmethod
    def revenue_distribution(cls, df):

        cls.create_directory()

        plt.figure(figsize=(10, 6))

        plt.hist(df["Revenue"], bins=50)

        plt.title("Revenue Distribution")
        plt.xlabel("Revenue")
        plt.ylabel("Frequency")

        plt.tight_layout()

        plt.savefig(
            cls.OUTPUT_DIR / "revenue_distribution.png"
        )

        plt.close()