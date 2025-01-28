from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    model = pickle.load(open('backend/model.pkl', 'rb'))
except FileNotFoundError:
    print("Error: model.pkl not found.")
    exit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get features from the form (assuming form input names are 'feature1', 'feature2', ..., 'feature13')
        features = [float(request.form[f'feature{i}']) for i in range(1, 14)]
        
        # Convert features into numpy array for prediction
        features = np.array(features).reshape(1, -1)
        
        # Make the prediction
        prediction = model.predict(features)
        
        # Interpret the prediction
        result = "The person has heart disease" if prediction[0] == 1 else "The person does not have heart disease"
        
        return render_template('index.html', prediction=result)
    
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
