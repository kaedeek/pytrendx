from VersaLog import *
from pprint import pprint

import json
import argparse
import pypistats

logger = VersaLog(enum="simple2", tag="PSTATS", show_tag=True)

def PstatsGet():
    parser = argparse.ArgumentParser(
        prog="ptx",
        description="PyTrend - Fetch and visualize PyPI package download trends.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--get", metavar="PKG", help="Get PyPI download stats for a package (example: --get pillow)")

    args = parser.parse_args()

    if args.get:
        try:
            if args.get:
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

    else:
        parser.print_help()

if __name__ == "__main__":
    PstatsGet()