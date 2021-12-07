import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file.
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_from_professors(conn):
    """
    Selects all professors from table with all information.
    :param conn: (list) the Connection object
    :return: (tuple) all professors with whole information
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Professoren")

    rows = cur.fetchall()
    print(rows)
    return rows


def select_all_from_assistants(conn):
    """
    Selects all assistants from table with all information.
    :param conn: (list) the Connection object
    :return: (tuple) all assistants with whole information
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Assistenten")

    rows = cur.fetchall()
    print(rows)
    return rows


def select_all_from_students(conn):
    """
    Selects all professors from table with all information.
    :param conn: (list) the Connection object
    :return: (tuple) all students with whole information
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Studenten")

    rows = cur.fetchall()
    print(rows)
    return rows


def select_all_from_events(conn):
    """
    Selects all events from table with all information.
    :param conn: (list) the Connection object
    :return: (tuple) all events with whole information
    """
    cur = conn.cursor()
    cur.execute("""SELECT VstNR, Titel, SWS, Professoren.Name  FROM Veranstaltungen
                    INNER JOIN Professoren on Professoren.PersNr = Veranstaltungen.gelesenVon;
        """)
    rows = cur.fetchall()
    print(rows)
    return rows


def get_person_by_name(conn, name, vorname):
    """
       Search person (professor, assistant or student) by his/her name.
       :param vorname: (str) first name of the person
       :param name: (str) last name of the person
       :param conn: (list) the Connection object
       :return: (tuple)  data record of the person
    """

    cur = conn.cursor()
    if vorname == "":
        cur.execute("""SELECT * FROM Professoren
                    WHERE Professoren.Name LIKE '{}'""".format(name))
        a = cur.fetchall()
        if a:
            print(a)
            return a
        cur.execute("""SELECT * FROM Assistenten
                    WHERE Assistenten.Name LIKE '{}'""".format(name))
        b = cur.fetchall()
        if b:
            print(b)
            return b
        cur.execute("""SELECT * FROM Studenten
                    WHERE Studenten.Name LIKE '{}'""".format(name))
        c = cur.fetchall()
        if c:
            print(c)
            return c
        if not a and not b and not c:
            error = "Nachname existiert nicht!"
            print(error)
            return error
    else:
        cur.execute("""SELECT * FROM Professoren
                    WHERE Professoren.Name LIKE '{}' AND Professoren.Vorname LIKE '{}'
                    """.format(name, vorname))
        a = cur.fetchall()
        if a:
            print(a)
            return a
        cur.execute("""SELECT * FROM Assistenten
                    WHERE Assistenten.Name LIKE '{}' AND Assistenten.Vorname LIKE '{}'
                    """.format(name, vorname))
        b = cur.fetchall()
        if b:
            print(b)
            return b
        cur.execute("""SELECT * FROM Studenten
                WHERE Studenten.Name LIKE '{}' AND Studenten.Vorname LIKE '{}';
                """.format(name, vorname))
        c = cur.fetchall()
        if c:
            print(c)
            return c
        if not a and not b and not c:
            error = "Nachname und/oder Vorname existieren nicht!"
            print(error)
            return error


def get_person_by_number(conn, number):
    """
       Search person (professor, assistant or student) by his/her
       personnel-/ or matriculation number.
       :param number: (int) personnel-/ or matriculation number
       :param conn: (list) the Connection object
       :return: (tuple) data record of the person
    """
    cur = conn.cursor()
    cur.execute("""SELECT * FROM Professoren
                WHERE Professoren.PersNr LIKE {}""".format(number))
    a = cur.fetchall()

    cur.execute("""SELECT * FROM Assistenten
                WHERE Assistenten.PersNr LIKE {}""".format(number))
    b = cur.fetchall()

    cur.execute("""SELECT * FROM Studenten
                WHERE Studenten.MatrNr LIKE {};
            """.format(number))
    c = cur.fetchall()

    if not a and not b and not c:
        error = "Diese Personal- bzw. Matrikelnummer existiert nicht!"
        print(error)
        return error
    elif a:
        cur.execute("""SELECT * FROM Professoren
                    WHERE Professoren.PersNr LIKE {}
                    """.format(number))
        a = cur.fetchall()
        print(a)
        return a
    elif b:
        cur.execute("""SELECT * FROM Assistenten
                    WHERE Assistenten.PersNr LIKE {}
                    """.format(number))
        b = cur.fetchall()
        print(b)
        return b
    elif c:
        cur.execute("""SELECT * FROM Studenten
            WHERE Studenten.MatrNr LIKE {}
            """.format(number))
        c = cur.fetchall()
        print(c)
        return c
    else:
        result = "Keine Angaben zu dieser Person gefunden gefunden."
        print(result)
        return result



def get_event_by_person(conn, number2):
    """
       Search for event/-s of a person (professor or assistant ) by his/her
       personnel number.
       :param number2: (int) personnel number
       :param conn: (str) the Connection object
       :return: (tuple) data record of events from the person
    """
    cur = conn.cursor()
    cur.execute("""SELECT PersNr FROM Professoren
                        WHERE Professoren.PersNr LIKE {}
                        """.format(number2))
    a = cur.fetchall()
    cur.execute("""SELECT * FROM Assistenten
                        WHERE Assistenten.PersNr LIKE {}
                        """.format(number2))
    b = cur.fetchall()
    if not a and not b:
        error = "Diese Personalnummer existiert nicht!"
        print(error)
        return error
    elif a:
        if int(a[0][0]) == int(number2):
            cur.execute("""SELECT * FROM Veranstaltungen
                    WHERE Veranstaltungen.gelesenVon LIKE {}
                    """.format(a[0][0]))
            rows = cur.fetchall()
            print(rows)
            return rows
    elif b:
        if int(b[0][0]) == int(number2):
            cur.execute("""SELECT * FROM Veranstaltungen
                    WHERE Veranstaltungen.gelesenVon LIKE {}
                    """.format(b[0][4]))
            rows = cur.fetchall()
            print(rows)
            return rows
    else:
        error = "Keine Veranstaltungen zu dieser Person gefunden gefunden."
        print(error)
        return error



def get_event_listend_by_student(conn, matr_nr):
    """
       Search all events that the student is listening to by his/her
       matriculation number.
       :param matr_nr: (int) matriculation number of the student
       :param conn: (list) the Connection object
       :return: (tuple) all events that the student listens to
    """
    cur = conn.cursor()
    cur.execute("""SELECT EXISTS(SELECT hoeren.MatrNr FROM hoeren 
                                    WHERE 
                                    hoeren.MatrNr LIKE '{}'); """.format(matr_nr))

    row = cur.fetchall()

    cur.execute("""SELECT MatrNr FROM Studenten
                            WHERE 
                            Studenten.MatrNr = {} ;
                            """.format(matr_nr))
    a = cur.fetchall()
    if not a:
        error = "Matrikelnummer existiert nicht!"
        print(error)
        return error
    elif row[0][0]:
        cur.execute("""SELECT hoeren.MatrNr, Veranstaltungen.Titel, Veranstaltungen.SWS, Professoren.Name FROM hoeren
                    INNER JOIN Veranstaltungen on hoeren.VstNr = Veranstaltungen.VstNr
                    INNER JOIN Professoren on Veranstaltungen.gelesenVon = Professoren.PersNr
                    WHERE MatrNr LIKE '{}';
                    """.format(matr_nr))
        a = cur.fetchall()
        print(a)
        return a
    else:
        error = "Student besucht keine Veranstaltung!"
        print(error)
        return error




def insert_new_testresult(conn, matr_nr, vst_nr, persNr_prof, result):
    """
       Inserts new test result to database.
       :param result: (float) result of test
       :param persNr_prof: (int) personnel number of professor
       :param vst_nr: (int) event number
       :param matr_nr: (int) matriculation number of student
       :param conn: (list) the Connection object
       :return: new data record of testresult
    """

    cur = conn.cursor()
    cur.execute("""SELECT MatrNr FROM Studenten
                        WHERE 
                        Studenten.MatrNr = {} ;
                        """.format(matr_nr))
    a = cur.fetchall()

    cur.execute("""SELECT VstNr FROM Veranstaltungen
                        WHERE 
                        Veranstaltungen.VstNr = {};
                        """.format(vst_nr))
    b = cur.fetchall()

    cur.execute("""SELECT PersNr FROM Professoren
                    WHERE 
                    Professoren.PersNr = {};""".format(persNr_prof))
    c = cur.fetchall()

    cur.execute("""SELECT EXISTS(SELECT hoeren.MatrNr,hoeren.VstNr FROM hoeren
                            WHERE 
                            hoeren.MatrNr = {} AND hoeren.VstNr = {});
                """.format(matr_nr, vst_nr))
    d = cur.fetchall()

    if not a:
        error = "Matrikelnummer existiert nicht!"
        print(error)
        return error
    elif not b:
        error = "Veranstaltungsnummer existiert nicht!"
        print(error)
        return error
    elif not c:
        error = "Personalnummer existiert nicht oder ist nicht die eines Professors!"
        print(error)
        return error
    elif not d:
        error = "Student ist nicht in der Veranstaltung eingeschrieben!"
        print(error)
        return error
    elif float(result) > 6.0:
        error = "Ungültige Eingabe. Prüfungsergebnis muss <= 6.0 sein."
        print(error)
        return error
    else:
        cur.execute("""INSERT OR REPLACE INTO pruefen(MatrNr, VstNr, PersNr, Note) 
                    VALUES ({}, {}, {}, {});
                  """.format(matr_nr, vst_nr, persNr_prof, result))
        success = "Prüfungsergebnis erfolgreich eingetragen."
        print(success)
        return success


def insert_new_student_to_event(conn, matr_nr, vst_nr):
    """
       Inserts new student to event.
       :param vst_nr: (int) event number
       :param matr_nr: (int) matriculation number of student
       :param conn: (list) the Connection object
       :return: appends student to event
    """
    cur = conn.cursor()
    cur.execute("""SELECT MatrNr FROM Studenten
                    WHERE 
                    Studenten.MatrNr = {} ;
                    """.format(matr_nr))
    a = cur.fetchall()

    cur.execute("""SELECT VstNr FROM Veranstaltungen
                    WHERE 
                    Veranstaltungen.VstNr = {};
                    """.format(vst_nr))
    b = cur.fetchall()
    cur.execute("""SELECT EXISTS(SELECT hoeren.MatrNr,hoeren.VstNr FROM hoeren
                        WHERE 
                        hoeren.MatrNr = {} AND hoeren.VstNr = {});
            """.format(matr_nr, vst_nr))
    c = cur.fetchall()

    cur.execute("""SELECT * FROM voraussetzen
                    WHERE voraussetzen.Nachfolger = {}
                    """.format(vst_nr))
    d = cur.fetchall()
    cur.execute("""SELECT VstNr FROM pruefen
                WHERE Note > 4.0""")
    note = cur.fetchall()
    if not a:
        error = "Matrikelnummer existiert nicht!"
        print(error)
        return error
    elif not b:
        error = "Veranstaltungsnummer existiert nicht!"
        print(error)
        return error
    elif c[0][0] == 1:
        error = "Student ist bereits in dieser Vorlesung eingeschrieben!"
        print(error)
        return error
    elif d:
        if note[0][0] == d[0][0]:
            error = "Nicht möglich, da die Vorgänger-Veranstaltung nicht erfolgreich absolviert wurde."
            print(error)
            return error
    else:
        cur.execute("""INSERT INTO hoeren(MatrNr, VstNr)
                               VALUES ({}, {});
                  """.format(matr_nr, vst_nr))
        success = "Student erfolgreich eingeschrieben."
        print(success)
        return success


def insert_new_event(conn, vst_nr, title, sws, persNr_prof, pre_event):
    """
       Inserts new event to database.
       :param persNr_prof:(int) personnel number of professor
       :param sws:(int) hours per week in semester
       :param title:(str) title of event
       :param vst_nr: (int) event number
       :param conn: (list) the Connection object
       :return: new data record of event
    """
    cur = conn.cursor()
    cur.execute("""SELECT * FROM Veranstaltungen 
                    WHERE 
                    Veranstaltungen.VstNr LIKE {} 
            """.format(vst_nr))

    a = cur.fetchall()

    cur.execute("""SELECT * FROM Professoren 
                    WHERE Professoren.PersNr LIKE {};
                """.format(persNr_prof))
    b = cur.fetchall()

    cur.execute("""SELECT Vorgaenger FROM voraussetzen
                WHERE Vorgaenger = {}""".format(pre_event))
    c = cur.fetchall()

    if a:
        error = "Veranstaltung existiert bereits!"
        print(error)
        return error
    elif not b:
        error = "Personalnummer existiert nicht!"
        print(error)
        return error
    elif not c:
        error = "Diese Vorgänger-Veranstaltung existiert nicht."
        print(error)
        return error
    else:
        cur.execute("""INSERT INTO Veranstaltungen(VstNr, Titel, SWS, gelesenVon)
                            VALUES({}, '{}', {}, {})
                  """.format(vst_nr, title, sws, persNr_prof))
        success = "Veranstaltung erfolgreich angelegt."
        print(success)
        return success


def insert_new_professor(conn, pers_nr, name, vorname, rang, gebaeude, raum):
    """
       Inserts new professor to database.
       :param raum: (int) room of event
       :param gebaeude: (str) building in which the event room is
       :param rang: (str)rank
       :param vorname: (str) first name of professor
       :param name: (str) last name of professor
       :param pers_nr: (int) personnel number of professor
       :param conn: (list) the Connection object
       :return: new data record of professor
       """
    cur = conn.cursor()
    cur.execute("""SELECT EXISTS(SELECT PersNr FROM Professoren
                WHERE PersNr = {});
            """.format(pers_nr))

    row = cur.fetchall()

    if rang != "W2":
        if rang != "W3":
            error = "Ungültiger Rang!"
            print(error)
            return error
    elif row[0][0] == 0 and vorname == "":
        cur.execute("""INSERT INTO Professoren(PersNr, Name, Vorname, Rang, Gebaeude, Raum)
                        VALUES ({},'{}', NULL,'{}','{}', {});
                    """.format(pers_nr, name, rang, gebaeude, raum))
        success = "Professor wurde erfolgreich angelegt."
        print(success)
        return success
    elif row[0][0] == 0 and vorname != "":
        cur.execute("""INSERT INTO Professoren(PersNr, Name, Vorname, Rang, Gebaeude, Raum)
                        VALUES ({},'{}','{}','{}','{}', {});
                    """.format(pers_nr, name, vorname, rang, gebaeude, raum))
        success = "Professor wurde erfolgreich angelegt."
        print(success)
        return success
    else:
        error = "Professor existiert bereits!"
        print(error)
        return error


def insert_new_assistant(conn, pers_nr, name, vorname, fachgebiet, zugeordnet):
    """
       Inserts new assistant to database.
       :param zugeordnet: (int) personnel number of professor, that assistant is dedicated
       :param fachgebiet: (str) area of expertise
       :param vorname: (str) first name of assistant
       :param name: (str) last name of assistant
       :param pers_nr: (int) personnel number of assistant
       :param conn: (list) the Connection object
       :return: new data record of assistant
       """
    cur = conn.cursor()
    cur.execute("""SELECT EXISTS(SELECT PersNr FROM Assistenten
                WHERE PersNr = {});
            """.format(pers_nr))

    row = cur.fetchall()
    if row[0][0] == 0 and vorname == "":
        cur.execute("""INSERT INTO Assistenten(PersNr, Name, Vorname, Fachgebiet, zugeordnet)
                        VALUES ({},'{}', NULL, '{}',{});
                    """.format(pers_nr, name, fachgebiet, zugeordnet))
        success = "Assistent wurde erfolgreich angelegt."
        print(success)
        return success

    elif row[0][0] == 0 and vorname != "":
        cur.execute("""INSERT INTO Assistenten(PersNr, Name, Vorname, Fachgebiet, zugeordnet)
                        VALUES ({},'{}','{}','{}',{});
                    """.format(pers_nr, name, vorname, fachgebiet, zugeordnet))
        success = "Assistent wurde erfolgreich angelegt."
        print(success)
        return success
    else:
        error = "Assistent existiert bereits!"
        print(error)
        return error


def insert_new_student(conn, matr_nr, name, vorname, semester, kurs):
    """
       Inserts new student to database.
       :param kurs: course of student
       :param semester: semester that student is arranged to
       :param vorname: first name of student
       :param name: (str)last name of student
       :param matr_nr: (int) matriculation number of student
       :param conn: (list) the Connection object
       :return: new data record of student
       """
    cur = conn.cursor()
    cur.execute("""SELECT EXISTS(SELECT MatrNr FROM Studenten
                WHERE MatrNr = {});
            """.format(matr_nr))

    row = cur.fetchall()
    if row[0][0] == 0 and vorname == "":
        cur.execute("""INSERT INTO Studenten(MatrNr, Name, Vorname, Semester, Kurs)
                                VALUES ({},'{}', NULL ,{},'{}');""".format(matr_nr, name, semester, kurs))
        success = "Student wurde erfolgreich angelegt."
        print(success)
        return success
    elif row[0][0] == 0 and vorname != "":
        cur.execute("""INSERT INTO Studenten(MatrNr, Name, Vorname, Semester, Kurs)
                        VALUES ({},'{}','{}',{},'{}');""".format(matr_nr, name, vorname, semester, kurs))
        success = "Student wurde erfolgreich angelegt."
        print(success)
        return success
    else:
        error = "Student existiert bereits!"
        print(error)
        return error


def delete_professor(conn, pers_nr):
    """
       Deletes professor from database.
       :param pers_nr: (int) personnel number of professor
       :param conn: (list) the Connection object
       """
    cur = conn.cursor()
    cur.execute("""SELECT EXISTS(SELECT PersNr FROM Professoren
                WHERE PersNr = {});
            """.format(pers_nr))

    row = cur.fetchall()

    if row[0][0]:
        cur.execute("""DELETE FROM Professoren                 
                    WHERE PersNr = {};""".format(pers_nr))
        success = "Professor wurde erfolgreich gelöscht."
        print(success)
        return success
    else:
        error = "Personalnummer existiert nicht!"
        print(error)
        return error


def delete_assistant(conn, pers_nr):
    """
       Deletes assistant from database.
       :param pers_nr: (int) personnel number of assitant
       :param conn: (list) the Connection object
       """
    cur = conn.cursor()
    cur.execute("""SELECT EXISTS(SELECT PersNr FROM Assistenten
                WHERE PersNr = {});
            """.format(pers_nr))

    row = cur.fetchall()

    if row[0][0]:
        cur.execute("""DELETE FROM Assistenten                 
                    WHERE PersNr = {};
                    """.format(pers_nr))
        success = "Assistent wurde erfolgreich gelöscht."
        print(success)
        return success
    else:
        error = "Personalnummer existiert nicht!"
        print(error)
        return error


def delete_student(conn, matr_nr):
    """
       Deletes student from database.
       :param matr_nr: (int) matriculation number of student
       :param conn: (list) the Connection object
       """
    cur = conn.cursor()
    cur.execute("""SELECT EXISTS(SELECT MatrNr FROM Studenten
                WHERE MatrNr = {});""".format(matr_nr))

    row = cur.fetchall()

    if row[0][0]:
        cur.execute("""DELETE FROM Studenten                 
                    WHERE MatrNr = {};""".format(matr_nr))
        cur.execute("""DELETE FROM hoeren                 
                            WHERE MatrNr = {};""".format(matr_nr))
        cur.execute("""DELETE FROM pruefen                 
                                    WHERE MatrNr = {};""".format(matr_nr))
        success = "Student wurde erfolgreich gelöscht."
        print(success)
        return success
    else:
        error = "Matrikelnummer existiert nicht!"
        print(error)
        return error
