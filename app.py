

# from model import predictDisease
# import re
# import difflib
# from flask import Flask, request, jsonify, render_template
# import webbrowser
# import threading

# # List of symptoms for matching (using exact matches from your data)
# symptoms = [
#     "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering",
#     "chills", "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue", "muscle_wasting",
#     "vomiting", "burning_micturition", "spotting_urination", "fatigue", "weight_gain",
#     "anxiety", "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness",
#     "lethargy", "patches_in_throat", "irregular_sugar_level", "cough", "high_fever",
#     "sunken_eyes", "breathlessness", "sweating", "dehydration", "indigestion", "headache",
#     "yellowish_skin", "dark_urine", "nausea", "loss_of_appetite", "pain_behind_the_eyes",
#     "back_pain", "constipation", "abdominal_pain", "diarrhoea", "mild_fever", "yellow_urine",
#     "yellowing_of_eyes", "acute_liver_failure", "fluid_overload", "swelling_of_stomach",
#     "swelled_lymph_nodes", "malaise", "blurred_and_distorted_vision", "phlegm",
#     "throat_irritation", "redness_of_eyes", "sinus_pressure", "runny_nose", "congestion",
#     "chest_pain", "weakness_in_limbs", "fast_heart_rate", "pain_during_bowel_movements",
#     "pain_in_anal_region", "bloody_stool", "irritation_in_anus", "neck_pain", "dizziness",
#     "cramps", "bruising", "obesity", "swollen_legs", "swollen_blood_vessels", "puffy_face_and_eyes",
#     "enlarged_thyroid", "brittle_nails", "swollen_extremeties", "excessive_hunger",
#     "extra_marital_contacts", "drying_and_tingling_lips", "slurred_speech", "knee_pain",
#     "hip_joint_pain", "muscle_weakness", "stiff_neck", "swelling_joints", "movement_stiffness",
#     "spinning_movements", "loss_of_balance", "unsteadiness", "weakness_of_one_body_side",
#     "loss_of_smell", "bladder_discomfort", "foul_smell_of_urine", "continuous_feel_of_urine",
#     "passage_of_gases", "internal_itching", "toxic_look_(typhos)", "depression", "irritability",
#     "muscle_pain", "altered_sensorium", "red_spots_over_body", "belly_pain", "abnormal_menstruation",
#     "dischromic_patches", "watering_from_eyes", "increased_appetite", "polyuria", "family_history",
#     "mucoid_sputum", "rusty_sputum", "lack_of_concentration", "visual_disturbances",
#     "receiving_blood_transfusion", "receiving_unsterile_injections", "coma", "stomach_bleeding",
#     "distention_of_abdomen", "history_of_alcohol_consumption", "fluid_overload", "blood_in_sputum",
#     "prominent_veins_on_calf", "palpitations", "painful_walking", "pus_filled_pimples",
#     "blackheads", "scurring", "skin_peeling", "silver_like_dusting", "small_dents_in_nails",
#     "inflammatory_nails", "blister", "red_sore_around_nose", "yellow_crust_ooze"
# ]

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')

# @app.route('/chat_response', methods=['POST'])
# def chat_response():
#     if request.method == 'POST':
#         try:
#             sym1 = request.form.get("data")
#             if not sym1:
#                 return jsonify({'response': 'Please enter at least 4 symptoms!'})

#             # Split symptoms by commas
#             sym1 = re.split(r'\s*,\s*', sym1.strip())
#             corrected_symptoms = []
#             wrong_symptoms = []

#             # Match symptoms with the predefined list
#             for symptom in sym1:
#                 corrected_symptom = difflib.get_close_matches(symptom.strip(), symptoms, n=1)
#                 if corrected_symptom:
#                     corrected_symptoms.append(corrected_symptom[0])
#                 else:
#                     wrong_symptoms.append(symptom)

#             # Capitalize the matched symptoms
#             corrected_symptoms = [s.capitalize() for s in corrected_symptoms]

#             if len(corrected_symptoms) < 4:
#                 return jsonify({'response': 'Please enter at least 4 symptoms!'})

#             if wrong_symptoms:
#                 wrong_symptom_str = ' and '.join([f'"{wrong}"' for wrong in wrong_symptoms])
#                 return jsonify({'response': f"The symptoms {wrong_symptom_str} are not in our database. Please try again!"})

#             # Join symptoms into a single string to pass to the model
#             symptoms_input = ",".join(corrected_symptoms)
#             result = predictDisease(symptoms_input)

#             precaution_list = result["Precaution"].split(", ")
#             precaution_string = "<br>".join(precaution_list)

#             doctor_msg = "It is essential to consult healthcare professionals for accurate diagnosis and treatment!"

#             return jsonify({
#                 'disease': result['Disease'],
#                 'description': result['Description'],
#                 'precaution': precaution_string,
#                 'doctor_msg': doctor_msg
#             })

#         except Exception as e:
#             print(f"Error: {e}")
#             return jsonify({'response': 'An error occurred. Please check the symptoms and try again.'})

# def open_browser():
#     webbrowser.open_new('http://127.0.0.1:5000/')

# if __name__ == '__main__':
#     threading.Timer(0.25, open_browser).start()
#     app.run(host='0.0.0.0', port=5000)






from model import predictDisease
import re
import difflib
from flask import Flask, request, jsonify, render_template

# List of symptoms for matching (using exact matches from your data)
symptoms = [
    "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering",
    "chills", "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue", "muscle_wasting",
    "vomiting", "burning_micturition", "spotting_urination", "fatigue", "weight_gain",
    "anxiety", "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness",
    "lethargy", "patches_in_throat", "irregular_sugar_level", "cough", "high_fever",
    "sunken_eyes", "breathlessness", "sweating", "dehydration", "indigestion", "headache",
    "yellowish_skin", "dark_urine", "nausea", "loss_of_appetite", "pain_behind_the_eyes",
    "back_pain", "constipation", "abdominal_pain", "diarrhoea", "mild_fever", "yellow_urine",
    "yellowing_of_eyes", "acute_liver_failure", "fluid_overload", "swelling_of_stomach",
    "swelled_lymph_nodes", "malaise", "blurred_and_distorted_vision", "phlegm",
    "throat_irritation", "redness_of_eyes", "sinus_pressure", "runny_nose", "congestion",
    "chest_pain", "weakness_in_limbs", "fast_heart_rate", "pain_during_bowel_movements",
    "pain_in_anal_region", "bloody_stool", "irritation_in_anus", "neck_pain", "dizziness",
    "cramps", "bruising", "obesity", "swollen_legs", "swollen_blood_vessels", "puffy_face_and_eyes",
    "enlarged_thyroid", "brittle_nails", "swollen_extremeties", "excessive_hunger",
    "extra_marital_contacts", "drying_and_tingling_lips", "slurred_speech", "knee_pain",
    "hip_joint_pain", "muscle_weakness", "stiff_neck", "swelling_joints", "movement_stiffness",
    "spinning_movements", "loss_of_balance", "unsteadiness", "weakness_of_one_body_side",
    "loss_of_smell", "bladder_discomfort", "foul_smell_of_urine", "continuous_feel_of_urine",
    "passage_of_gases", "internal_itching", "toxic_look_(typhos)", "depression", "irritability",
    "muscle_pain", "altered_sensorium", "red_spots_over_body", "belly_pain", "abnormal_menstruation",
    "dischromic_patches", "watering_from_eyes", "increased_appetite", "polyuria", "family_history",
    "mucoid_sputum", "rusty_sputum", "lack_of_concentration", "visual_disturbances",
    "receiving_blood_transfusion", "receiving_unsterile_injections", "coma", "stomach_bleeding",
    "distention_of_abdomen", "history_of_alcohol_consumption", "fluid_overload", "blood_in_sputum",
    "prominent_veins_on_calf", "palpitations", "painful_walking", "pus_filled_pimples",
    "blackheads", "scurring", "skin_peeling", "silver_like_dusting", "small_dents_in_nails",
    "inflammatory_nails", "blister", "red_sore_around_nose", "yellow_crust_ooze"
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/chat_response', methods=['POST'])
def chat_response():
    if request.method == 'POST':
        try:
            sym1 = request.form.get("data")
            if not sym1:
                return jsonify({'response': 'Please enter at least 4 symptoms!'})

            # Split symptoms by commas
            sym1 = re.split(r'\s*,\s*', sym1.strip())
            corrected_symptoms = []
            wrong_symptoms = []

            # Match symptoms with the predefined list
            for symptom in sym1:
                corrected_symptom = difflib.get_close_matches(symptom.strip(), symptoms, n=1)
                if corrected_symptom:
                    corrected_symptoms.append(corrected_symptom[0])
                else:
                    wrong_symptoms.append(symptom)

            # Capitalize the matched symptoms
            corrected_symptoms = [s.capitalize() for s in corrected_symptoms]

            if len(corrected_symptoms) < 4:
                return jsonify({'response': 'Please enter at least 4 symptoms!'})

            if wrong_symptoms:
                wrong_symptom_str = ' and '.join([f'"{wrong}"' for wrong in wrong_symptoms])
                return jsonify({'response': f"The symptoms {wrong_symptom_str} are not in our database. Please try again!"})

            # Join symptoms into a single string to pass to the model
            symptoms_input = ",".join(corrected_symptoms)
            result = predictDisease(symptoms_input)

            precaution_list = result["Precaution"].split(", ")
            precaution_string = "<br>".join(precaution_list)

            doctor_msg = "It is essential to consult healthcare professionals for accurate diagnosis and treatment!"

            return jsonify({
                'disease': result['Disease'],
                'description': result['Description'],
                'precaution': precaution_string,
                'doctor_msg': doctor_msg
            })

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'response': 'An error occurred. Please check the symptoms and try again.'})

# Remove the open_browser function and the threading code to prevent automatic browser opening

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
