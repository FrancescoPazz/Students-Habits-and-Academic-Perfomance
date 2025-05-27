from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=['Male', 'Female', 'Other'])
    major = SelectField('Major', choices=[])
    study_hours_per_day = FloatField('Study Hours per Day', validators=[DataRequired()])
    attendance_percentage = FloatField('Attendance %', validators=[DataRequired()])
    extracurricular_participation = SelectField('Extracurricular', choices=['Yes', 'No'])
    previous_gpa = FloatField('Previous GPA', validators=[DataRequired()])
    semester = IntegerField('Semester', validators=[DataRequired()])
    access_to_tutoring = SelectField('Access to Tutoring', choices=['Yes', 'No'])
    sleep_hours = FloatField('Sleep Hours', validators=[DataRequired()])
    diet_quality = IntegerField('Diet Quality (1-10)', validators=[DataRequired()])
    exercise_frequency = IntegerField('Exercise/Week', validators=[DataRequired()])
    mental_health_rating = IntegerField('Mental Health (1-10)', validators=[DataRequired()])
    stress_level = IntegerField('Stress Level (1-10)', validators=[DataRequired()])
    exam_anxiety_score = FloatField('Exam Anxiety Score', validators=[DataRequired()])
    screen_entertainment_hours = FloatField('Screen Hours (Entertainment)', validators=[DataRequired()])
    screen_productivity_hours = FloatField('Screen Hours (Productivity)', validators=[DataRequired()])
    social_activity = FloatField('Social Activity Hours', validators=[DataRequired()])
    screen_time = FloatField('Total Screen Time', validators=[DataRequired()])
    parental_education_level = SelectField('Parental Education Level', choices=['None', 'High School', 'College', 'Graduate'])
    internet_quality = SelectField('Internet Quality', choices=[])
    family_income_range = SelectField('Family Income', choices=['Low', 'Medium', 'High'])
    parental_support_level = IntegerField('Parental Support (1-10)', validators=[DataRequired()])
    motivation_level = IntegerField('Motivation Level (1-10)', validators=[DataRequired()])
    learning_style = SelectField('Learning Style', choices=['Visual', 'Auditory', 'Kinesthetic', 'Reading/Writing'])
    time_management_score = FloatField('Time Management Score', validators=[DataRequired()])
    part_time_job = SelectField('Part-time Job', choices=['Yes', 'No'])
    dropout_risk = FloatField('Dropout Risk (0-1)', validators=[DataRequired()])
    study_environment = SelectField('Study Environment', choices=['Quiet', 'Noisy', 'Shared', 'Private'])

    submit = SubmitField('Predict Exam Score')

    def __init__(self, *args, **kwargs):
        major_choices = kwargs.pop('major_choices', None)
        internet_choices = kwargs.pop('internet_choices', None)
        super().__init__(*args, **kwargs)

        if major_choices is not None:
            self.major.choices = major_choices
        if internet_choices is not None:
            self.internet_quality.choices = internet_choices