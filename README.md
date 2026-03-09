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

Mustapha Adeyemo




## Model Insight

The most important factors influencing customer booking behaviour were:

* Purchase lead time
* Flight hour
* Length of stay
* Flight duration
* Number of passengers

These features suggest that customers who plan their trips earlier, travel longer distances, or select additional services are more likely to complete bookings.

This insight can help airlines target high-intent customers earlier and personalise marketing strategies.

## Model Output

The trained machine learning model is saved locally using **joblib**.

During training, the model is exported to the `outputs/` directory:

```python
joblib.dump(model, "../outputs/booking_model.pkl")
```

Due to GitHub's file size limitations, the trained model file is **not stored in the repository**.
The `outputs/` directory is excluded from version control using `.gitignore`.

---

## How to Reproduce the Model

To regenerate the trained model:

1. Clone the repository

```
git clone https://github.com/Godblessme99/ba-customer-booking-prediction.git
```

2. Navigate to the project folder

```
cd ba-customer-booking-prediction
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the training notebook

Open the notebook:

```
notebooks/01_eda.ipynb
```

Run all cells to train the model and save it to:

```
outputs/booking_model.pkl
```

This will recreate the trained model locally.
