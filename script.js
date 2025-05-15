document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultContainer = document.getElementById('result');
    const resultContent = document.getElementById('result-content');
    const probabilityBar = document.getElementById('probability-bar');
    const resetButton = document.getElementById('reset-btn');
    const loadingContainer = document.getElementById('loading');
    
    // Set default values for the form
    function setDefaultValues() {
        document.getElementById('age').value = 45;
        document.getElementById('trestbps').value = 120;
        document.getElementById('chol').value = 200;
        document.getElementById('fbs').value = 110;
        document.getElementById('thalach').value = 150;
        document.getElementById('oldpeak').value = 1.0;
    }
    
    // Set default values when page loads
    setDefaultValues();
    
    // Handle form submission
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Show loading screen
        loadingContainer.classList.remove('hidden');
        
        // Collect form data
        const formData = {
            age: document.getElementById('age').value,
            sex: document.querySelector('input[name="sex"]:checked').value,
            cp: document.getElementById('cp').value,
            trestbps: document.getElementById('trestbps').value,
            chol: document.getElementById('chol').value,
            fbs: document.getElementById('fbs').value,
            restecg: document.getElementById('restecg').value,
            thalach: document.getElementById('thalach').value,
            exang: document.querySelector('input[name="exang"]:checked').value,
            oldpeak: document.getElementById('oldpeak').value,
            slope: document.getElementById('slope').value,
            ca: document.getElementById('ca').value,
            thal: document.getElementById('thal').value
        };
        
        // Send data to API
        predictHeartDisease(formData);
    });
    
    // Reset prediction
    resetButton.addEventListener('click', function() {
        form.reset();
        setDefaultValues();
        resultContainer.classList.add('hidden');
        form.classList.remove('hidden');
    });
    
    // Send prediction request to API
    function predictHeartDisease(data) {
        // API endpoint (update with your actual backend URL)
        const apiUrl = 'http://localhost:5000/predict';
        
        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(result => {
            displayResult(result);
        })
        .catch(error => {
            console.error('Error:', error);
            // Hide loading screen
            loadingContainer.classList.add('hidden');
            
            // Show error message
            resultContent.textContent = 'Error connecting to the server. Please try again later.';
            resultContent.className = 'error';
            form.classList.add('hidden');
            resultContainer.classList.remove('hidden');
        });
    }
    
    // Display prediction result
    function displayResult(result) {
        // Hide loading screen
        loadingContainer.classList.add('hidden');
        
        // Format the result message
        const probability = Math.round(result.probability * 100);
        const riskClass = result.prediction === 1 ? 'high-risk' : 'low-risk';
        
        // Update the UI
        resultContent.textContent = result.message;
        resultContent.className = riskClass;
        
        // Update probability bar
        probabilityBar.style.width = `${probability}%`;
        probabilityBar.textContent = `${probability}%`;
        
        // If high risk, make the bar red
        if (result.prediction === 1) {
            probabilityBar.style.backgroundColor = '#e53935';
        } else {
            probabilityBar.style.backgroundColor = '#43a047';
        }
        
        // Hide form and show result
        form.classList.add('hidden');
        resultContainer.classList.remove('hidden');
    }
}); 