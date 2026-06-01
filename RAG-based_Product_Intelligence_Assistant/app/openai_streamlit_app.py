import os
import streamlit as st
import pandas as pd

from dotenv import load_dotenv

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from langchain_openai import ChatOpenAI

# -----------------------------------
# LOAD ENV VARIABLES
# -----------------------------------

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Product Intelligence Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Product Intelligence Assistant")

st.markdown(
    """
    Ask intelligent business questions about:
    - customers
    - industries
    - products
    - profits
    - sales performance
    """
)

# -----------------------------------
# LOAD DATASET
# -----------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("data/AWS_SaaS_Sales.csv")

    documents = []

    for _, row in df.iterrows():

        text = f"""
        Customer: {row['Customer']}
        Industry: {row['Industry']}
        Product: {row['Product']}
        Region: {row['Region']}
        Sales: {row['Sales']}
        Profit: {row['Profit']}
        """

        documents.append(text)

    return documents

documents = load_data()

# -----------------------------------
# CREATE TF-IDF VECTORS
# -----------------------------------

@st.cache_resource
def create_vectors(documents):

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    return vectorizer, tfidf_matrix

vectorizer, tfidf_matrix = create_vectors(documents)

# -----------------------------------
# LOAD OPENAI MODEL
# -----------------------------------

@st.cache_resource
def load_llm():

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3
    )

    return llm

llm = load_llm()

# -----------------------------------
# USER INPUT
# -----------------------------------

query = st.text_input(
    "Enter your business question:",
    placeholder="Example: Which industries generate the highest profits?"
)

# -----------------------------------
# GENERATE RESPONSE
# -----------------------------------

if st.button("Generate Insights"):

    if query.strip() == "":

        st.warning("Please enter a business question.")

    else:

        with st.spinner("Analyzing business records..."):

            # Transform query
            query_vector = vectorizer.transform([query])

            # Similarity search
            similarities = cosine_similarity(
                query_vector,
                tfidf_matrix
            )

            # Top records
            top_indices = similarities[0].argsort()[-5:][::-1]

            retrieved_docs = "\n".join(
                [documents[idx] for idx in top_indices]
            )

            # Prompt
            prompt = f"""
            You are an expert Product Intelligence Assistant.

            Use ONLY the provided business records.

            BUSINESS RECORDS:
            {retrieved_docs}

            USER QUESTION:
            {query}

            Provide:

            1. Executive Summary
            2. Key Business Insights
            3. Strategic Recommendation

            Keep the response concise, professional, and data-driven.
            """

            # Generate response
            response = llm.invoke(prompt)

            # Display AI response
            st.subheader("📌 AI Business Insights")

            st.markdown(response.content)

            # Expandable records section
            with st.expander("View Retrieved Business Records"):

                st.text(retrieved_docs)