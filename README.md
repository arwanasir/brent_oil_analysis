# Brent Oil Price Analysis: Change Point Detection

## 📌 Project Overview

This project is conducted for **Birhan Energies**, a strategic consultancy firm. The goal is to analyze the impact of significant geopolitical and economic events on **Brent Oil Prices** (1987 - 2022) using advanced statistical modeling and Bayesian Change Point Analysis.

The analysis seeks to move beyond simple correlation, using probabilistic modeling to identify structural breaks in market regimes and quantify the impact of global shocks.

## Project Structure

```text
brent_oil_analysis/
├── .github/workflows/
│   └── unittests.yml       # CI/CD Pipeline for automated testing
├── data/
│   ├── raw/                # Original Brent Oil Price CSV
│   └── processed/          # Generated researched_events.csv
├── notebooks/
│   ├── task_1_eda.ipynb    # Task 1: EDA & Geopolitical Research
│   └── task_2_model_engine.ipynb # Task 2: Bayesian Modeling & Inference
├── src/
│   ├── __init__.py
│   ├── analysis_utils.py   # Modular logic for EDA and Stats
│   └── model_engine.py     # PyMC Model definitions for Task 2
├── tests/
│   └── test_analysis.py    # Unit tests for data processing
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```
