# British Airways Customer Booking Prediction

## Project Overview

This project builds a **machine learning model to predict whether a customer will complete a flight booking** based on their booking behaviour.

Airlines must increasingly **predict customer intent before the travel date** so they can target marketing and optimise revenue strategies.

Using customer booking data, we trained a **Random Forest classification model** to predict booking completion.

---

# Objective

Predict whether a customer will complete a booking using behavioural and booking features.

Target variable:

`booking_complete`

* 0 → customer did not complete booking
* 1 → customer completed booking

---

# Dataset

The dataset contains customer booking behaviour including:

* number of passengers
* purchase lead time
* length of stay
* flight hour
* route
* booking origin
* additional services requested
* flight duration

These features help identify patterns that influence booking completion.

---

# Project Structure

```
ba-customer-booking-prediction
│
├── data/
│   └── raw/
│       └── customer_booking.csv
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── src/
│   └── train_model.py
│
├── outputs/
│   └── booking_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Exploratory Data Analysis

The exploratory analysis is located in:

```
notebooks/01_eda.ipynb
```

This notebook includes:

* dataset exploration
* feature inspection
* preprocessing
* model training
* evaluation metrics

---

# Model

Algorithm used:

**Random Forest Classifier**

Reasons for choosing Random Forest:

* handles mixed data types well
* robust to overfitting
* provides feature importance
* strong performance on tabular datasets

---

# Model Performance

Evaluation metrics:

Accuracy:

```
0.85
```

Classification Report:

```
precision    recall  f1-score   support

0       0.86      0.98      0.92      8504
1       0.49      0.11      0.18      1496
```

The model predicts non-bookings well but has difficulty detecting completed bookings due to **class imbalance**.

---

# Feature Importance

Key factors influencing booking completion include:

* purchase lead
* flight hour
* length of stay
* flight duration
* number of passengers

---

# How to Run the Project

Clone the repository:

```
git clone https://github.com/Godblessme99/ba-customer-booking-prediction.git
```

Navigate to the project:

```
cd ba-customer-booking-prediction
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Train the Model

Run the training script:

```
python src/train_model.py
```

The trained model will be saved to:

```
outputs/booking_model.pkl
```

---

# Model Output

The trained model is exported using **joblib**.

```
joblib.dump(model, "../outputs/booking_model.pkl")
```

The outputs folder is excluded from version control due to file size limitations.

---

# Business Insight

Key findings:

* Customers booking further in advance are more likely to complete bookings
* Flight time and duration influence purchase behaviour
* Ancillary services (meals, baggage) correlate with booking completion

These insights help airlines improve **marketing targeting and demand forecasting**.

---

# Future Improvements

PMustapha Adeyemoossible improvements:

* address class imbalance using SMOTE or class weighting
* hyperparameter tuning
* deploy the model as a prediction API
* build a dashboard for airline analysts

---

# Author

Machine Learning Project
British Airways Data Science Simulation
`

This will recreate the trained model locally.
