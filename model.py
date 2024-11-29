

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Read the dataset and clean
data = pd.read_csv("Training.csv").dropna(axis=1)
Sym_desc = pd.read_csv("symptom_Description.csv")
Sym_pre = pd.read_csv("symptom_precaution.csv")

encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

# Define the features (symptoms) and target (disease labels)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models with class balancing
final_svm_model = SVC(class_weight='balanced')  # Adding class_weight to handle imbalance
final_svm_model.fit(X_train, y_train)

final_nb_model = GaussianNB()
final_nb_model.fit(X_train, y_train)

final_rf_model = RandomForestClassifier(random_state=42, class_weight='balanced')  # Adding class_weight
final_rf_model.fit(X_train, y_train)

# Check model performance on the test set
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(f"Confusion Matrix for {model}:")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

# Evaluate models to ensure they perform well and are not biased towards one class
evaluate_model(final_rf_model, X_test, y_test)
evaluate_model(final_nb_model, X_test, y_test)
evaluate_model(final_svm_model, X_test, y_test)

# Mapping symptoms to their indices
symptoms = X.columns.values
symptom_index = {symptom: index for index, symptom in enumerate(symptoms)}

def predictDisease(symptoms_input):
    # Initialize input vector with zeros (no symptoms present)
    input_data = [0] * len(symptom_index)

    # Process the input symptoms and map them to the input vector
    for symptom in symptoms_input.split(","):
        symptom = symptom.strip().lower()  # Normalize to lowercase to avoid case sensitivity issues
        if symptom in symptom_index:
            input_data[symptom_index[symptom]] = 1

    input_data = np.array(input_data).reshape(1, -1)

    # Make predictions with all models
    rf_prediction = encoder.classes_[final_rf_model.predict(input_data)[0]]
    nb_prediction = encoder.classes_[final_nb_model.predict(input_data)[0]]
    svm_prediction = encoder.classes_[final_svm_model.predict(input_data)[0]]

    # Log individual model predictions
    print(f"Individual Predictions: RF - {rf_prediction}, NB - {nb_prediction}, SVM - {svm_prediction}")

    # Combine the predictions using majority vote (most frequent prediction)
    final_prediction = [rf_prediction, nb_prediction, svm_prediction]
    final_prediction = max(set(final_prediction), key=final_prediction.count)

    # Retrieve disease description and precautions from the corresponding CSV files
    description = Sym_desc[Sym_desc['Disease'] == final_prediction]['description'].values[0]
    precautions = Sym_pre[Sym_pre['Disease'] == final_prediction].iloc[0, 1:]

    return {
        "Disease": final_prediction,
        "Description": description,
        "Precaution": precautions.to_string()
    }

# Debugging: test the model with a sample input
# result = predictDisease("fatigue,cough,headache,shivering")
# print(result)
