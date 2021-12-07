
from flask import Flask, render_template, request



import query_functions as qf
from forms import ResultsForm
import os

app = Flask(__name__, instance_relative_config=False)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



@app.route("/")
def index():
    return render_template('base.html')


@app.route("/append/", methods=["GET", "POST"])
def append_result():
    """
    Loads a form to insert a new test result to database.
    :return: renders a HTML-Template with variables form and error/success message (msg).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        matr_nr = request.form["matr_nr"]
        vst_nr = request.form["vst_nr"]
        persNr_prof = request.form["persNr_prof"]
        result = request.form["result"]
        msg = qf.insert_new_testresult(conn, matr_nr, vst_nr, persNr_prof, result)
        conn.commit()
        conn.close()
        return render_template('append.html', form=form, msg=msg)
    return render_template('append.html', form=form)


@app.route("/append_student_to_event/", methods=["GET", "POST"])
def append_student_to_event():
    """
    Loads a form to insert a student to an existing event.
    :return: renders a HTML-Template with variables form and error/success message (msg).
    """
    form = ResultsForm()
    database = "administration_database.db"
    #create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        matr_nr = request.form["matr_nr"]
        vst_nr = request.form["vst_nr"]
        msg = qf.insert_new_student_to_event(conn, matr_nr, vst_nr)
        conn.commit()
        conn.close()
        return render_template('append.html', form=form, msg=msg)
    return render_template('append.html', form=form)



@app.route("/append_event/", methods=["GET", "POST"])
def insert_new_event():
    """
    Loads a form to insert a new event to database.
    :return: renders a HTML-Template with variables form and error/success message (msg).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        persNr_prof = request.form["persNr_prof"]
        vst_nr = request.form["vst_nr"]
        title = request.form["title"]
        sws = request.form["sws"]
        pre_event = request.form["pre_event"]
        msg = qf.insert_new_event(conn, vst_nr, title, sws, persNr_prof, pre_event)
        conn.commit()
        conn.close()
        return render_template('append.html', form=form, msg=msg)
    return render_template('append.html', form=form)


@app.route("/outputs_professors/", methods=["GET", "POST"])
def select_all_from_professors():
    """
    Loads a form to get all information of table professors.
    :return: renders a HTML-Template with variables form and output message (output).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        output = qf.select_all_from_professors(conn)
        return render_template('outputs.html', form=form, output=output)
    return render_template('outputs.html', form=form)


@app.route("/outputs_assistants/", methods=["GET", "POST"])
def select_all_from_assistants():
    """
    Loads a form to get all information of table assistants.
    :return: renders a HTML-Template with variables form and output message (output).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        output = qf.select_all_from_assistants(conn)
        return render_template('outputs.html', form=form, output=output)
    return render_template('outputs.html', form=form)


@app.route("/outputs/", methods=["GET", "POST"])
def select_all_from_events():
    """
    Loads a form to get all information of table events.
    :return: renders a HTML-Template with variables form and output message (output).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        output = qf.select_all_from_events(conn)
        return render_template('outputs.html', form=form, output=output)
    return render_template('outputs.html', form=form)


@app.route("/outputs_students/", methods=["GET", "POST"])
def select_all_from_students():
    """
    Loads a form to get all information of table students.
    :return: renders a HTML-Template with variables form and output message (output).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        output = qf.select_all_from_students(conn)
        return render_template('outputs.html', form=form, output=output)
    return render_template('outputs.html', form=form)


@app.route("/search_listend_by_student/", methods=["GET", "POST"])
def get_event_listend_by_student():
    """
    Loads a form to search for event/-s of a student by his/her matriculation number.
    :return: renders a HTML-Template with variables form and search message (search).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        matr_nr = request.form["matr_nr"]
        search = qf.get_event_listend_by_student(conn, matr_nr)
        return render_template('search.html', form=form, search=search)
    return render_template('search.html', form=form)


@app.route("/search/", methods=["GET", "POST"])
def get_events_by_person():
    """
    Loads a form to search for event/-s of a person (professor or assistant) by their personnel number.
    :return: renders a HTML-Template with variables form and search message (search).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        number2 = request.form["number2"]
        search = qf.get_event_by_person(conn, number2)
        conn.commit()
        conn.close()
        return render_template('search.html', form=form, search=search)
    return render_template('search.html', form=form)


@app.route("/search_by_number/", methods=["GET", "POST"])
def get_person_by_number():
    """
    Loads a form to search a person by her/his matriculation- or personnel number.
    :return: renders a HTML-Template with variables form and search message (search).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        number = request.form["number"]
        search = qf.get_person_by_number(conn, number)
        return render_template('search.html', form=form, search=search)
    return render_template('search.html', form=form)


@app.route("/search_by_name/", methods=["GET", "POST"])
def get_person_by_name():
    """
    Loads a form to search a person by her/his name.
    :return: renders a HTML-Template with variables form and search message (search).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        name = request.form["name"]
        vorname = request.form["vorname"]
        search = qf.get_person_by_name(conn, name, vorname)
        return render_template('search.html', form=form, search=search)
    return render_template('search.html', form=form)


@app.route("/append_persons/", methods=["GET", "POST"])
def insert_new_professor():
    """
    Loads a form to insert a professor.
    :return: renders a HTML-Template with variables form and error message (msg).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        persNr_prof = request.form["persNr_prof"]
        name = request.form["name"]
        vorname = request.form["vorname"]
        rang = request.form["rang"]
        gebaeude = request.form["gebaeude"]
        raum = request.form["raum"]
        msg = qf.insert_new_professor(conn, persNr_prof, name, vorname, rang, gebaeude, raum)
        conn.commit()
        conn.close()
        return render_template('append_persons.html', form=form, msg=msg)
    return render_template('append_persons.html', form=form)


@app.route("/append_assistant/", methods=["GET", "POST"])
def insert_new_assistant():
    """
    Loads a form to insert a assistant.
    :return: renders a HTML-Template with variables form and error message (msg).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        persNr_assist = request.form["persNr_assist"]
        name = request.form["name"]
        vorname = request.form["vorname"]
        fachgebiet = request.form["fachgebiet"]
        zugeordnet = request.form["zugeordnet"]
        msg = qf.insert_new_assistant(conn, persNr_assist, name, vorname, fachgebiet, zugeordnet)
        conn.commit()
        conn.close()
        return render_template('append_persons.html', form=form, msg=msg)
    return render_template('append_persons.html', form=form)


@app.route("/append_student/", methods=["GET", "POST"])
def insert_new_student():
    """
    Loads a form to insert a student.
    :return: renders a HTML-Template with variables form and error message (msg).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        matr_nr = request.form["matr_nr"]
        name = request.form["name"]
        vorname = request.form["vorname"]
        semester = request.form["semester"]
        kurs = request.form["kurs"]
        msg = qf.insert_new_student(conn, matr_nr, name, vorname, semester, kurs)
        conn.commit()
        conn.close()
        return render_template('append_persons.html', form=form, msg=msg)
    return render_template('append_persons.html', form=form)




@app.route("/delete_persons/", methods=["GET", "POST"])
def delete_professor():
    """
    Loads a form to delete a professor.
    :return: renders a HTML-Template with variables form and error message (msg).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        persNr_prof = request.form["persNr_prof"]
        msg = qf.delete_professor(conn, persNr_prof)
        conn.commit()
        conn.close()
        return render_template('delete_persons.html', form=form, msg=msg)

    return render_template('delete_persons.html', form=form)


@app.route("/delete_assistant/", methods=["GET", "POST"])
def delete_assistant():
    """
    Loads a form to delete a assistant.
    :return: renders a HTML-Template with variables form and error message (msg).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        persNr_assist = request.form["persNr_assist"]
        msg = qf.delete_assistant(conn, persNr_assist)
        conn.commit()
        conn.close()
        return render_template('delete_persons.html', form=form, msg=msg)

    return render_template('delete_persons.html', form=form)


@app.route("/delete_student/", methods=["GET", "POST"])
def delete_student():
    """
    Loads a form to delete a student.
    :return: renders a HTML-Template with variables form and error message (msg).
    """
    form = ResultsForm()
    database = "administration_database.db"
    # create a database connection
    conn = qf.create_connection(database)
    if request.method == "POST":
        matr_nr = request.form["matr_nr"]
        msg = qf.delete_student(conn, matr_nr)
        conn.commit()
        conn.close()
        return render_template('delete_persons.html', form=form, msg=msg)
    return render_template('delete_persons.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

