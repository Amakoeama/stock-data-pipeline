# Stock Data Engineering Pipeline

## Overview
This project implements a data engineering pipeline to process historical stock market data.

## Dataset
Source: Kaggle S&P 500 dataset

## Pipeline Steps
- Data loading
- Filtering selected companies
- Data cleaning (duplicates, missing values)
- Data transformation
- Feature engineering (daily returns, moving averages)

## Output
Cleaned dataset: `output/cleaned_stock_data.csv`

## How to Run

```bash
python3 src/capstone_stock_pipeline.py
