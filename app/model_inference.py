import joblib
import numpy as np

model = joblib.load('model.pkl')

def predict_exam_score(input_data):
    feature_order = [
        'age', 'gender', 'major', 'study_hours_per_day', 'attendance_percentage',
        'extracurricular_participation', 'previous_gpa', 'semester',
        'access_to_tutoring', 'sleep_hours', 'diet_quality', 'exercise_frequency',
        'mental_health_rating', 'stress_level', 'exam_anxiety_score',
        'screen_entertainment_hours', 'screen_productivity_hours',
        'social_activity', 'screen_time', 'parental_education_level',
        'internet_quality', 'family_income_range', 'parental_support_level',
        'motivation_level', 'learning_style', 'time_management_score',
        'part_time_job', 'dropout_risk', 'study_environment'
    ]

    processed = []
    for feat in feature_order:
        val = input_data.get(feat)
        if val in ['Yes', 'yes']:
            processed.append(1)
        elif val in ['No', 'no']:
            processed.append(0)
        elif isinstance(val, str):
            processed.append(hash(val) % 1000)
        else:
            processed.append(float(val))

    prediction = model.predict([processed])[0]
    return round(prediction, 2)
