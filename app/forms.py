from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email

app = Flask (__name__)
app.config['SECRET_KEY'] = 'thisismykey'

class UploadForm(FlaskForm):
    image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg','png','Images only!'])
    ])
    
    