# Fraud Detection Using Machine Learning

## 📌 Project Overview

This project is a **Fraud Detection Machine Learning application** that predicts whether a financial transaction is **fraudulent or legitimate**.

The machine learning model is trained using transaction-related features and deployed as an interactive **Streamlit web application**.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## 📊 Features

The application takes the following transaction details as input:

* Transaction Type
* Transaction Amount
* Old Balance of Sender
* New Balance of Sender
* Old Balance of Receiver
* New Balance of Receiver

It also calculates additional balance-difference features used by the trained model.

## 🤖 Machine Learning

The trained machine learning pipeline is saved as:

```text
fraud_detection_model.pkl
```

The saved model is loaded into the Streamlit application using Joblib.

The model produces:

* `0` → Legitimate Transaction
* `1` → Fraudulent Transaction

## 🌐 Streamlit Application

The project includes an interactive Streamlit interface where users can enter transaction details and click the **Predict** button.

The application displays the prediction as either:

**Fraudulent**

or

**Legitimate**

## 📁 Project Structure

```text
Fraud_Dectection/
│
├── fraud_detection.py
├── fraud_detection_model.pkl
├── analysis_model.ipynb
├── README.md
├── LICENSE
└── .gitignore
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/d6752668-web/fraud_detection.git
```

### 2. Open the project folder

```bash
cd fraud_detection
```

### 3. Install required libraries

```bash
pip install pandas scikit-learn joblib streamlit
```

### 4. Run the Streamlit application

```bash
python -m streamlit run fraud_detection.py
```

### 5. Open the application

Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open it in your web browser.

## 📌 Dataset

The project uses a financial transaction dataset for fraud detection.

The original dataset is not included in the GitHub repository because of its large file size.

## 🎯 Project Objective

The main objective of this project is to demonstrate how **Machine Learning can be used to identify potentially fraudulent financial transactions** and how a trained model can be deployed as an interactive web application using Streamlit.

## 👨‍💻 Author

**Dinesh**
