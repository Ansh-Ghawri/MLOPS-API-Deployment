from flask import Flask, request, jsonify
import joblib
import pandas as pd # We need pandas briefly just to wrap the input text

print("Loading model...")
# Load the trained model pipeline ONCE when the app starts
model = joblib.load('sentiment_model.joblib')
print("Model loaded.")

# Create the Flask app object
app = Flask(__name__)

# Define the prediction endpoint
# It will accept POST requests at the URL /predict
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data sent to the endpoint
        data = request.get_json()
        print(f"Received data: {data}")

        # Extract the text field - IMPORTANT: wrap it in a list or Series
        input_text = pd.Series([data['text']]) # Model expects iterable input

        # Make prediction
        prediction = model.predict(input_text)
        prediction_proba = model.predict_proba(input_text) # Get probabilities

        # Prepare the response
        result = {
            'input_text': data['text'],
            'prediction': prediction[0], # Get the first (and only) prediction
            'probability_positive': prediction_proba[0][1], # Probability of 'positive' class
            'probability_negative': prediction_proba[0][0] # Probability of 'negative' class
        }
        print(f"Prediction result: {result}")
        return jsonify(result)

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': str(e)}), 400 # Bad request

# Run the Flask app
if __name__ == '__main__':
    # Host='0.0.0.0' makes it accessible from outside the container later
    # Debug=True is helpful for development, shows errors in browser
    app.run(host='0.0.0.0', port=5000, debug=True)