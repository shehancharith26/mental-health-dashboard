# Mental Health & Stress Level Prediction Platform

An AI-powered diagnostic and predictive system that analyzes lifestyle, workplace dynamics, and demographic factors to evaluate mental health conditions and stress levels.

## Features
- **Exploratory Data Analysis (EDA):** Insights into how work hours, sleep, and physical activity impact mental health.
- **Predictive Machine Learning Models:** Linear Regression & Random Forest models to forecast mental health scores.
- **Risk Level Assessment:** Evaluates employee stress levels (Low, Moderate, High) based on composite workplace factors.
- **Feature Importance Analysis:** Highlights key drivers influencing employee burnout and mental well-being.

## Tech Stack
- **Language:** Python 3.x
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn
- **Data Visualization:** Matplotlib, Seaborn
- **Environment:** Google Colab / Jupyter Notebook

## Dataset Overview
The model uses demographic, professional, and lifestyle metrics:
- **Demographics & Work:** Age, Gender, Department, Job Role, Remote Work Status, Work Experience, Work Hours.
- **Lifestyle Factors:** Sleep Duration, Physical Activity, Caffeine Intake.
- **Evaluated Metrics:** Workload Score, Job Satisfaction, Stress Level, Mental Health Score.

## Model Performance
| Model | MAE | RMSE | R² Score |
| :--- | :--- | :--- | :--- |
| **Linear Regression** | 2.531 | 3.343 | 0.914 |
| **Random Forest Regressor** | 2.086 | 2.710 | 0.944 |

## Getting Started
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/Mental-Health-Prediction-ML.git](https://github.com/your-username/Mental-Health-Prediction-ML.git)
   cd Mental-Health-Prediction-ML
