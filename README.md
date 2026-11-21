# 🧠 Mental Health & Stress Level Prediction Platform

An end-to-end Machine Learning model and interactive **Streamlit** web application designed to predict employee mental health scores and provide actionable burnout risk assessments.

## 🎯 Project Overview
Workplace stress and burnout significantly impact employee well-being and productivity. This platform analyzes lifestyle and workplace factors to deliver real-time mental health score predictions along with tailored wellness recommendations.

## 🚀 Key Deliverables & Features
- **Preprocessing & Pipeline:** Constructed robust Scikit-learn pipelines utilizing `StandardScaler` for numerical features and `OneHotEncoder` for categorical variables.
- **High-Accuracy Model:** Trained and evaluated a **Random Forest Regression** model on 2,000 records, achieving strong predictive performance:
  - **$R^2$ Score:** `0.944`
  - **MAE:** `2.086`
  - **RMSE:** `2.710`
- **Interactive Web Dashboard:** Built with Streamlit and Plotly, featuring real-time prediction updates, interactive parameter sliders, visual gauge charts, and personalized risk assessments.

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Machine Learning & Data Processing:** Scikit-learn, Pandas, NumPy, Joblib
- **Frontend & Data Visualization:** Streamlit, Plotly

## 💻 How to Run Locally
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/shehancharith26/mental-health-dashboard.git](https://github.com/shehancharith26/mental-health-dashboard.git)
   cd mental-health-dashboard
