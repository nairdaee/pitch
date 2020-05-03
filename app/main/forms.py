from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch title', validators = [Required()])
    description = TextAreaField('Pitch description', validators = [Required()])
    category = category = SelectField('Select category', choices=[('pickup', 'Pick Up Lines'), ('entertainment', 'Entertainment'), ('motivational', 'Motivational')])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Pitch Comment', validators=[Required()])
    submit = SubmitField('Submit')