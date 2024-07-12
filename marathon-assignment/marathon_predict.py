from flask import Flask, request, jsonify
import joblib
import pandas as pd
import pickle

app = Flask(__name__)

model = joblib.load(r"final_time_model.pkl")
col_names = joblib.load(r"pace_column_names.pkl")

@app.route("/")
def hello() -> str:
    return "Hello World from Flask!"

def pace_to_time(pace):
    hr, min, sec = map(float, pace.split(':'))
    return hr * 3600 + min * 60 + sec

def seconds_to_timestamp(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))


@app.route('/predict', methods = ['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON Request
    user_data = request.json
    
    # Convert JSON request to Pandas DF
    df = pd.DataFrame(user_data)
    
    # Match Column Names
    df = df.reindex(columns=col_names)
    
    df['Pace'] = df['Pace'].apply(pace_to_time)
    
    # Get Prediction
    prediction_seconds = model.predict(df)
    
    # Convert prediction from seconds to timestamp
    timestamp = seconds_to_timestamp(prediction_seconds)
    
    # return JSON version of prediction
    return jsonify({"Official Time": timestamp})


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
