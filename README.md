# 🧠 Machine Learning Projects

Welcome to the **Machine Learning Projects Repository**!  
This repo showcases a collection of end-to-end ML projects using Python, covering real-world problems like classification, regression, fault detection, anomaly scoring, and deployment using Flask.

## 📁 Project List

Each project folder contains everything from data ingestion to model deployment:

- **IoT Equipment Fault Prediction**
  - Predict machine failures based on sensor data.
  - SMOTE for imbalance, Logistic Regression, Random Forest, and XGBoost.
  - Deployed via Flask with an interactive UI.
  <h3>📸 Project Screenshots</h3>
<p align="center"> <img src="assets/iot_demo1.png" alt="Model Training" width="250"/> <img src="assets/iot_demo2.png" alt="Prediction Page" width="250"/> <img src="assets/iot_demo3.png" alt="Jupyter Notebook Output" width="250"/><img src="assets/iot_demo4.png" alt="Jupyter Notebook Output" width="250"/> </p> <p align="center"> <em>Left: Model Training Logs &nbsp; | &nbsp; Center: Web UI Prediction Form &nbsp; | &nbsp; Right: Notebook Metrics & Plots</em> </p>

(More projects being added continuously...)

---

## 🧰 Tech Stack

- **Python 3.8+**
- **Scikit-learn, XGBoost, Imbalanced-learn**
- **Flask** for deployment
- **Pandas, NumPy, Matplotlib, Seaborn** for EDA
- **Git & GitHub** for version control

---

## 🚀 Running the Project Locally

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/ML_Projects.git
cd ML_Projects
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run a specific project (e.g., Flask app):

bash
Copy
Edit
python app.py
Then visit http://localhost:5000 in your browser.

📦 Folder Structure (Typical)
cpp
Copy
Edit
ML_projects/
│
├── project_name/
│   ├── src/
│   ├── templates/
│   ├── static/
│   ├── app.py
│   └── requirements.txt
├── artifacts/
├── logs/
├── .gitignore
├── README.md
└── requirements.txt
📌 Notes
Large model files (e.g., .pkl) are not tracked by Git due to the 100MB limit.
⚠️ Note:
This project does not include the trained `model.pkl` file due to GitHub's 100MB size limit.

If you wish to run predictions:
- Either train your own model using the provided pipeline, OR
- Contact me for the model file.

All core functionalities (data ingestion, transformation, model training) are available and runnable.

Each project is modular, with data_ingestion, data_transformation, model_trainer, and predict_pipeline components.

📫 Contact
For queries or suggestions, feel free to reach out via GitHub Issues.

