from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

class IdentifiersForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    submit = SubmitField('Next')

class DemographicsForm(FlaskForm):
    age = IntegerField('Age (10-100)', validators=[DataRequired(), NumberRange(min=10, max=100)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    major = SelectField('Major', choices=[('Arts', 'Arts'), ('Biology', 'Biology'), ('Business', 'Business'), ('Computer Science', 'Computer Science'), ('Engineering', 'Engineering'), ('Psychology', 'Psychology'), ('Other', 'Other')])
    custom_major = StringField('Custom Major', validators=[Optional()])
    submit = SubmitField('Next')

    def validate(self, extra_validators=None):
        if not super().validate(extra_validators):
            return False
        
        if self.major.data == 'Other' and not self.custom_major.data:
            self.custom_major.errors.append('Insert a custom major if "Other" is selected')
            return False
            
        return True

class AcademicEngagementForm(FlaskForm):
    semester = IntegerField('Semester (1-8)', validators=[DataRequired(), NumberRange(min=1, max=8)])
    study_hours_per_day = FloatField('Study Hours per Day (0-24)', validators=[DataRequired(), NumberRange(min=0, max=24)])
    attendance_percentage = FloatField('Attendance Percentage (0-100)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    access_to_tutoring = SelectField('Access to Tutoring', choices=[('Yes', 'Yes'), ('No', 'No')])
    extracurricular_participation = SelectField('Extracurricular Participation', choices=[('Yes', 'Yes'), ('No', 'No')])
    previous_gpa = FloatField('Previous GPA (0-4)', validators=[DataRequired(), NumberRange(min=0, max=4)])
    submit = SubmitField('Next')

class LifestyleHealthForm(FlaskForm):
    sleep_hours = FloatField('Sleep Hours (0-24)', validators=[DataRequired(), NumberRange(min=0, max=24)])
    diet_quality = SelectField('Diet Quality', choices=[('Poor', 'Poor'), ('Fair', 'Fair'), ('Good', 'Good')])
    exercise_frequency = IntegerField('Exercise Frequency (days/week, 0-7)', validators=[DataRequired(), NumberRange(min=0, max=7)])
    mental_health_rating = FloatField('Mental Health Rating (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    stress_level = FloatField('Stress Level (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    exam_anxiety_score = IntegerField('Exam Anxiety Score (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Next')

class ScreenActivityForm(FlaskForm):
    screen_productivity_hours = FloatField('Screen Productivity Hours (0-24)', validators=[DataRequired(), NumberRange(min=0, max=24)])
    screen_entertainment_hours = FloatField('Screen Entertainment Hours (0-24)', validators=[DataRequired(), NumberRange(min=0, max=24)])
    social_activity = IntegerField('Social Activity (events/week, 0-20)', validators=[DataRequired(), NumberRange(min=0, max=20)])
    submit = SubmitField('Next')
    
    def validate(self, extra_validators=None):
        if not super().validate(extra_validators):
            return False
        
        total_screen = (self.screen_productivity_hours.data or 0) + (self.screen_entertainment_hours.data or 0)
        if total_screen > 24:
            self.screen_productivity_hours.errors.append('Total screen time cannot exceed 24 hours')
            return False
            
        return True
    
class FamilySocioeconomicForm(FlaskForm):
    family_income_range = SelectField('Family Income Range', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    parental_education_level = SelectField('Parental Education Level', 
                                         choices=[('High School', 'High School'), 
                                                ('Some College', 'Some College'),
                                                ('Bachelor', 'Bachelor'),
                                                ('Master', 'Master'),
                                                ('PhD', 'PhD')])
    parental_support_level = IntegerField('Parental Support Level (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    internet_quality = SelectField('Internet Quality', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    submit = SubmitField('Next')
    
    def __init__(self, internet_choices=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if internet_choices:
            self.internet_quality.choices = internet_choices

class PersonalSkillsForm(FlaskForm):
    time_management_score = IntegerField('Time Management Score (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    motivation_level = IntegerField('Motivation Level (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    learning_style = SelectField('Learning Style', 
                                choices=[('Auditory', 'Auditory'), 
                                         ('Kinesthetic', 'Kinesthetic'), 
                                         ('Reading', 'Reading'),
                                         ('Visual', 'Visual')])
    submit = SubmitField('Next')

class BehaviorPreferencesForm(FlaskForm):
    part_time_job = SelectField('Part-time Job', choices=[('Yes', 'Yes'), ('No', 'No')])
    dropout_risk = SelectField('Dropout Risk', choices=[('Yes', 'Yes'), ('No', 'No')])
    study_environment = SelectField('Study Environment', 
                                   choices=[('Cafe', 'Cafe'), 
                                          ('Co-Learning Group', 'Co-Learning Group'), 
                                          ('Dorm', 'Dorm'),
                                          ('Library', 'Library'),
                                          ('Quiet Room', 'Quiet Room')])
    submit = SubmitField('Predict Score')