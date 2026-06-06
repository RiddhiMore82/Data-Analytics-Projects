from pathlib import Path


class ReportBuilder:

    REPORT_DIR = Path("reports")

    @classmethod
    def build_html_report(
        cls,
        insights
    ):

        cls.REPORT_DIR.mkdir(
            exist_ok=True
        )

        html_content = f"""
        <html>
        <head>
            <title>EDA Report</title>
        </head>

        <body>

            <h1>
                Automated EDA & Insight Report
            </h1>

            <h2>
                Business Insights
            </h2>

            <ul>
                {''.join([f'<li>{i}</li>' for i in insights])}
            </ul>

            <h2>
                Visualizations
            </h2>

            <img
                src="../visualizations/revenue_by_country.png"
                width="700"
            >

            <br><br>

            <img
                src="../visualizations/top_customers.png"
                width="700"
            >

            <br><br>

            <img
                src="../visualizations/revenue_distribution.png"
                width="700"
            >

        </body>
        </html>
        """

        report_path = (
            cls.REPORT_DIR /
            "eda_report.html"
        )

        with open(
            report_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html_content)

        return report_path