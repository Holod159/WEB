from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заказ', validators=[DataRequired()])
    content = TextAreaField("Примечание")
    is_private = BooleanField("Оплачен")
    submit = SubmitField('Применить')
    progress = StringField('Прогресс')