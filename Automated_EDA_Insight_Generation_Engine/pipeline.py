from src.loader import DataLoader
from src.cleaner import DataCleaner
from src.profiler import DataProfiler
from src.visualizer import DataVisualizer
from src.segmenter import CustomerSegmenter
from src.anomaly_detector import AnomalyDetector
from src.insight_generator import InsightGenerator
from src.report_builder import ReportBuilder
from src.metrics_exporter import MetricsExporter


def run_pipeline(file_path):

    loader = DataLoader(file_path)

    df = loader.load_data()

    cleaned_df = DataCleaner.clean(df)

    DataProfiler.generate_profile(cleaned_df)

    DataVisualizer.revenue_by_country(cleaned_df)
    DataVisualizer.top_customers(cleaned_df)
    DataVisualizer.revenue_distribution(cleaned_df)

    customer_df = (
        CustomerSegmenter.create_customer_features(
            cleaned_df
        )
    )

    customer_df = (
        CustomerSegmenter.perform_clustering(
            customer_df
        )
    )

    customer_df = (
        AnomalyDetector.detect(
            customer_df
        )
    )

    insights, metrics = (
        InsightGenerator.generate(
            cleaned_df,
            customer_df
        )
    )

    report_path = (
        ReportBuilder.build_html_report(
            insights
        )
    )

    metrics_path = (
        MetricsExporter.export_metrics(
            metrics
        )
    )

    return {
        "cleaned_df": cleaned_df,
        "customer_df": customer_df,
        "insights": insights,
        "metrics": metrics,
        "report_path": report_path,
        "metrics_path": metrics_path,

        "charts": {
            "country": "visualizations/revenue_by_country.png",
            "customers": "visualizations/top_customers.png",
            "revenue": "visualizations/revenue_distribution.png"
        }
    }