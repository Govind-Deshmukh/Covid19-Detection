# COVID-19 Death Outcome Risk Estimation

This repository contains code and data for estimating the risk of death due to COVID-19 based on medical data. The dataset used in this analysis was provided by the Mexican government and can be found on Kaggle under the title "COVID-19 Dataset".

## Dataset

The dataset consists of the following columns:

- USMER: USMER medical unit identifier
- MEDICAL_UNIT: Type of institution of the National Health System that provided the care
- SEX: Gender of the patient (1 for female, 2 for male)
- PATIENT_TYPE: Type of patient (1 for hospitalized, 2 for not hospitalized)
- DATE_DIED: Date of death of the patient (9999-99-99 if the patient did not die due to COVID-19)
- INTUBED: Whether the patient was connected to a ventilator (1 for yes, 2 for no)
- PNEUMONIA: Whether the patient had pneumonia (1 for yes, 2 for no)
- AGE: Age of the patient
- PREGNANT: Whether the patient is pregnant (1 for yes, 2 for no)
- DIABETES: Whether the patient has diabetes (1 for yes, 2 for no)
- COPD: Whether the patient has Chronic obstructive pulmonary disease (1 for yes, 2 for no)
- ASTHMA: Whether the patient has asthma (1 for yes, 2 for no)
- INMSUPR: Whether the patient is immunosuppressed (1 for yes, 2 for no)
- HIPERTENSION: Whether the patient has hypertension (1 for yes, 2 for no)
- OTHER_DISEASE: Whether the patient has other diseases (1 for yes, 2 for no)
- CARDIOVASCULAR: Whether the patient has heart or blood vessel-related diseases (1 for yes, 2 for no)
- OBESITY: Whether the patient is obese (1 for yes, 2 for no)
- RENAL_CHRONIC: Whether the patient has chronic renal disease (1 for yes, 2 for no)
- TOBACCO: Whether the patient is a tobacco user (1 for yes, 2 for no)
- CLASIFFICATION_FINAL: COVID-19 test findings (1-3 for positive test results, 4 or higher for negative or inconclusive results)
- ICU: Whether the patient was admitted to an Intensive Care Unit (1 for yes, 2 for no)
- DEATH: Whether the patient died or recovered (1 for death, 0 for recovery)

## Data Cleaning and Preprocessing

The provided dataset was cleaned and preprocessed before training the model. Missing values were handled, boolean features were converted to 0 and 1, and feature engineering was performed. Age was divided into age groups and one-hot encoded. The dataset was then split into training and testing sets.

## Model Building

A logistic regression model was trained using the undersampled training dataset. Grid search was performed to find the best hyperparameters for the model. The model was evaluated using various metrics such as accuracy, precision, recall, f1-score, and ROC-AUC score. The results showed a high recall for the "1" class, indicating good performance in identifying patients at risk of death due to COVID-19.

A logistic regression model was trained using the undersampled training dataset. Grid search was performed to find the best hyperparameters for the model. The model was evaluated using various metrics such as accuracy, precision, recall, f1-score, and ROC-AUC score. The results showed a high recall for the "1" class, indicating good performance in identifying patients at risk of death due to COVID-19.

## Model Interpretation

The coefficients of the logistic regression model were interpreted to understand the impact of different features on the risk of death. The coefficients were visualized using bar plots, indicating the direction and magnitude of the effect.

## Dependencies

The following dependencies are required to run the code:

- Python 3
- Flask
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn

Please make sure to install the necessary packages before running the code.

## Usage

To use the trained model for prediction, run the Flask application included in the code. The application provides a simple web interface where you can enter the patient's information and get the prediction of whether the patient is likely to have COVID-19. The `model.pkl` file contains the trained logistic regression model.

To start the Flask application, run the following command:

```
python app.py
```

then the application will be accessible at

The application will be accessible at http://localhost:5000.
