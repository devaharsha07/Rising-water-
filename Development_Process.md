# Project Development Process

## Project Overview

Rising Waters is an AI-powered Flood Prediction System developed using Machine Learning and Flask. The system predicts flood probability using environmental parameters and provides AI-based safety recommendations.

---

# Development Steps

## Step 1: Dataset Collection

- Collected historical flood-related environmental data.
- Verified dataset quality.
- Checked for missing values.

---

## Step 2: Data Preprocessing

- Imported dataset using Pandas.
- Selected input features.
- Prepared target variable.
- Split dataset into training and testing data.

---

## Step 3: Machine Learning Model Development

The following models were trained:

- Decision Tree
- Random Forest
- K-Nearest Neighbours (KNN)
- XGBoost

The models were compared, and XGBoost was selected as the final model because it produced the best performance.

---

## Step 4: Model Saving

The trained model was saved using Joblib as:

floods.save

---

## Step 5: Flask Application Development

The web application was developed using Flask.

Main components:

- app.py
- HTML Templates
- CSS Styling
- Prediction Engine

---

## Step 6: Frontend Development

Developed responsive pages using:

- HTML
- CSS

Pages:

- Home Page
- Prediction Result Page

---

## Step 7: Version Control

Git and GitHub were used to maintain project versions and collaboration.

Repository:

https://github.com/mohanias1/Rising-Waters-AI

---

## Step 8: Deployment

The application was deployed on Render.

Live Website:

https://rising-waters-ai.onrender.com/