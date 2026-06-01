import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from langchain_ollama import OllamaLLM

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Product Intelligence Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 RAG-Based Product Intelligence Assistant")

st.markdown(
    "Ask business questions about customers, products, sales, profits, and industries."
)

# ---------------------------------
# LOAD DATASET
# ---------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("data/SaaS-Sales.csv")

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

# ---------------------------------
# CREATE TF-IDF VECTORS
# ---------------------------------

@st.cache_resource
def create_vectors(documents):

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    return vectorizer, tfidf_matrix

vectorizer, tfidf_matrix = create_vectors(documents)

# ---------------------------------
# LOAD LLM
# ---------------------------------

@st.cache_resource
def load_llm():

    llm = OllamaLLM(model="tinyllama")

    return llm

llm = load_llm()

# ---------------------------------
# USER INPUT
# ---------------------------------

query = st.text_input(
    "Enter your business question:",
    placeholder="Example: Which industries generate the highest profits?"
)

# ---------------------------------
# PROCESS QUERY
# ---------------------------------

if st.button("Generate Insights"):

    if query.strip() == "":

        st.warning("Please enter a business question.")

    else:

        with st.spinner("Analyzing business records..."):

            # Query vector
            query_vector = vectorizer.transform([query])

            # Similarity search
            similarities = cosine_similarity(
                query_vector,
                tfidf_matrix
            )

            # Top matches
            top_indices = similarities[0].argsort()[-3:][::-1]

            retrieved_docs = "\n".join(
                [documents[idx] for idx in top_indices]
            )

            # Prompt
            prompt = f"""
            You are a Product Intelligence Assistant.

            Use the business records below to answer the question.

            Business Records:
            {retrieved_docs}

            Question:
            {query}

            Provide a clear and concise business insight.
            """

            # LLM response
            response = llm.invoke(prompt)

            # Output
            st.subheader("📌 AI Business Insight")

            st.write(response)

            # Retrieved records
            with st.expander("View Retrieved Business Records"):

                st.text(retrieved_docs)