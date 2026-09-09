# Student Placement Prediction using Machine Learning
A simple machine learning web application that predicts whether a student is likely to be placed based on academic performance, internships, projects, aptitude, and communication skills.

#📌 Project Overview

The Student Placement Prediction System uses a machine learning classification model to estimate a student's placement outcome.

The user enters student details through a web interface, and the trained ML model predicts:

PLACED
NOT PLACED

The application also displays the estimated placement probability.

#🚀 Features

Student placement prediction
Simple web-based interface
Machine learning classification
Placement probability calculation
User-friendly input form
Python Flask backend
Easy to run locally
#🛠️ Technologies Used

Python
Pandas
Scikit-learn
Flask
HTML
CSS
Logistic Regression
📊 Input Features

#The model currently uses:

Feature	Description
CGPA	Student's CGPA
Internships	Number of internships completed
Projects	Number of projects completed
Aptitude Score	Aptitude test score
Communication Score	Communication skills score
🧠 Machine Learning Model

The project uses Logistic Regression, a supervised machine learning classification algorithm.

#Workflow 

Student Data
     ↓
Data Preparation
     ↓
Feature Selection
     ↓
Logistic Regression
     ↓
Prediction
     ↓
Placed / Not Placed
     ↓
Placement Probability

#📁 Project Structure

student-placement-prediction/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── README.md
│
└── requirements.txt
