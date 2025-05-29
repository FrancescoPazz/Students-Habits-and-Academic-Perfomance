import joblib
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), '..', 'best_xgb_model.pkl')
model = joblib.load(model_path)

def predict_exam_score(input_data):
    """
    Predice il punteggio dell'esame basato sui dati di input
    """
    processed_data = process_input_data(input_data)
    
    prediction = model.predict([processed_data])[0]
    return round(prediction, 2)

def process_input_data(input_data):
    """
    Processa i dati di input per la predizione
    """
    feature_order = [
        'access_to_tutoring', 'part_time_job', 'dropout_risk', 'extracurricular_participation',  # binary
        'parental_support_level', 'family_income_range', 'parental_education_level', 
        'diet_quality', 'internet_quality',  # ordinal
        'gender', 'major', 'learning_style', 'study_environment',  # nominal
        # numerical features
        'age', 'study_hours_per_day', 'attendance_percentage', 'previous_gpa', 'semester',
        'sleep_hours', 'exercise_frequency', 'mental_health_rating', 'stress_level',
        'exam_anxiety_score', 'screen_entertainment_hours', 'screen_productivity_hours',
        'social_activity', 'screen_time', 'motivation_level', 'time_management_score'
    ]
    
    processed = []
    
    for feature in feature_order:
        value = input_data.get(feature, 0)
        
        # Processa i valori categorici
        if feature in ['access_to_tutoring', 'part_time_job', 'extracurricular_participation']:
            processed.append(1 if value == 'Yes' else 0)
        elif feature == 'dropout_risk':
            processed.append(1 if value == 'Yes' else 0)
        elif feature == 'family_income_range':
            mapping = {'Low': 0, 'Medium': 1, 'High': 2}
            processed.append(mapping.get(value, 1))
        elif feature == 'parental_education_level':
            mapping = {'High School': 0, 'Some College': 1, 'Bachelor': 2, 'Master': 3, 'PhD': 4}
            processed.append(mapping.get(value, 2))
        elif feature == 'diet_quality':
            mapping = {'Poor': 0, 'Fair': 1, 'Good': 2}
            processed.append(mapping.get(value, 1))
        elif feature == 'internet_quality':
            mapping = {'Low': 0, 'Medium': 1, 'High': 2}
            processed.append(mapping.get(value, 1))
        elif feature == 'gender':
            mapping = {'Male': 0, 'Female': 1, 'Other': 2}
            processed.append(mapping.get(value, 0))
        elif feature == 'learning_style':
            mapping = {'Visual': 0, 'Auditory': 1, 'Kinesthetic': 2, 'Reading/Writing': 3}
            processed.append(mapping.get(value, 0))
        elif feature == 'study_environment':
            mapping = {'Quiet': 0, 'Noisy': 1, 'Library': 2, 'Home': 3}
            processed.append(mapping.get(value, 0))
        elif feature == 'major':
            # Per il major, usa un mapping semplice basato su hash
            processed.append(hash(str(value)) % 100)
        else:
            # Feature numeriche
            processed.append(float(value) if value else 0.0)
    
    return processed