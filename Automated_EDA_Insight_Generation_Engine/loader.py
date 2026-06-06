import pandas as pd
from pathlib import Path


class DataLoader:
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load_data(self):
        """
        Load CSV or Excel file.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        suffix = self.file_path.suffix.lower()

        if suffix == ".csv":
            df = pd.read_csv(self.file_path)

        elif suffix in [".xlsx", ".xls"]:
            df = pd.read_excel(self.file_path)

        else:
            raise ValueError(
                f"Unsupported file format: {suffix}"
            )

        return df

    @staticmethod
    def dataset_info(df):
        print("\n========== DATASET INFO ==========")
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)