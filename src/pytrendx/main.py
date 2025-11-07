from VersaLog import *
from pprint import pprint
from datetime import datetime
from sklearn.linear_model import LinearRegression

import requests
import json
import argparse
import pypistats
import numpy as np
import matplotlib.pyplot as plt

logger = VersaLog(enum="simple2", tag="PSTATS", show_tag=True)

def fetch_overall(pkg: str):
    url = f"https://pypistats.org/api/packages/{pkg}/overall"
    req = requests.get(url)
    data = req.json()

    dataset = data.get("data", [])

    records = []
    for entry in dataset:
        date_value = entry.get("date")
        downloads = entry.get("downloads")

        if not date_value or downloads is None:
            continue

        try:
            records.append((datetime.strptime(date_value, "%Y-%m-%d"), downloads))
        except Exception:
            continue

    if not records:
        logger.warning("No valid records found for this package.")
    else:
        logger.info(f"{len(records)} records fetched successfully.\n")

    return records


def show_graph(pkg: str, records):
    dates, downloads = zip(*records)
    plt.figure(figsize=(10, 5))
    plt.plot(dates, downloads, marker="o", linestyle="-")
    plt.title(f"📈 PyPI Download Trend for '{pkg}'")
    plt.xlabel("Date")
    plt.ylabel("Downloads")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def analyze_stats(pkg: str, records):
    downloads = np.array([d[1] for d in records])
    avg = np.mean(downloads)
    median = np.median(downloads)
    stddev = np.std(downloads)
    total = np.sum(downloads)

    print(f"\n📊 Statistical Analysis for '{pkg}':")
    print("=" * 45)
    print(f"Total downloads: {total:,.0f}")
    print(f"Average:         {avg:,.2f}")
    print(f"Median:          {median:,.2f}")
    print(f"Std Deviation:   {stddev:,.2f}")
    print("=" * 45)


def predict_trend(pkg: str, records, days_ahead: int = 14):
    dates = np.arange(len(records)).reshape(-1, 1)
    downloads = np.array([d[1] for d in records])

    model = LinearRegression()
    model.fit(dates, downloads)

    future_dates = np.arange(len(records), len(records) + days_ahead).reshape(-1, 1)
    predictions = model.predict(future_dates)

    print(f"\n🔮 Predicted Downloads for '{pkg}' (next {days_ahead} days):")
    print("=" * 45)
    for i, pred in enumerate(predictions, 1):
        print(f"Day +{i}: {pred:,.0f} downloads")
    print("=" * 45)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, downloads, label="Actual", marker="o")
    plt.plot(future_dates, predictions, label="Predicted", linestyle="--", color="orange")
    plt.title(f"📉 Prediction for '{pkg}' (Next {days_ahead} Days)")
    plt.xlabel("Day")
    plt.ylabel("Downloads")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def PstatsGet():
    parser = argparse.ArgumentParser(
        prog="ptx",
        description="PyTrend - Fetch and visualize PyPI package download trends.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--get", metavar="PKG", help="Get PyPI stats for a package")
    parser.add_argument("--graph", metavar="PKG", help="Graph visualization of download trends")
    parser.add_argument("--analyze", metavar="PKG", help="Statistical analysis of downloads using NumPy")
    parser.add_argument("--predict", metavar="PKG", help="Predict future trends for a package")

    args = parser.parse_args()

    if args.get:
        try:
            pkg = args.get
            print(f"\n📦 Fetching PyPI stats for '{pkg}'...\n")
            data_str = pypistats.recent(pkg, "week", format="json")
            data = json.loads(data_str)

            print(f"📊 Download stats for '{pkg}':")
            print("=" * 40)
            print(f"Last day:   {data['data'].get('last_day', 'N/A')}")
            print(f"Last week:  {data['data'].get('last_week', 'N/A')}")
            print(f"Last month: {data['data'].get('last_month', 'N/A')}")
            print("=" * 40)

        except Exception as e:
            logger.error(e)

    elif args.graph:
        pkg = args.graph
        records = fetch_overall(pkg)
        show_graph(pkg, records)

    elif args.analyze:
        pkg = args.analyze
        records = fetch_overall(pkg)
        analyze_stats(pkg, records)

    elif args.predict:
        pkg = args.predict
        records = fetch_overall(pkg)
        predict_trend(pkg, records)

    else:
        parser.print_help()

if __name__ == "__main__":
    PstatsGet()