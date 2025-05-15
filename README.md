# Heart Disease Prediction Application

A simple web application that predicts the risk of heart disease based on medical attributes.

## Project Structure

```
├── backend/
│   ├── app.py              # Flask API
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Backend documentation
└── frontend/
    ├── index.html          # HTML structure
    ├── styles.css          # CSS styling
    └── script.js           # JavaScript functionality
```

## Features

- User-friendly form for entering medical information
- Machine learning model (RandomForest) for heart disease prediction
- Real-time prediction with probability score
- Responsive design that works on mobile and desktop

## Setup and Installation

### Backend

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the server:
   ```
   python app.py
   ```

The API server will start on http://localhost:5000

### Frontend

1. Simply open the `frontend/index.html` file in a web browser, or serve it using a simple HTTP server:
   ```
   cd frontend
   python -m http.server 8000
   ```

Then navigate to http://localhost:8000 in your browser.

## How to Use

1. Fill in the form with patient medical data
2. Click "Predict" button
3. View prediction result showing risk level and probability
4. Click "Make Another Prediction" to start over

## Medical Features Explanation

- **Age**: Age in years
- **Sex**: Gender (male/female)
- **CP**: Chest pain type (0-3)
- **Trestbps**: Resting blood pressure (mm Hg)
- **Chol**: Serum cholesterol (mg/dl)
- **FBS**: Fasting blood sugar > 120 mg/dl
- **Restecg**: Resting electrocardiographic results (0-2)
- **Thalach**: Maximum heart rate achieved
- **Exang**: Exercise-induced angina (yes/no)
- **Oldpeak**: ST depression induced by exercise
- **Slope**: Slope of the peak exercise ST segment (0-2)
- **CA**: Number of major vessels colored by fluoroscopy (0-3)
- **Thal**: Thalassemia (1-3)

## Technical Details

- Backend: Python Flask with scikit-learn
- Frontend: HTML, CSS, JavaScript (vanilla)
- Model: RandomForest classifier trained on sample heart disease data
- Communication: RESTful API with JSON

## Disclaimer

This application is for educational purposes only and should not be used for actual medical diagnosis. Always consult with a qualified healthcare professional for medical advice. 