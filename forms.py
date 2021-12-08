
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField, StringField
from wtforms.validators import DataRequired, InputRequired, Length


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

    name = StringField("Nachname der Person", validators=[DataRequired(), InputRequired(), Length(max=30)])

    vorname = StringField("Vorname der Person", validators=[Length(max=30)])

    rang = StringField("Rang der Person", validators=[DataRequired(), InputRequired(), Length(max=2)])

    gebaeude = StringField("Gebäude in dem unterrichtet wird", validators=[DataRequired(), InputRequired(),
                                                                           Length(max=1)])

    fachgebiet = StringField("Fachgebiet des Assistenten", validators=[DataRequired(), InputRequired(), Length(max=30)])

    semester = IntegerField("Semester des Studenten",
                         validators=[DataRequired(), InputRequired()])

    raum = IntegerField("Vorlesungsraum",
                            validators=[DataRequired(), InputRequired()])

    kurs = StringField("Kurs des Studenten", validators=[DataRequired(), InputRequired(), Length(max=10)])

    sws = IntegerField("Semesterwochen",
                            validators=[DataRequired(), InputRequired()])

    title = StringField("Titel der Veranstaltung", validators=[DataRequired(), InputRequired(), Length(max=30)])

    zugeordnet = IntegerField("zugeordneter Professor", validators=[DataRequired(), InputRequired()])

    pre_event = IntegerField("Vorgänger-Veranstaltung", validators=[])

    submit_save = SubmitField('Speichern')

    submit_output = SubmitField('Ausgabe')

    submit_search = SubmitField('Suche')

    submit_delete = SubmitField('Löschen')

    submit_home = SubmitField('Home')

    number = IntegerField('Matrikelnummer oder Personalnummer',
                          validators=[DataRequired(), InputRequired()])
    number2 = IntegerField('Personalnummer des Professors oder eines Assistenten',
                          validators=[DataRequired(), InputRequired()])
