from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the trained pipeline
pipe = pickle.load(open('../data/pipe.pkl', 'rb'))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Extract input data from JSON
    batting_team = data['batting_team']
    bowling_team = data['bowling_team']
    city = data['city']
    current_score = data['current_score']
    overs_done = data['overs_done']
    wickets_down = data['wickets_down']
    last_five = data['last_five']

    # Derived features
    balls_left = 120 - (overs_done * 6)
    wickets_left = 10 - wickets_down
    crr = current_score / overs_done

    # Create DataFrame for model
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'current_score': [current_score],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'crr': [crr],
        'last_five': [last_five]
    })

    prediction = pipe.predict(input_df)
    return jsonify({'predicted_score': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
