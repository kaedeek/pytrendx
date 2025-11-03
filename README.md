## What is PyTrendx?

[![PyPI version](https://badge.fury.io/py/pytrendx.svg)](https://badge.fury.io/py/pytrendx)
[![Downloads](https://pepy.tech/badge/pytrendx)](https://pepy.tech/project/pytrendx)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Support%20Server-7289DA?style=flat&logo=discord)](https://discord.gg/MaWeRFxa)

`PyTrendx` is a CLI tool that allows you to easily fetch PyPI package download statistics and view trends directly from your terminal.

---

## Features

- Current: Fetch PyPI download stats for a specific package
- Planned features:
  - Graph visualization of download trends (`--graph`)
  - Statistical analysis of downloads using NumPy (`--analyze`)
  - Predict future trends (`--predict`)

---

## Installation

```bash
pip install pytrendx
```

## Usage
```bash
ptx --get pillow
```