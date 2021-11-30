
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField, StringField
from wtforms.validators import DataRequired, InputRequired, NoneOf


class ResultsForm(FlaskForm):
    """Result form. Defines the validators of variables and
    the form of the request."""

    matr_nr = IntegerField("Matrikelnummer",
                          validators=[DataRequired(), InputRequired()])

    vst_nr = IntegerField("Veranstaltungsnummer",
                         validators=[DataRequired(), InputRequired()])

    persNr_prof = IntegerField("Personalnummer des Professors",
                               validators=[DataRequired(), InputRequired()])

    persNr_assist = IntegerField("Personalnummer des Assistenten",
                               validators=[DataRequired(), InputRequired()])

    result = FloatField("Bewertung",
                        validators=[DataRequired(), InputRequired()])

    name = StringField("Nachname der Person", validators=[DataRequired(), InputRequired(), NoneOf((0,1,2,3,4,5,6,7,8, 9), "Keine Zahlen")])

    vorname = StringField("Vorname der Person", validators=[])

    rang = StringField("Rang der Person", validators=[DataRequired(), InputRequired()])

    gebaeude = StringField("Gebäude in dem unterrichtet wird", validators=[DataRequired(), InputRequired()])

    fachgebiet = StringField("Fachgebiet des Assistenten", validators=[DataRequired(), InputRequired()])

    semester = IntegerField("Semester des Studenten",
                         validators=[DataRequired(), InputRequired()])

    raum = IntegerField("Vorlesungsraum",
                            validators=[DataRequired(), InputRequired()])

    kurs = StringField("Kurs des Studenten", validators=[DataRequired(), InputRequired()])

    sws = IntegerField("Semesterwochen",
                            validators=[DataRequired(), InputRequired()])

    title = StringField("Titel der Veranstaltung", validators=[DataRequired(), InputRequired()])

    zugeordnet = IntegerField("zugeordneter Professor", validators=[DataRequired(), InputRequired()])

    pre_event = IntegerField("Vorgänger-Veranstaltung", validators=[DataRequired()])

    submit = SubmitField('Speichern')

    submit2 = SubmitField('Ausgabe')

    submit3 = SubmitField('Suche')

    submit4 = SubmitField('Löschen')

    number = IntegerField('Matrikelnummer oder Personalnummer',
                          validators=[DataRequired(), InputRequired()])

    number2 = IntegerField('Personalnummer des Professors oder eines Assistenten',
                          validators=[DataRequired(), InputRequired()])
