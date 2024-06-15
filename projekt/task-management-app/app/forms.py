from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    status = SelectField('Status', choices=[
        ('to-do', 'To Do'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed')
    ], validators=[DataRequired()])
    due_date = DateTimeField('Due Date', format='%Y-%m-%d %H:%M:%S', render_kw={'placeholder': 'YYYY-MM-DD HH:MM:SS'})
    submit = SubmitField('Submit')
