# British Airways Customer Booking Prediction

## Project Overview

This project was developed as part of the **British Airways Data Science Virtual Experience Program**.

The objective was to build a machine learning model capable of predicting whether a customer will complete a flight booking based on behavioural data.

By identifying patterns in customer behaviour, airlines can proactively target high-intent customers before travel.

---

## Dataset

The dataset contains **50,000 customer booking records** with **13 behavioural features**.

Examples of features include:

* purchase lead time
* number of passengers
* flight hour
* length of stay
* route
* booking origin
* ancillary services (meals, baggage, seat preference)

Target variable:

```
booking_complete
```

Class distribution:

* 15% completed bookings
* 85% non-bookings

---

## Project Workflow

### 1. Exploratory Data Analysis

Initial exploration included:

* dataset structure inspection
* distribution analysis
* feature relationships

### 2. Data Preparation

* feature/target separation
* categorical encoding using OneHotEncoder
* train/test split (80/20)

### 3. Machine Learning Model

A **Random Forest Classifier** was trained using a Scikit-Learn pipeline.

Reasons for choosing Random Forest:

* handles mixed feature types well
* robust to feature interactions
* provides interpretable feature importance

---

## Model Performance

Accuracy: **85%**

Because the dataset is highly imbalanced:

* Precision (booking class): **0.49**
* Recall (booking class): **0.11**

The model predicts non-bookers well but struggles to detect booking customers.

Future improvements could include:

* class balancing techniques
* additional behavioural features
* hyperparameter tuning

---

## Key Insights

The most influential variables were:

1. purchase lead time
2. flight hour
3. length of stay
4. flight duration
5. number of passengers

Customers planning trips earlier, travelling longer, and selecting additional services show stronger booking intent.

---

## Technologies UseMustapha Adeyemo Python
* Pandas
* Scikit-Learn
* Matplotlib
* Jupyter Notebook
* Git & GitHub

---

## Author

Taofiq
