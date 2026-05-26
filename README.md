# 📡 Telecom Customer Churn Predictor

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit)
![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-orange?logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

A machine learning web application that predicts whether a telecom customer will churn (leave) or stay, based on their usage patterns and history.

🔗 **Live App:** https://churn-prediction-ipwth9dtpfwmu5byjdpyyr.streamlit.app  
📂 **GitHub:** https://github.com/pawan0221/churn-prediction

---

## 🎯 Problem Statement

Telecom companies lose millions every year due to customer churn. This app uses Machine Learning to identify at-risk customers early, so the business can take action before they leave.

---

## 🚀 Features

- 🔍 Predicts churn in real time based on customer inputs
- 📊 Shows confidence score with every prediction
- 🌲 Powered by Random Forest (100 decision trees)
- 🌐 Fully deployed — no installation needed

---

## 🧠 Model Details

| Detail | Info |
|--------|------|
| Algorithm | Random Forest Classifier |
| Library | scikit-learn |
| Training Data | 300 synthetic telecom customer records |
| Features Used | Age, Data Usage, Complaints, Tenure, Plan Type |
| Target | Churn (1 = Yes, 0 = No) |

---

## 📥 Input Features

| Feature | Description |
|---------|-------------|
| Age | Customer age (18–70) |
| Data Usage (GB) | Monthly data consumption |
| Number of Complaints | Complaints filed in last 6 months |
| Tenure (months) | How long they've been a customer |
| Plan Type | Prepaid or Postpaid |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| pandas & numpy | Data processing |
| scikit-learn | ML model training |
| joblib | Model saving/loading |
| Streamlit | Web app & deployment |
| Git & GitHub | Version control |

churn-prediction/
├── app.py                      # Streamlit web application
├── churn_decision_tree.joblib  # Trained Random Forest model
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

---

## ⚙️ Run Locally

```bash
# Clone the repo
git clone https://github.com/pawan0221/churn-prediction.git
cd churn-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 👨‍💻 Author

**Pawan Soni**  
GitHub: [@pawan0221](https://github.com/pawan0221)

---

## 📄 License

This project is open source and available under the MIT License.
