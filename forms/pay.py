from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class PayForm(FlaskForm):
    title = StringField('Номер карты', validators=[DataRequired()])
    content = TextAreaField("Пин код")
    progress = StringField('Прогресс')
    submit = SubmitField('Оплатить')