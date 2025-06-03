from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .forms import (IdentifiersForm, DemographicsForm, AcademicEngagementForm, 
                   LifestyleHealthForm, ScreenActivityForm, FamilySocioeconomicForm,
                   PersonalSkillsForm, BehaviorPreferencesForm)
from .model_inference import predict_exam_score

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
    
    if request.method == 'GET':
        for field in form:
            if field.name in session.get('form_data', {}) and field.name != 'csrf_token':
                field.data = session['form_data'][field.name]
    
    if form.validate_on_submit():
        form_data_to_save = {}
        for field in form:
            if field.name not in ['csrf_token', 'submit']:
                if field.name == 'major' and field.data == 'Other':
                    form_data_to_save['major'] = form.custom_major.data
                elif field.name != 'custom_major':
                    form_data_to_save[field.name] = field.data
        
        if step_name == 'screen_activity':
            screen_productivity = form_data_to_save.get('screen_productivity_hours', 0)
            screen_entertainment = form_data_to_save.get('screen_entertainment_hours', 0)
            form_data_to_save['screen_time'] = screen_productivity + screen_entertainment
        
        session['form_data'].update(form_data_to_save)
        session.modified = True
        
        if current_step_index < len(STEP_ORDER) - 1:
            next_step = STEP_ORDER[current_step_index + 1]
            return redirect(url_for('main.step', step_name=next_step))
        else:
            return redirect(url_for('main.predict'))
    
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
    form = form_class(data=session.get('form_data', {}))

    return form

@main.route('/test_bad_student')
def test_bad_student():
    studente_pessimo = {
        'age': 19,
        'gender': 'Male',
        'major': 'Arts',
        'semester': 1,
        'study_hours_per_day': 0.5,
        'attendance_percentage': 30.0,
        'access_to_tutoring': 'No',
        'extracurricular_participation': 'No',
        'previous_gpa': 1.2,
        'sleep_hours': 4.0,
        'diet_quality': 'Poor',
        'exercise_frequency': 0,
        'mental_health_rating': 2.0,
        'stress_level': 9.0,
        'exam_anxiety_score': 10,
        'screen_entertainment_hours': 12.0,
        'screen_productivity_hours': 1.0,
        'social_activity': 0,
        'screen_time': 13.0,
        'family_income_range': 'Low',
        'parental_education_level': 'High School',
        'parental_support_level': '1',
        'internet_quality': 'Low',
        'time_management_score': 1,
        'motivation_level': 1,
        'learning_style': 'Visual',
        'part_time_job': 'Yes',
        'dropout_risk': 'Yes',
        'study_environment': 'Cafe'  
    }
    
    try:
        score = predict_exam_score(studente_pessimo)
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Studente Pessimo</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body class="bg-light">
            <div class="container mt-5">
                <div class="row justify-content-center">
                    <div class="col-md-8">
                        <div class="card shadow">
                            <div class="card-header bg-dark text-white">
                                <h2 class="mb-0">Test Studente con prestazioni basse</h2>
                            </div>
                            <div class="card-body">
                                
                                <div class="row">
                                    <div class="col-md-6">
                                        <h5>Risultati</h5>
                                        <table class="table table-sm">
                                            <tr><td><strong>Exam score:</strong></td><td><span class="badge bg-primary fs-6">{score}</span></td></tr>
                                        </table>
                                    </div>
                                    
                                    <div class="col-md-6">
                                        <h5>Caratteristiche Negative</h5>
                                        <ul class="list-group list-group-flush">
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>GPA Precedente:</span><span class="badge bg-danger">{studente_pessimo['previous_gpa']}</span>
                                            </li>
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Ore Studio/giorno:</span><span class="badge bg-danger">{studente_pessimo['study_hours_per_day']}</span>
                                            </li>
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Frequenza (%):</span><span class="badge bg-danger">{studente_pessimo['attendance_percentage']}</span>
                                            </li>
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Salute Mentale:</span><span class="badge bg-danger">{studente_pessimo['mental_health_rating']}/10</span>
                                            </li>
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Motivazione:</span><span class="badge bg-danger">{studente_pessimo['motivation_level']}/10</span>
                                            </li>
                                            <li class="list-group-item d-flex justify-content-between">
                                                <span>Ansia Esami:</span><span class="badge bg-danger">{studente_pessimo['exam_anxiety_score']}/10</span>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                                
                                <div class="mt-4">
                                    <h5>Tutti i Dati del Test</h5>
                                    <div class="row">
                                        <div class="col-md-4">
                                            <h6>Accademico</h6>
                                            <small>
                                                <strong>Major:</strong> {studente_pessimo['major']}<br>
                                                <strong>Semestre:</strong> {studente_pessimo['semester']}<br>
                                                <strong>Tutoraggio:</strong> {studente_pessimo['access_to_tutoring']}<br>
                                                <strong>Extracurriculari:</strong> {studente_pessimo['extracurricular_participation']}
                                            </small>
                                        </div>
                                        <div class="col-md-4">
                                            <h6>Salute & Lifestyle</h6>
                                            <small>
                                                <strong>Ore Sonno:</strong> {studente_pessimo['sleep_hours']}<br>
                                                <strong>Dieta:</strong> {studente_pessimo['diet_quality']}<br>
                                                <strong>Esercizio/sett:</strong> {studente_pessimo['exercise_frequency']}<br>
                                                <strong>Stress:</strong> {studente_pessimo['stress_level']}/10
                                            </small>
                                        </div>
                                        <div class="col-md-4">
                                            <h6>Famiglia</h6>
                                            <small>
                                                <strong>Reddito:</strong> {studente_pessimo['family_income_range']}<br>
                                                <strong>Educazione Genitori:</strong> {studente_pessimo['parental_education_level']}<br>
                                                <strong>Supporto:</strong> {studente_pessimo['parental_support_level']}/10<br>
                                                <strong>Internet:</strong> {studente_pessimo['internet_quality']}
                                            </small>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="mt-4 d-flex gap-2">
                                    <a href="{url_for('main.test_bad_student')}" class="btn btn-success">🌟 Confronta con Studente Eccellente</a>
                                    <a href="{url_for('main.home')}" class="btn btn-primary">🏠 Torna Home</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        
    except Exception as e:
        import traceback
        return f"""
        <h1>Errore nel Test</h1>
        <p><strong>Errore:</strong> {str(e)}</p>
        <pre>{traceback.format_exc()}</pre>
        <a href='{url_for('main.home')}'>Torna Home</a>
        """


@main.route('/about')
def about():
    students = [
        {'name': 'Francesco Pazzaglia', 'id': '0001077423'},
        {'name': 'Filippo Massari', 'id': '0001071420'}
    ]
    return render_template('about.html', students=students)