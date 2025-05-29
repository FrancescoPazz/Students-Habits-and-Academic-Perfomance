import os
import pandas as pd
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .forms import (IdentifiersForm, DemographicsForm, AcademicEngagementForm, 
                   LifestyleHealthForm, ScreenActivityForm, FamilySocioeconomicForm,
                   PersonalSkillsForm, BehaviorPreferencesForm)
from .model_inference import predict_exam_score

CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'data',
                        'enhanced_student_habits_performance_dataset.csv')

df = pd.read_csv(CSV_PATH)

STEP_ORDER = [
    'identifiers',
    'demographics', 
    'academic_engagement',
    'lifestyle_health',
    'screen_activity',
    'family_socioeconomic',
    'personal_skills',
    'behavior_preferences'
]

STEP_NAMES = {
    'identifiers': 'Identifiers',
    'demographics': 'Demographics',
    'academic_engagement': 'Academic Engagement',
    'lifestyle_health': 'Lifestyle & Health',
    'screen_activity': 'Screen Activity',
    'family_socioeconomic': 'Family & Socioeconomic Support',
    'personal_skills': 'Personal Skills',
    'behavior_preferences': 'Behavior & Preferences'
}

main = Blueprint('main', __name__)

@main.route('/')
def home():
    session.clear()
    return redirect(url_for('main.step', step_name='identifiers'))

@main.route('/step/<step_name>', methods=['GET', 'POST'])
def step(step_name):
    if step_name not in STEP_ORDER:
        flash('Step non valido', 'error')
        return redirect(url_for('main.home'))
    
    current_step_index = STEP_ORDER.index(step_name)
    
    if 'form_data' not in session:
        session['form_data'] = {}
    
    form = get_form_for_step(step_name)
    
    if form.validate_on_submit():
        session['form_data'].update({field.name: field.data for field in form if field.name != 'csrf_token'})
        session.modified = True
        
        if current_step_index < len(STEP_ORDER) - 1:
            next_step = STEP_ORDER[current_step_index + 1]
            return redirect(url_for('main.step', step_name=next_step))
        else:
            return redirect(url_for('main.predict'))
    
    if step_name in session.get('form_data', {}):
        for field in form:
            if field.name in session['form_data']:
                field.data = session['form_data'][field.name]
    
    prev_step = STEP_ORDER[current_step_index - 1] if current_step_index > 0 else None
    next_step = STEP_ORDER[current_step_index + 1] if current_step_index < len(STEP_ORDER) - 1 else None
    
    return render_template('step.html', 
                         form=form, 
                         step_name=step_name,
                         step_title=STEP_NAMES[step_name],
                         current_step=current_step_index + 1,
                         total_steps=len(STEP_ORDER),
                         prev_step=prev_step,
                         next_step=next_step,
                         is_last_step=(current_step_index == len(STEP_ORDER) - 1))

@main.route('/previous/<step_name>')
def previous_step(step_name):
    current_step_index = STEP_ORDER.index(step_name)
    if current_step_index > 0:
        prev_step = STEP_ORDER[current_step_index - 1]
        return redirect(url_for('main.step', step_name=prev_step))
    return redirect(url_for('main.home'))

@main.route('/predict')
def predict():
    if 'form_data' not in session or not session['form_data']:
        flash('Nessun dato trovato. Ricompila il form.', 'error')
        return redirect(url_for('main.home'))
    
    try:
        score = predict_exam_score(session['form_data'])
        return render_template('result.html', score=score)
    except Exception as e:
        flash(f'Errore nella predizione: {str(e)}', 'error')
        return redirect(url_for('main.home'))

def get_form_for_step(step_name):
    """Restituisce il form appropriato per lo step"""
    forms_map = {
        'identifiers': IdentifiersForm,
        'demographics': DemographicsForm,
        'academic_engagement': AcademicEngagementForm,
        'lifestyle_health': LifestyleHealthForm,
        'screen_activity': ScreenActivityForm,
        'family_socioeconomic': FamilySocioeconomicForm,
        'personal_skills': PersonalSkillsForm,
        'behavior_preferences': BehaviorPreferencesForm
    }
    
    form_class = forms_map[step_name]
    
    if step_name == 'demographics':
        major_choices = [(m, m) for m in sorted(df['major'].dropna().unique())]
        return form_class(major_choices=major_choices)
    elif step_name == 'family_socioeconomic':
        internet_choices = [(i, i) for i in sorted(df['internet_quality'].dropna().unique())]
        return form_class(internet_choices=internet_choices)
    else:
        return form_class()

@main.route('/about')
def about():
    students = [
        {'name': 'Francesco Pazzaglia', 'id': '0001077423'},
        {'name': 'Filippo Massari', 'id': '0001071420'}
    ]
    return render_template('about.html', students=students)