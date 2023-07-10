from flask import Flask, render_template, request
import pickle 
import numpy as np
import pandas as pd
import json

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = []

    # Get the feature values from the form
    form_values = [
        'RETURNED_HOME', 'INTUBED', 'PNEUMONIA', 'PREGNANT', 'DIABETES', 'COPD', 'ASTHMA', 'INMSUPR', 
        'HIPERTENSION', 'OTHER_DISEASE', 'CARDIOVASCULAR', 'OBESITY', 'RENAL_CHRONIC', 'TOBACCO', 'ICU', 
        'TEST_RESULT', 'AGE_0-9', 'AGE_10-19', 'AGE_20-29', 'AGE_30-39', 'AGE_40-49', 'AGE_50-59', 
        'AGE_60-69', 'AGE_70-79', 'AGE_80-89', 'AGE_OVER_90', 'WOMAN', 'MAN'
    ]
    
    for value in form_values:
        try:
            feature_value = int(request.form[value])
            features.append(feature_value)
        except ValueError:
            # Handle non-integer values here, such as setting a default value or returning an error message
            # For example, setting a default value of 0:
            features.append(0)
    
    # Create a DataFrame from the features
    df = pd.DataFrame([features], columns=form_values)

    # Perform prediction using the loaded model
    prediction = model.predict(df)
    
    if prediction == 1:
        result = "The person is likely to have COVID-19."
    else:
        result = "The person is unlikely to have COVID-19."

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
