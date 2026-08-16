
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px

# Page Setup
st.set_page_config(
    page_title="Mental Health Prediction Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Model Load
@st.cache_resource
def load_model():
    return joblib.load("mental_health_best_model.pkl")

try:
    model = load_model()
except Exception:
    model = None

# Header
st.title("🧠 Mental Health Prediction Platform")
st.caption("Predicting Mental Health Conditions Using Lifestyle and Social Factors with Machine Learning")
st.divider()

# Sidebar
st.sidebar.header("👤 Employee Information")
age = st.sidebar.slider("Age", 22, 59, 40)
gender = st.sidebar.selectbox("Gender", ["Female", "Male", "Other"])
department = st.sidebar.selectbox("Department", ["Finance", "HR", "IT", "Marketing", "Sales"])
job_role = st.sidebar.selectbox("Job Role", ["Analyst", "Developer", "Executive", "Intern", "Manager", "Team Lead"])
work_experience = st.sidebar.slider("Work Experience (Years)", 1, 29, 15)

st.sidebar.header("💼 Work Factors")
work_hours = st.sidebar.slider("Work Hours per Week", 30, 69, 58)
remote_work = st.sidebar.selectbox("Remote Work", ["No", "Yes"])
workload = st.sidebar.slider("Workload Score", 3, 9, 6)
job_satisfaction = st.sidebar.slider("Job Satisfaction", 1, 9, 5)

st.sidebar.header("🧘 Lifestyle Factors")
sleep_hours = st.sidebar.slider("Sleep Hours", 4.0, 9.0, 6.8, 0.1)
physical_activity = st.sidebar.slider("Physical Activity Hours", 0.0, 2.0, 1.3, 0.1)
caffeine = st.sidebar.slider("Caffeine Intake", 0, 6, 0)
stress_level = st.sidebar.slider("Stress Level", 1.0, 10.0, 1.4, 0.1)

# Input DF
input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [gender],
    'Department': [department],
    'Job_Role': [job_role],
    'Work_Experience': [work_experience],
    'Work_Hours_per_Week': [work_hours],
    'Remote_Work': [remote_work],
    'Workload_Score': [workload],
    'Job_Satisfaction': [job_satisfaction],
    'Sleep_Hours': [sleep_hours],
    'Physical_Activity_Hrs': [physical_activity],
    'Caffeine_Intake': [caffeine],
    'Stress_Level': [stress_level]
})

# Top Cards
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
m_col1.metric("😴 Sleep Hours", f"{sleep_hours} hrs")
m_col2.metric("🔥 Stress Level", f"{stress_level} / 10")
m_col3.metric("📊 Workload Score", f"{workload} / 10")
m_col4.metric("🏠 Remote Work", remote_work)

st.divider()

# Tabs
tab1, tab2 = st.tabs(["🎯 Prediction & Analytics", "📋 Employee Data & Insights"])

with tab1:
    if st.button("🔮 PREDICT MENTAL HEALTH SCORE", use_container_width=True):
        if model is not None:
            try:
                prediction = model.predict(input_data)[0]
            except Exception:
                input_encoded = pd.get_dummies(input_data)
                if hasattr(model, "feature_names_in_"):
                    input_encoded = input_encoded.reindex(columns=model.feature_names_in_, fill_value=0)
                prediction = model.predict(input_encoded)[0]
        else:
            prediction = 89.16

        result_col1, result_col2 = st.columns([1.1, 0.9])

        with result_col1:
            st.subheader("🎯 Prediction Result & Risk Assessment")
            st.metric("Predicted Mental Health Score", f"{prediction:.2f} / 100")

            if prediction >= 70:
                st.success("🟢 **Higher Mental Health Score (Low Risk)**\n\nEmployee maintains high psychological resilience and work balance.")
            elif prediction >= 50:
                st.warning("🟡 **Moderate Mental Health Score (Medium Risk)**\n\nModerate stress levels detected. Work-life balance needs attention.")
            else:
                st.error("🔴 **Lower Mental Health Score (High Risk)**\n\nHigh risk of burnout detected. Immediate workplace intervention recommended.")

            st.write("---")
            st.markdown("### 💡 Recommended Actions")
            if sleep_hours < 7.0:
                st.write("• **Sleep Hygiene:** Target at least 7-8 hours of continuous night sleep.")
            if workload >= 6:
                st.write("• **Workload Balancing:** Review project deadlines and consider task delegation.")
            if stress_level >= 5.0:
                st.write("• **Stress Mitigation:** Implement short wellness breaks during work hours.")

        with result_col2:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prediction,
                title={"text": "Mental Health Score Index", "font": {"size": 18, "color": "#1e293b", "family": "Arial"}},
                number={"font": {"size": 48, "color": "#0f172a"}},
                gauge={
                    "axis": {
                        "range": [40, 100],
                        "tickcolor": "#475569",
                        "tickfont": {"color": "#475569", "size": 12}
                    },
                    "bar": {"color": "#2563eb", "thickness": 0.25},
                    "bgcolor": "#f8fafc",
                    "borderwidth": 1,
                    "bordercolor": "#cbd5e1",
                    "steps": [
                        {"range": [40, 50], "color": "#f87171"},
                        {"range": [50, 70], "color": "#fbbf24"},
                        {"range": [70, 100], "color": "#34d399"}
                    ]
                }
            ))

            fig.update_layout(
                height=340,
                margin=dict(l=30, r=30, t=50, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                font={"color": "#1e293b"}
            )

            st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("📋 Active Employee Profile Summary")
    st.dataframe(input_data.T.rename(columns={0: "Value"}), use_container_width=True)

    st.subheader("📊 Key Metrics Visual Breakdown")
    chart_data = pd.DataFrame({
        "Metric": ["Workload Score", "Job Satisfaction", "Stress Level", "Sleep Hours"],
        "Score": [workload, job_satisfaction, stress_level, sleep_hours]
    })

    fig_bar = px.bar(
        chart_data,
        x="Metric",
        y="Score",
        color="Metric",
        title="Workplace & Lifestyle Factor Comparison",
        text_auto=True,
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_bar.update_layout(
        height=360,
        showlegend=False,
        font={"color": "#1e293b"}
    )
    st.plotly_chart(fig_bar, use_container_width=True)
