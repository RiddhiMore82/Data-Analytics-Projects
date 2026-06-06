import pandas as pd


class DataProfiler:

    @staticmethod
    def generate_profile(df):

        print("\n========== EDA REPORT ==========")

        print(f"\nRows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        print("\n========== NUMERICAL SUMMARY ==========")
        print(df.describe())

        print("\n========== MISSING VALUES ==========")
        print(df.isnull().sum())

        print("\n========== REVENUE SUMMARY ==========")
        print(df["Revenue"].describe())
        print("\nTotal Revenue:")
        print(f"${df['Revenue'].sum():,.2f}")

        print("\n========== TOP 10 COUNTRIES ==========")

        country_revenue = (
            df.groupby("Country")["Revenue"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        print(country_revenue)

        print("\n========== TOP 10 CUSTOMERS ==========")

        customer_revenue = (
            df.groupby("CustomerID")["Revenue"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        print(customer_revenue)