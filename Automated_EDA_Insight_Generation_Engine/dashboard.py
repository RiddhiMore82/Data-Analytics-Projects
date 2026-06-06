import streamlit as st

from src.pipeline import run_pipeline


st.set_page_config(
    page_title="Automated EDA Engine",
    layout="wide"
)

st.title("📊 Automated EDA & Insight Engine")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    temp_path = f"temp_{uploaded_file.name}"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Running analytics pipeline..."):

        results = run_pipeline(temp_path)

    metrics = results["metrics"]

    st.success("Analysis Complete")

    # =========================
    # KPI SECTION
    # =========================

    st.header("📈 Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Revenue",
            f"${metrics['total_revenue']:,.0f}"
        )

    with col2:
        st.metric(
            "Top Country",
            metrics["top_country"]
        )

    with col3:
        st.metric(
            "Anomalies",
            metrics["anomaly_count"]
        )

    # =========================
    # INSIGHTS
    # =========================

    st.header("💡 Business Insights")

    for insight in results["insights"]:
        st.write(f"• {insight}")

    # =========================
    # CHARTS
    # =========================

    st.header("📊 Visualizations")

    st.image(
        results["charts"]["country"]
    )

    st.image(
        results["charts"]["customers"]
    )

    st.image(
        results["charts"]["revenue"]
    )

    # =========================
    # DATA PREVIEW
    # =========================

    st.header("📋 Cleaned Dataset Preview")

    st.dataframe(
        results["cleaned_df"].head(20)
    )

    # =========================
    # DOWNLOAD LINKS
    # =========================

    st.header("📄 Generated Files")

    st.write(
        f"HTML Report: "
        f"{results['report_path']}"
    )

    st.write(
        f"Metrics JSON: "
        f"{results['metrics_path']}"
    )