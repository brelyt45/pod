from flask_wtf import FlaskForm
from wtforms import Form, FieldList, FormField, IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError, Regexp
import re
from pod.teamnames import mlbtup


class NonValidatingSelectField(SelectField):
    def pre_validate(self, form):
        pass


class NonValidatingStringField(StringField):
    def pre_validate(self, form):
        pass


class ParlayPickForm(FlaskForm):
    sport = SelectField('sport', choices=[('MLB', 'MLB'), ('NBA', 'NBA'), ('NCAAB', 'NCAAB'), ('NCAAF', 'NCAAF'), ('NFL', 'NFL'), ('NHL', 'NHL')])
    team = NonValidatingSelectField('team', choices=mlbtup)
    linetype = SelectField('linetype', choices=[('Spread', 'Spread'), ('MoneyLine', 'MoneyLine'), ('Over/Under', 'Over/Under'), ('Prop', 'Prop')])
    line = StringField('line')
    date = StringField()

    # def validate_line(self, line):
    #     overunderpattern = re.compile(r'(^[ou][1-9]\d*(.5)?$)+')
    #     spreadpattern = re.compile(r'(^[-+]?[1-9]\d*(\.5)?$)+')

    #     if self.linetype.data == 'Over/Under':
    #         if not bool(overunderpattern.match(line.data)):
    #             raise ValidationError("Invalid over/under expression.  Examples: o48, u49.5")

    #     elif self.linetype.data == 'Spread':
    #         if not bool(spreadpattern.match(line.data)):
    #             raise ValidationError("Invalid spread expression. Examples: 8, +8.5, -2.5")

    #         # Python regex for line ([ou][1-9]\d*(.5)?)|([-+]?[1-9]\d*(\.5)?)
    #         # link to proof https://regex101.com/r/Yr1qFJ/1


class ParlayForm(FlaskForm):
    picks = FieldList(FormField(ParlayPickForm), min_entries=1, max_entries=10)
