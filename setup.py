from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cryptofapos",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Cryptocurrency Factor Analytics and Portfolio Optimization System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/CryptoFAPOS",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scipy>=1.7.0",
        "scikit-learn>=0.24.0",
        "statsmodels>=0.12.0",
        "yfinance>=0.1.63",
        "pykalman>=0.9.5",
    ],
)
