# Brent Oil Price Analysis: Change Point Detection & Interactive Dashboard

## 📌 Project Overview

This project was developed for **Birhan Energies** to analyze how significant geopolitical and economic events influence **Brent Oil Prices**. By combining historical data (1987-2022) with **Bayesian Change Point Analysis**, we quantify the impact of global shocks—such as the 2008 financial crisis, the 2014 OPEC price war, and the COVID-19 pandemic—on market regimes.

The project transitions from raw data exploration to advanced probabilistic modeling, culminating in a full-stack web dashboard for stakeholder visualization.

## 🚀 Key Features

- **Time-Series Analysis:** Comprehensive EDA of 30+ years of oil price data to identify trends and seasonalities.
- **Bayesian Inference:** Structural break detection using **PyMC** to find "switch points" in price regimes.
- **Statistical Quantification:** Calculation of mean shifts ($\mu_1 \rightarrow \mu_2$) and volatility changes post-event.
- **Interactive Dashboard:** A full-stack application (Flask + React) for stakeholders to explore event impacts dynamically with date filtering and event highlighting.

## 📂 Project Structure

```text
brent_oil_analysis/
├── dashboard/               # Task 3: Full-stack Dashboard
│   ├── backend/             # Flask API serving analysis results
│   │   ├── app.py           # API Endpoints
│   │   └── data_provider.py # Data handling logic
│   └── frontend/            # React + Recharts interactive UI
├── data/
│   ├── raw/                 # Original Brent Oil Price CSV
│   └── processed/           # Quantified event data and researched_events.csv
├── notebooks/
│   ├── task_1_eda.ipynb     # Task 1: EDA & Geopolitical Research
│   └── task_2_model.ipynb   # Task 2: Bayesian Modeling & Inference
├── src/
│   ├── analysis_utils.py    # Modular logic for EDA
│   └── model_engine.py      # PyMC Model definitions for Task 2
├── tests/                   # Unit tests for CI/CD pipeline
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 🛠️ Tech Stack

- **Data Science**: Python (Pandas, NumPy, Scipy)

- **Probabilistic Modeling**: PyMC (MCMC Sampling)

- **Backend**: Flask, Flask-CORS

- **Frontend**: React.js, Recharts, Axios

- **DevOps**: GitHub Actions (CI/CD)

## Dashboard Setup & Usage

- **1. Backend (Flask)**
  The backend serves the processed analysis data via RESTful endpoints.

```bash
cd dashboard/backend
# Ensure dependencies are installed
pip install flask flask-cors pandas
python app.py
```

- **2. Frontend (React)**
  The frontend provides an interactive UI to visualize the price shifts.

```bash
cd dashboard/frontend
npm install
npm start
```

Open http://localhost:3000 to view the interactive charts.

## Analysis Results

- **2008 Global Financial Crisis**: Identified as a major structural break with a sharp decline in mean price and a spike in volatility.

- **2014 OPEC Policy Shift**: The model detected a clear transition from a sustained high-price regime ($100+) to a lower-price regime (~$50).

- **2020 COVID-19 Lockdown**: Captured the unprecedented price drop and subsequent "volatility clustering" during the global recovery phase.
