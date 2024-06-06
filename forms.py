from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField
# from wtforms.validators import DataRequired

class AvalonForm(FlaskForm):
    merlin = BooleanField('Merlin', default=True)
    assassin = BooleanField('Skrytobójca', default=True)
    parsifal = BooleanField('Parsifal')
    lancelot = BooleanField('Lancelot')
    morgana = BooleanField('Morgana')
    mordred = BooleanField('Mordred')
    oberon = BooleanField('Oberon')
    submit = SubmitField('Zacznij Noc')
