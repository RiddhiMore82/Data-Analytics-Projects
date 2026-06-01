import pandas as pd

# Load dataset
df = pd.read_csv("data/SaaS-Sales.csv")

# Keep only important columns
df = df[
    [
        "Order Date",
        "Customer",
        "Industry",
        "Segment",
        "Product",
        "Country",
        "Region",
        "Sales",
        "Quantity",
        "Profit"
    ]
]

# Convert each row into business text
documents = []

for _, row in df.iterrows():

    text = f"""
    Order Date: {row['Order Date']}
    Customer: {row['Customer']}
    Industry: {row['Industry']}
    Segment: {row['Segment']}
    Product: {row['Product']}
    Country: {row['Country']}
    Region: {row['Region']}
    Sales: {row['Sales']}
    Quantity: {row['Quantity']}
    Profit: {row['Profit']}
    """

    documents.append(text)

# Preview first 3 documents
for doc in documents[:3]:
    print(doc)
    print("=" * 50)