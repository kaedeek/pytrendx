from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pytrendx",
    version="1.0.3",
    description="Fetch and visualize PyPI package download trends directly from the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="kaede",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "VersaLog",
        "pypistats",
        "matplotlib",
        "numpy",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "ptx = main:PstatsGet"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Developers",
    ],
)
