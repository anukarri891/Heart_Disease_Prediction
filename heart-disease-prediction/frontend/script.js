document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Collect all inputs
    const inputs = [...document.querySelectorAll('#predictionForm input')];
    const features = {};
    inputs.forEach(input => features[input.name] = parseFloat(input.value));

    // Send the data to the backend
    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(features)
    });

    // Display the result
    const data = await response.json();
    document.getElementById('result').textContent = `Prediction: ${data.prediction}`;
});
