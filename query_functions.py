import sqlite3
from sqlite3 import Error

import flask


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

    for row in rows:
        print(row)


def select_all_from_assistants(conn):
    """
    Selects all assistants from table with all information.
    :param conn: (list) the Connection object
    :return: (tuple) all assistants with whole information
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Assistenten")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_all_from_students(conn):
    """
    Selects all professors from table with all information.
    :param conn: (list) the Connection object
    :return: (tuple) all students with whole information
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Studenten")

    rows = cur.fetchall()

    for row in rows:
        print(row)


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

    for row in rows:
        print(row)


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
        cur.execute("""SELECT * FROM Assistenten
                    WHERE Assistenten.Name LIKE '{}'""".format(name))
        b = cur.fetchall()
        if b:
            print(b)
        cur.execute("""SELECT * FROM Studenten
                    WHERE Studenten.Name LIKE '{}'""".format(name))
        c = cur.fetchall()
        if c:
            print(c)
        if not a and not b and not c:
            print("Nachname existiert nicht!")

    else:
        cur.execute("""SELECT * FROM Professoren
                    WHERE Professoren.Name LIKE '{}' AND Professoren.Vorname LIKE '{}'
                    """.format(name, vorname))
        a = cur.fetchall()
        if a:
            print(a)
        cur.execute("""SELECT * FROM Assistenten
                    WHERE Assistenten.Name LIKE '{}' AND Assistenten.Vorname LIKE '{}'
                    """.format(name, vorname))
        b = cur.fetchall()
        if b:
            print(b)
        cur.execute("""SELECT * FROM Studenten
                WHERE Studenten.Name LIKE '{}' AND Studenten.Vorname LIKE '{}';
                """.format(name, vorname))
        c = cur.fetchall()
        if c:
            print(c)
        if not a and not b and not c:
            print("Nachname und/oder Vorname existieren nicht!")


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
        print("Diese Personal- bzw. Matrikelnummer existiert nicht!")
    elif a:
        cur.execute("""SELECT * FROM Professoren
                    WHERE Professoren.PersNr LIKE {}
                    """.format(number))
        a = cur.fetchall()
        print(a)
    elif b:
        cur.execute("""SELECT * FROM Assistenten
                    WHERE Assistenten.PersNr LIKE {}
                    """.format(number))
        b = cur.fetchall()
        print(b)
    elif c:
        cur.execute("""SELECT * FROM Studenten
            WHERE Studenten.MatrNr LIKE {}
            """.format(number))
        c = cur.fetchall()
        print(c)
    else:
        print("Keine Angaben zu dieser Person gefunden gefunden.")



def get_event_by_person(conn, number2):
    """
       Search event of person (professor, assistant or student) by his/her
       personnel-/ or matriculation number.
       :param number2: (int) personnel-/ or matriculation number
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
        print("Diese Personalnummer existiert nicht!")
    elif a:
        if int(a[0][0]) == int(number2):
            cur.execute("""SELECT * FROM Veranstaltungen
                    WHERE Veranstaltungen.gelesenVon LIKE {}
                    """.format(a[0][0]))
            a = cur.fetchall()
            print(a)
    elif b:
        if int(b[0][0]) == int(number2):
            cur.execute("""SELECT * FROM Veranstaltungen
                    WHERE Veranstaltungen.gelesenVon LIKE {}
                    """.format(b[0][4]))
            event = cur.fetchall()
            print(event)
    else:
        print("Keine Veranstaltungen zu dieser Person gefunden gefunden.")



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
        print("Matrikelnummer existiert nicht!")
    elif row[0][0]:
        cur.execute("""SELECT hoeren.MatrNr, Veranstaltungen.Titel, Veranstaltungen.SWS, Professoren.Name FROM hoeren
                    INNER JOIN Veranstaltungen on hoeren.VstNr = Veranstaltungen.VstNr
                    INNER JOIN Professoren on Veranstaltungen.gelesenVon = Professoren.PersNr
                    WHERE MatrNr LIKE '{}';
                    """.format(matr_nr))
    else:
        print("Student besucht keine Veranstaltung!")

    rows = cur.fetchall()
    for row in rows:
        print(row)


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
    #Kommentar Simon
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
        print("Matrikelnummer existiert nicht!")
    elif not b:
        print("Veranstaltungsnummer existiert nicht!")
    elif not c:
        print("Personalnummer existiert nicht oder ist nicht die eines Professors!")
    elif not d:
        print("Student ist nicht in der Veranstaltung eingeschrieben!")
    elif float(result) > 6.0:
        print("Ungültige Eingabe. Prüfungsergebnis muss <= 6.0 sein.")
    else:
        cur.execute("""INSERT OR REPLACE INTO pruefen(MatrNr, VstNr, PersNr, Note) 
                    VALUES ({}, {}, {}, {});
                  """.format(matr_nr, vst_nr, persNr_prof, result))
        print("Prüfungsergebnis erfolgreich eingetragen.")


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
        print("Matrikelnummer existiert nicht!")
    elif not b:
        print("Veranstaltungsnummer existiert nicht!")
    elif c[0][0] == 1:
        print("Student ist bereits in dieser Vorlesung eingeschrieben!")
    elif d:
        if note[0][0] == d[0][0]:
            print("Nicht möglich, da die Vorgänger-Veranstaltung nicht"
                  " erfolgreich absolviert wurde.")
    else:
        cur.execute("""INSERT INTO hoeren(MatrNr, VstNr)
                               VALUES ({}, {});
                  """.format(matr_nr, vst_nr))
        print("Student erfolgreich eingeschrieben.")


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
    print(a + b)

    if a:
        print("Veranstaltung existiert bereits!")
    elif not b:
        print("Personalnummer existiert nicht!")
    elif not c:
        print("Diese Vorgänger-Veranstaltung existiert nicht.")
    else:
        cur.execute("""INSERT INTO Veranstaltungen(VstNr, Titel, SWS, gelesenVon)
                            VALUES({}, '{}', {}, {})
                  """.format(vst_nr, title, sws, persNr_prof))
        print("Veranstaltung erfolgreich angelegt.")


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

    if str(rang) != "W2" or "W3":
        print("Ungültiger Rang!")
    elif row[0][0] == 0 and vorname == "":
        cur.execute("""INSERT INTO Professoren(PersNr, Name, Vorname, Rang, Gebaeude, Raum)
                        VALUES ({},'{}', NULL,'{}','{}', {});
                    """.format(pers_nr, name, rang, gebaeude, raum))
        print("Professor wurde erfolgreich angelegt.")
    elif row[0][0] == 0 and vorname != "":
        cur.execute("""INSERT INTO Professoren(PersNr, Name, Vorname, Rang, Gebaeude, Raum)
                        VALUES ({},'{}','{}','{}','{}', {});
                    """.format(pers_nr, name, vorname, rang, gebaeude, raum))
        print("Professor wurde erfolgreich angelegt.")
    else:
        print("Professor existiert bereits!")


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
        print("Assistent wurde erfolgreich angelegt.")

    elif row[0][0] == 0 and vorname != "":
        cur.execute("""INSERT INTO Assistenten(PersNr, Name, Vorname, Fachgebiet, zugeordnet)
                        VALUES ({},'{}','{}','{}',{});
                    """.format(pers_nr, name, vorname, fachgebiet, zugeordnet))
        print("Assistent wurde erfolgreich angelegt.")
    else:
        print("Assistent existiert bereits!")


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
        print("Student wurde erfolgreich angelegt.")
    elif row[0][0] == 0 and vorname != "":
        cur.execute("""INSERT INTO Studenten(MatrNr, Name, Vorname, Semester, Kurs)
                        VALUES ({},'{}','{}',{},'{}');""".format(matr_nr, name, vorname, semester, kurs))
        print("Student wurde erfolgreich angelegt.")
    else:
        print("Student existiert bereits!")


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
                    WHERE PersNr = {};
                    """.format(pers_nr))
        print("Professor wurde erfolgreich gelöscht.")
    else:
        print("Personalnummer existiert nicht!")


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
        print("Assistent wurde erfolgreich gelöscht.")
    else:
        print("Personalnummer existiert nicht!")


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
        print("Student wurde erfolgreich gelöscht.")
    else:
        print("Matrikelnummer existiert nicht!")
