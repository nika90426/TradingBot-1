from setuptools import setup, find_namespace_packages
import os

setup(
    name="TradingBot",
    version="1.2.0",
    python_requires=">=3",
    package_dir={"": "tradingbot"},
    packages=find_namespace_packages(where="tradingbot"),
    scripts=["tradingbot/TradingBot.py"],
    entry_points={"console_scripts": ["trading_bot = TradingBot:main"]},
    install_requires=[
        "alpha-vantage==2.2.0",
        "govuk-bank-holidays==0.8",
        "numpy==1.19.0",
        "pandas==1.0.5",
        "pytz==2020.1",
        "requests==2.24.0",
        "scipy==1.5.0",
        "yfinance==0.1.54",
    ],
    package_data={"config": ["*.json"]},
    data_files=[
        (os.path.join(os.sep, "opt", "TradingBot", "config"), ["config/config.json"])
    ],
    # metadata to display on PyPI
    author="Alberto Cardellini",
    author_email="",
    description="Autonomous market trading script",
    keywords="trading stocks finance",
    url="https://github.com/ilcardella/TradingBot",
    project_urls={
        "Bug Tracker": "https://github.com/ilcardella/TradingBot/issues",
        "Documentation": "https://tradingbot.readthedocs.io",
        "Source Code": "https://github.com/ilcardella/TradingBot",
    },
    classifiers=["License :: OSI Approved :: MIT License"],
)
