import pandas as pd

# Load dataset
df = pd.read_csv("data/SaaS-Sales.csv")

# Basic info
print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATASET SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDATA TYPES:")
print(df.dtypes)