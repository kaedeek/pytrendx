## What is PyTrendx?

[![PyPI version](https://badge.fury.io/py/pytrendx.svg)](https://badge.fury.io/py/pytrendx)
[![Downloads](https://pepy.tech/badge/pytrendx)](https://pepy.tech/project/pytrendx)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Support%20Server-7289DA?style=flat&logo=discord)](https://discord.gg/x7re7gbu)

`PyTrendx` is a **modern CLI tool** that allows you to easily fetch, visualize, analyze, and predict **PyPI package download statistics** directly from your terminal.

It combines **pypistats**, **matplotlib**, **NumPy**, and **scikit-learn** to make data analysis effortless — right from your console.

---

## Features

- Fetch PyPI download stats (`--get`)
- Graph visualization of download trends (`--graph`)
- Statistical analysis using NumPy (`--analyze`)
- Predict future download trends with machine learning (`--predict`)

---

## Installation

```bash
pip install pytrendx
```

## Usage

### Fetch current download stats
```bash
ptx --get pillow
```

```bash
📦 Fetching PyPI stats for 'pillow'...

📊 Download stats for 'pillow':
========================================
Last day:   N/A
Last week:  53472343
Last month: N/A
========================================
```

### Graph download trends
```bash
ptx --graph pillow
```

![graph](/image/res/graph.png)

### Analyze download statistics
```bash
ptx --analyze pillow
```

```bash
📊 Statistical Analysis for 'pillow':
=============================================
Total downloads: 2,252,527,225
Average:         6,222,450.90
Median:          6,421,581.00
Std Deviation:   1,608,374.11
=============================================
```

### Predict future trends
```bash
ptx --predict pillow
```

```bash
🔮 Predicted Downloads for 'pillow' (next 14 days):
=============================================
Day +1: 6,912,699 downloads
Day +2: 6,916,502 downloads
Day +3: 6,920,305 downloads
Day +4: 6,924,108 downloads
Day +5: 6,927,911 downloads
Day +6: 6,931,714 downloads
Day +7: 6,935,517 downloads
Day +8: 6,939,320 downloads
Day +9: 6,943,123 downloads
Day +10: 6,946,926 downloads
Day +11: 6,950,729 downloads
Day +12: 6,954,532 downloads
Day +13: 6,958,335 downloads
Day +14: 6,962,138 downloads
=============================================
```

![predict](/image/res/predict.png)