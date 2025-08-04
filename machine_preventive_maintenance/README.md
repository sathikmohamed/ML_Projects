# 🔧 IoT Equipment Fault Prediction

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Last Commit](https://img.shields.io/github/last-commit/sathikmohamed/ML_projects)
![Issues](https://img.shields.io/github/issues/sathikmohamed/ML_projects)
![Stars](https://img.shields.io/github/stars/sathikmohamed/ML_projects?style=social)

---

## 📌 Project Overview

**IoT Equipment Fault Prediction** is a machine learning-based solution to detect potential failures in industrial equipment using real-time sensor data. The project demonstrates how predictive maintenance can reduce downtime and increase operational efficiency by identifying anomalies in sensor readings.

This showcase includes a complete end-to-end ML pipeline with data preprocessing, model training, evaluation, and deployment using a Flask web application.

---

## 🚀 Features

- Ingests and processes IoT sensor data from equipment
- Applies preprocessing with scaling and transformations
- Trains a Logistic Regression model using oversampling (SMOTE)
- Evaluates model using F1, Accuracy, ROC-AUC, and more
- Deploys a web interface to accept real-time input and return predictions
- Uses modular design with custom exception handling and logging

---

## 🧠 Tech Stack

- Python 3.80
- Pandas, NumPy, Scikit-learn
- SMOTE (imbalanced-learn)
- Flask (for model deployment)
- Git & GitHub for version control

---

## 📁 Directory Structure

ML_projects/
│
├── artifacts/ # Stores trained model, preprocessor
├── notebook/ # Data exploration and analysis
├── src/ # Core source code
│ ├── components/ # Data transformation and model training modules
│ ├── pipeline/ # Prediction pipeline
│ ├── exception.py # Custom exception class
│ ├── logger.py # Logging setup
│ └── utils.py # Utility functions
├── templates/ # HTML files for Flask app
├── app.py # Main Flask app
├── requirements.txt
├── README.md
└── .gitignore



## ⚙️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/sathikmohamed/ML_projects.git
   cd ML_projects
Create virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the application

bash
Copy
Edit
python app.py
📌 Note
Model files (model.pkl) over 100MB are not pushed to GitHub due to size limits. If you're trying to run the project locally, you will need to retrain the model or download the model.pkl and preprocessor.pkl files separately.

📜 License
This project is licensed under the MIT License.

🙋‍♂️ Contact
For feedback or suggestions, please open an issue or reach out via the GitHub repository.