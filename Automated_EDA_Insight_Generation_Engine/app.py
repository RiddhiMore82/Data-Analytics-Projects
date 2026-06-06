from src.pipeline import run_pipeline


def main():

    results = run_pipeline(
        "data/Online Retail.xlsx"
    )

    print("\n========== INSIGHTS ==========\n")

    for insight in results["insights"]:
        print(f"• {insight}")

    print(
        f"\nReport: "
        f"{results['report_path']}"
    )

    print(
        f"Metrics: "
        f"{results['metrics_path']}"
    )


if __name__ == "__main__":
    main()