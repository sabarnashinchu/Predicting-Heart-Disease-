from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

# If model doesn't exist, train a simple one
model_path = 'heart_disease_model.pkl'
scaler_path = 'scaler.pkl'

def train_model():
    # Sample data (in a real app, you'd use a proper dataset)
    # Features: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
    X = np.array([
        [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1],
        [37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2],
        [41, 0, 1, 130, 204, 0, 0, 172, 0, 1.4, 2, 0, 2],
        [56, 1, 1, 120, 236, 0, 1, 178, 0, 0.8, 2, 0, 2],
        [57, 0, 0, 120, 354, 0, 1, 163, 1, 0.6, 2, 0, 2],
        [57, 1, 0, 140, 192, 0, 1, 148, 0, 0.4, 1, 0, 1],
        [56, 0, 1, 140, 294, 0, 0, 153, 0, 1.3, 1, 0, 2],
        [44, 1, 1, 120, 263, 0, 1, 173, 0, 0, 2, 0, 3],
        [52, 1, 2, 172, 199, 1, 1, 162, 0, 0.5, 2, 0, 3],
        [57, 1, 2, 150, 168, 0, 1, 174, 0, 1.6, 2, 0, 2],
        [54, 1, 0, 140, 239, 0, 1, 160, 0, 1.2, 2, 0, 2],
        [48, 0, 2, 130, 275, 0, 1, 139, 0, 0.2, 2, 0, 2],
        [49, 1, 1, 130, 266, 0, 1, 171, 0, 0.6, 2, 0, 2],
        [64, 1, 3, 110, 211, 0, 0, 144, 1, 1.8, 1, 0, 2],
        [58, 0, 3, 150, 283, 1, 0, 162, 0, 1, 2, 0, 2]
    ])
    
    # Labels: 0 = no heart disease, 1 = heart disease
    y = np.array([1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0])
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_scaled, y)
    
    # Save model and scaler
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    with open(scaler_path, 'wb') as f:
        pickle.dump(scaler, f)
    
    return model, scaler

# Load or train model
if os.path.exists(model_path) and os.path.exists(scaler_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
else:
    model, scaler = train_model()

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'status': 'running',
        'message': 'Heart Disease Prediction API is up and running',
        'endpoints': {
            '/predict': 'POST - Make heart disease predictions',
            '/health': 'GET - Check API health status'
        },
        'usage': 'Access the frontend application at http://localhost:8000'
    })

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Extract features from request
    features = [
        float(data['age']),
        1 if data['sex'] == 'male' else 0,
        float(data['cp']),
        float(data['trestbps']),
        float(data['chol']),
        1 if float(data['fbs']) > 120 else 0,
        float(data['restecg']),
        float(data['thalach']),
        1 if data['exang'] == 'yes' else 0,
        float(data['oldpeak']),
        float(data['slope']),
        float(data['ca']),
        float(data['thal'])
    ]
    
    # Scale features
    features_scaled = scaler.transform(np.array(features).reshape(1, -1))
    
    # Make prediction
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]
    
    return jsonify({
        'prediction': int(prediction),
        'probability': float(probability),
        'message': 'High risk of heart disease' if prediction == 1 else 'Low risk of heart disease'
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 