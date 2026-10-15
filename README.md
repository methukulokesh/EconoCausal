# EconoCausal: Dynamic Pricing Using Double Machine Learning

**Internship Project | Data Science and Machine Learning | Infotact Solutions**

## 1. Project Overview

EconoCausal is a data-driven project that explores how product prices affect customer demand. It aims to use data analysis and causal machine learning to understand pricing patterns and compare different pricing strategies.

The project will explore Double Machine Learning (DML) to estimate price effects while considering other relevant factors, depending on the quality and suitability of the available data.

## 2. Problem Statement

Retail businesses need to choose prices that balance customer demand and profitability. However, sales can also be affected by inventory levels, seasonality, and other factors. Therefore, historical sales data alone may not explain the actual effect of a price change.

This project aims to analyze retail data, study the relationship between price and demand, and explore how causal analysis can support better pricing decisions.

## 3. Project Objectives

- Clean and preprocess the retail dataset.
- Perform exploratory data analysis (EDA).
- Identify patterns in prices, sales, and demand.
- Build a baseline demand-prediction model.
- Explore DML for estimating the effect of price changes.
- Compare alternative pricing scenarios.
- Analyze potential revenue and profitability.
- Develop an interactive dashboard to present the results.
- Evaluate model performance and document limitations.

## 4. Dataset

**Dataset:** Retail Store Inventory and Demand Forecasting  
**Format:** CSV

The selected dataset contains retail sales, inventory, and demand-related information.

**Main columns:**
- `Date` — Date of the record
- `Store ID` — Store identifier
- `Product ID` — Product identifier
- `Category` — Product category
- `Region` — Store region
- `Inventory Level` — Inventory available
- `Units Sold` — Number of units sold
- `Units Ordered` — Number of units ordered
- `Demand Forecast` — Forecasted demand
- `Price` — Product price

The dataset will be checked for data quality, price variation, and relevant variables before model development.

## 5. Technology Stack

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Causal Analysis:** EconML or DoubleML
- **Dashboard:** Streamlit
- **Version Control:** Git and GitHub

## 6. Project Workflow

1. Set up the Python environment and inspect the dataset.
2. Clean and preprocess the data.
3. Perform exploratory data analysis.
4. Analyze price and demand patterns.
5. Build and evaluate a baseline demand model.
6. Explore DML and validate its assumptions, if the data supports causal analysis.
7. Compare pricing scenarios and potential business outcomes.
8. Develop the dashboard and document the results.

## 7. Planned Features

- Retail data analysis and visualizations.
- Demand prediction using machine learning.
- Price-effect estimation using DML, where appropriate.
- What-if pricing scenario comparisons.
- Revenue and profitability analysis.
- An interactive dashboard for displaying findings.

## 8. Project Structure

```text
EconoCausal/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── reports/
│   └── daily-logs/
├── outputs/
│   └── figures/
├── requirements.txt
├── README.md
└── .gitignore
```

## 9. Current Progress

- Created the initial project folder structure.
- Set up and activated the Python virtual environment.
- Installed and tested the core data science libraries.
- Verified the EconML import.
- Generated `requirements.txt`.
- Created and tested the environment verification script.
- Selected the retail inventory dataset.
- Created the initial dataset inspection script.
- Connected the GitHub repository to the Infotact project progress dashboard.

## 10. Limitations

The results will depend on the quality of the dataset and the variables available for analysis. Factors such as promotions and competitor prices are not included in the selected dataset, which may limit the reliability of causal estimates.

Predicting demand does not necessarily prove that a price change causes demand to change. Any causal estimates and pricing scenarios will therefore be evaluated carefully and presented with their limitations.

## 11. Development Plan

The project will be developed step by step, starting with dataset validation and exploratory analysis, followed by model development, pricing scenario analysis, and dashboard implementation.

Progress will be maintained through meaningful GitHub commits, dated daily logs, testing, and documentation.