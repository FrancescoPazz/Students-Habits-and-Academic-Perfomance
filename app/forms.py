from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class IdentifiersForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    submit = SubmitField('Next')

class DemographicsForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=16, max=28)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    major = SelectField('Major', choices=[])
    submit = SubmitField('Next')
    
    def __init__(self, major_choices=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if major_choices:
            self.major.choices = major_choices

class AcademicEngagementForm(FlaskForm):
    semester = IntegerField('Semester', validators=[DataRequired(), NumberRange(min=1, max=8)])
    study_hours_per_day = FloatField('Study Hours per Day', validators=[DataRequired(), NumberRange(min=0, max=24)])
    attendance_percentage = FloatField('Attendance Percentage', validators=[DataRequired(), NumberRange(min=0, max=100)])
    access_to_tutoring = SelectField('Access to Tutoring', choices=[('Yes', 'Yes'), ('No', 'No')])
    extracurricular_participation = SelectField('Extracurricular Participation', choices=[('Yes', 'Yes'), ('No', 'No')])
    previous_gpa = FloatField('Previous GPA', validators=[DataRequired(), NumberRange(min=0, max=4)])
    submit = SubmitField('Next')

class LifestyleHealthForm(FlaskForm):
    sleep_hours = FloatField('Sleep Hours', validators=[DataRequired(), NumberRange(min=0, max=24)])
    diet_quality = SelectField('Diet Quality', choices=[('Poor', 'Poor'), ('Fair', 'Fair'), ('Good', 'Good')])
    exercise_frequency = IntegerField('Exercise Frequency (times/week)', validators=[DataRequired(), NumberRange(min=0, max=7)])
    mental_health_rating = IntegerField('Mental Health Rating (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    stress_level = IntegerField('Stress Level (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    exam_anxiety_score = IntegerField('Exam Anxiety Score (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Next')

class ScreenActivityForm(FlaskForm):
    screen_time = FloatField('Total Screen Time (hours)', validators=[DataRequired(), NumberRange(min=0, max=24)])
    screen_productivity_hours = FloatField('Screen Productivity Hours', validators=[DataRequired(), NumberRange(min=0, max=24)])
    screen_entertainment_hours = FloatField('Screen Entertainment Hours', validators=[DataRequired(), NumberRange(min=0, max=24)])
    social_activity = IntegerField('Social Activity (events/week)', validators=[DataRequired(), NumberRange(min=0, max=20)])
    submit = SubmitField('Next')

class FamilySocioeconomicForm(FlaskForm):
    family_income_range = SelectField('Family Income Range', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    parental_education_level = SelectField('Parental Education Level', 
                                         choices=[('High School', 'High School'), 
                                                ('Some College', 'Some College'),
                                                ('Bachelor', 'Bachelor'),
                                                ('Master', 'Master'),
                                                ('PhD', 'PhD')])
    parental_support_level = IntegerField('Parental Support Level (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    internet_quality = SelectField('Internet Quality', choices=[])
    submit = SubmitField('Next')
    
    def __init__(self, internet_choices=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if internet_choices:
            self.internet_quality.choices = internet_choices

class PersonalSkillsForm(FlaskForm):
    time_management_score = IntegerField('Time Management Score (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    motivation_level = IntegerField('Motivation Level (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    learning_style = SelectField('Learning Style', 
                                choices=[('Visual', 'Visual'), 
                                       ('Auditory', 'Auditory'), 
                                       ('Kinesthetic', 'Kinesthetic'), 
                                       ('Reading/Writing', 'Reading/Writing')])
    submit = SubmitField('Next')

class BehaviorPreferencesForm(FlaskForm):
    part_time_job = SelectField('Part-time Job', choices=[('Yes', 'Yes'), ('No', 'No')])
    dropout_risk = SelectField('Dropout Risk', choices=[('Yes', 'Yes'), ('No', 'No')])
    study_environment = SelectField('Study Environment', 
                                   choices=[('Quiet', 'Quiet'), 
                                          ('Noisy', 'Noisy'), 
                                          ('Library', 'Library'),
                                          ('Home', 'Home')])
    submit = SubmitField('Predict Score')