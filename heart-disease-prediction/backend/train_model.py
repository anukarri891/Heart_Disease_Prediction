import pickle
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('heart_disease_data.csv')

# Split data into features (X) and target (Y)
X = df.drop(columns='target', axis=1)
Y = df['target']

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=23)

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Save the model to a file named 'model.pkl'
with open('backend/model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model has been saved as 'model.pkl'.")
