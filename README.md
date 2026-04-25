# 🛠️ Feature Engineering Pipeline System

## 🚀 Overview

This project implements a **production-style Feature Engineering Pipeline System** designed to preprocess raw data consistently and prepare it for machine learning models.

Instead of applying manual transformations, this system uses structured pipelines to ensure **reproducibility, scalability, and data leakage prevention**.

---

## 🧠 Key Features

* 🔄 **Automated Preprocessing Pipeline**

  * Handles missing values
  * Encodes categorical variables
  * Scales numerical features

* 🧩 **Column-wise Transformations**

  * Separate pipelines for numerical and categorical features
  * Built using `ColumnTransformer`

* 🚫 **Data Leakage Prevention**

  * Pipeline is fitted only on training data
  * Same transformations applied to test/inference data

* 💾 **Pipeline Persistence**

  * Saves preprocessing pipeline for reuse
  * Ensures consistent transformations in production

* 🤖 **Model Training Integration**

  * Pipeline integrated with model training workflow

---

## 🏗️ Project Structure

```id="c6g7d5"
feature-pipeline-system/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── model.pkl
│
├── pipelines/
│   └── preprocess_pipeline.pkl
│
├── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── pipeline_builder.py
│   └── train.py
│
├── config/
│   └── config.yaml
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

```id="p1q3r9"
Raw Data → Preprocessing Pipeline → Clean Features → Model → Saved Pipeline + Model
```

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Pandas
* Pickle

---

## ▶️ How to Run

### 1. Clone Repository

```id="zzr9w2"
git clone <your-repo-link>
cd feature-pipeline-system
```

### 2. Install Dependencies

```id="l6k2y1"
pip install -r requirements.txt
```

### 3. Run Training Pipeline

```id="x0b8m4"
python main.py
```

---

## 📦 Output

After running:

* 📁 `models/model.pkl` → trained model
* 📁 `pipelines/preprocess_pipeline.pkl` → preprocessing pipeline

---

## 💡 Why This Project?

In real-world machine learning systems:

* Data preprocessing must be **consistent**
* Manual transformations lead to **errors and data leakage**
* Pipelines ensure **reusability and reliability**

This project demonstrates how to build:

* Scalable preprocessing systems
* Reproducible ML workflows
* Production-ready pipelines

---

## 🔮 Future Improvements

* Add multiple model training
* Integrate experiment tracking
* Use database instead of file storage
* Build API using FastAPI
* Deploy on cloud

---

## 👩‍💻 Author

Built as part of an advanced ML systems learning journey.
