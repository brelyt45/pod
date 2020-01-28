from flask_wtf import FlaskForm
from wtforms import Form, FieldList, FormField, IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError
import re


class ParlayPickForm(Form):
    sport = SelectField('sport', choices=[('MLB', 'MLB'), ('NBA', 'NBA'), ('NCAAB', 'NCAAB'), ('NCAAF', 'NCAAF'), ('NFL', 'NFL'), ('NHL', 'NHL')])
    team = SelectField('team', choices=[])
    linetype = SelectField('linetype', choices=[('Spread', 'Spread'), ('MoneyLine', 'MoneyLine'), ('Over/Under', 'Over/Under'), ('Prop', 'Prop')])
    line = StringField('line', validators=[DataRequired(), Length(max=60)])
    date = StringField()

    def validate_email(self, line):
        overunderpattern = re.compile(r'(^[ou][1-9]\d*(.5)?$)')
        spreadpattern = re.compile(r'(^[-+]?[1-9]\d*(\.5)?$)')

        if not bool(overunderpattern.match(line.data)):
            raise ValidationError("Invalid over/under expression.  Examples: o48, u49.5")

        if not bool(spreadpattern.match(line.data)):

            # Python regex for line ([ou][1-9]\d*(.5)?)|([-+]?[1-9]\d*(\.5)?)
            # link to proof https://regex101.com/r/Yr1qFJ/1


class ParlayForm(FlaskForm):
