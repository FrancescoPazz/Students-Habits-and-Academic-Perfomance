import joblib
import pandas as pd
import os

model_path = os.path.join(os.path.dirname(__file__), '..', 'best_xgb_model.pkl')
preprocessor_path = os.path.join(os.path.dirname(__file__), '..', 'preprocessor.pkl')

model = joblib.load(model_path)
preprocessor = joblib.load(preprocessor_path)

def predict_exam_score(input_data):
    try:
        df = pd.DataFrame([input_data])
        
        X_processed = preprocessor.transform(df)
        
        prediction = model.predict(X_processed)[0]
        
        return round(prediction, 2)
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e
