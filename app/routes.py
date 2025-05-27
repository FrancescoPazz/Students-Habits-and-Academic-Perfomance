import os
import pandas as pd
from flask import Blueprint, render_template, request
from .forms import StudentForm
from .model_inference import predict_exam_score

CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'data',
                        'enhanced_student_habits_performance_dataset.csv')

df = pd.read_csv(CSV_PATH)

major_choices = sorted(df['major'].dropna().unique())
major_choices = [(m, m) for m in major_choices]

internet_choices = sorted(df['internet_quality'].dropna().unique())
internet_choices = [(i, i) for i in internet_choices]

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    form = StudentForm(
        major_choices=major_choices,
        internet_choices=internet_choices
    )

    if form.validate_on_submit():
        data = {field.name: field.data for field in form}
        score = predict_exam_score(data)
        return render_template('result.html', score=score)

    return render_template('home.html', form=form)


@main.route('/about')
def about():
    students = [
        {'name': 'Francesco Pazzaglia', 'role': '0001077423'},
        {'name': 'Mattia Massari', 'role': '00010714020'}
    ]
    return render_template('about.html', students=students)
