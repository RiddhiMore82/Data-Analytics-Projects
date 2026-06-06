import json
from pathlib import Path


class MetricsExporter:

    REPORT_DIR = Path("reports")

    @classmethod
    def export_metrics(
        cls,
        metrics
    ):

        cls.REPORT_DIR.mkdir(
            exist_ok=True
        )

        output_file = (
            cls.REPORT_DIR /
            "insights.json"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                metrics,
                file,
                indent=4
            )

        return output_file