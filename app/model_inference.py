import joblib
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), '..', 'best_xgb_model.pkl')
model = joblib.load(model_path)

def predict_exam_score(input_data):
    processed_data = process_input_data(input_data)
    
    prediction = model.predict([processed_data])[0]
    return round(prediction, 2)

def process_input_data(input_data):
    feature_order = [
        'access_to_tutoring', 'part_time_job', 'dropout_risk', 'extracurricular_participation',

        'parental_support_level', 'family_income_range', 'parental_education_level', 
        'diet_quality', 'internet_quality',

        'gender', 'major', 'learning_style', 'study_environment',

        'age', 'study_hours_per_day', 'attendance_percentage', 'previous_gpa', 'semester',
        'sleep_hours', 'exercise_frequency', 'mental_health_rating', 'stress_level',
        'exam_anxiety_score', 'screen_entertainment_hours', 'screen_productivity_hours',
        'social_activity', 'screen_time', 'motivation_level', 'time_management_score'
    ]
    
    processed = []
    
    for feature in feature_order:
        value = input_data.get(feature, 0)
        
        if feature in ['access_to_tutoring', 'part_time_job', 'extracurricular_participation', 'dropout_risk']:
            processed.append(1 if value == 'Yes' else 0)
        elif feature == 'parental_support_level':
            mapping = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9}
            processed.append(mapping.get(value, 4))
        elif feature in ['family_income_range', 'internet_quality']:
            mapping = {'Low': 0, 'Medium': 1, 'High': 2}
            processed.append(mapping.get(value, 1))
        elif feature == 'parental_education_level':
            mapping = {'High School': 0, 'Some College': 1, 'Bachelor': 2, 'Master': 3, 'PhD': 4}
            processed.append(mapping.get(value, 2))
        elif feature == 'diet_quality':
            mapping = {'Poor': 0, 'Fair': 1, 'Good': 2}
            processed.append(mapping.get(value, 1))
        elif feature == 'gender':
            mapping = {'Female': 0, 'Male': 1, 'Other': 2}
            processed.append(mapping.get(value, 0))
        elif feature == 'major':
            mapping = {'Arts': 0, 'Biology': 1, 'Business': 2, 'Computer Science': 3, 'Engineering': 4, 'Psychology': 5, 'Other': 6}
            processed.append(mapping.get(value, 4))
        elif feature == 'learning_style':
            mapping = {'Auditory': 0, 'Kinesthetic': 1, 'Reading': 2, 'Visual': 3}
            processed.append(mapping.get(value, 0))
        elif feature == 'study_environment':
            mapping = {'Cafe': 0, 'Co-Learning Group': 1, 'Dorm': 2, 'Library': 3, 'Quiet Room': 4}
            processed.append(mapping.get(value, 0))
        else:
            processed.append(float(value) if value else 0.0)
    
    return processed