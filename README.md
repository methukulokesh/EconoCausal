# EconoCausal: Dynamic Pricing Using Double Machine Learning

**Internship Project | Data Science and Machine Learning | Infotact Solutions**

## 1. Project Overview

EconoCausal aims to analyze how product pricing affects customer demand using data analysis and causal machine learning. The project explores Double Machine Learning (DML) to estimate the effect of price while considering other relevant factors.

The goal is to build a decision-support system that helps compare pricing scenarios and understand their potential impact on demand and profitability.

## 2. Problem Statement

Product demand depends on several factors, including price, promotions, seasonality, and inventory. Analyzing historical sales alone may not be enough to understand the actual effect of price changes.

This project aims to combine demand prediction and causal analysis to support better pricing decisions using available retail data.

## 3. Project Objectives

- Clean and preprocess the dataset.
- Perform exploratory data analysis (EDA).
- Build a baseline demand-prediction model.
- Apply Double Machine Learning to estimate price effects, where supported by the data.
- Compare alternative pricing scenarios.
- Analyze potential revenue and profitability.
- Develop an interactive dashboard to present the results.

## 4. Dataset

The project will use a suitable retail dataset containing pricing and sales information.

The dataset will be inspected for missing values, duplicates, data types, and relevant variables before model development. The final dataset source and available columns will be documented after verification.

## 5. Technology Stack

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Causal Analysis:** EconML or DoubleML
- **Dashboard:** Streamlit
- **Version Control:** Git and GitHub

## 6. Project Workflow

1. Environment setup and dataset inspection.
2. Data cleaning and preprocessing.
3. Exploratory data analysis.
4. Demand prediction and model evaluation.
5. Double Machine Learning implementation.
6. Pricing scenario analysis.
7. Dashboard development and final documentation.

## 7. Project Structure

```text
EconoCausal/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── reports/
├── outputs/
├── requirements.txt
├── README.md
└── .gitignore
```

## 8. Current Progress

- Initial project environment configured.
- Core data science libraries tested.
- EconML import verified.
- Initial project documentation prepared.

## 9. Limitations

The reliability of causal estimates depends on data quality, relevant control variables, and the assumptions used in the analysis. Pricing scenarios will be treated as estimates for decision support rather than guaranteed business outcomes.

## 10. Development Plan

The project will be developed step by step, with regular GitHub commits, daily progress updates, testing, and documentation of the results.