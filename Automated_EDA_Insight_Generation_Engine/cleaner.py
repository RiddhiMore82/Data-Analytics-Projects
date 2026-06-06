import pandas as pd


class DataCleaner:

    @staticmethod
    def basic_summary(df):
        """
        Display data quality metrics.
        """

        print("\n========== DATA QUALITY REPORT ==========")

        print(f"Total Rows: {len(df)}")

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    @staticmethod
    def clean(df):
        """
        Perform basic cleaning.
        """

        cleaned_df = df.copy()

    # Remove duplicates
        cleaned_df = cleaned_df.drop_duplicates()

    # Remove rows without customer ID
        cleaned_df = cleaned_df.dropna(subset=["CustomerID"])

    # Remove negative or zero quantity
        cleaned_df = cleaned_df[cleaned_df["Quantity"] > 0]

    # Remove negative or zero price
        cleaned_df = cleaned_df[cleaned_df["UnitPrice"] > 0]

    # Remove cancelled invoices
        cleaned_df = cleaned_df[
        ~cleaned_df["InvoiceNo"].astype(str).str.startswith("C")
    ]

    # Create revenue column
        cleaned_df["Revenue"] = (
        cleaned_df["Quantity"] * cleaned_df["UnitPrice"]
    )

        return cleaned_df
