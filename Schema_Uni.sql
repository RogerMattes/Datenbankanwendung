DROP TABLE hoeren;
DROP TABLE voraussetzen;
DROP TABLE pruefen;
DROP TABLE Veranstaltungen;
DROP TABLE Studenten;
DROP TABLE Assistenten;
DROP TABLE Professoren;

CREATE TABLE Studenten
       (MatrNr         INTEGER PRIMARY KEY,
        Name           VARCHAR(30) NOT NULL,
        Vorname        VARCHAR(30),
        Semester       INTEGER CHECK (Semester BETWEEN 1 and 10),
        Kurs           VARCHAR(10) NOT NULL);        

CREATE TABLE Professoren
       (PersNr         INTEGER PRIMARY KEY,
        Name           VARCHAR(30) NOT NULL,
        Vorname        VARCHAR(30),
        Rang           CHAR(2) CHECK (Rang IN ('W2', 'W3')),
        Gebaeude       CHAR(1),
        Raum           INTEGER);

CREATE TABLE Assistenten
       (PersNr         INTEGER PRIMARY KEY,
        Name           VARCHAR(30) NOT NULL,
        Vorname        VARCHAR(30),        
        Fachgebiet     VARCHAR(30),
        zugeordnet     INTEGER REFERENCES Professoren ON DELETE SET NULL);

CREATE TABLE Veranstaltungen
       (VstNr          INTEGER PRIMARY KEY,
        Titel          VARCHAR(30),
        SWS            INTEGER,
        gelesenVon     INTEGER REFERENCES Professoren ON DELETE SET NULL);

CREATE TABLE hoeren
       (MatrNr         INTEGER REFERENCES Studenten ON DELETE CASCADE,
        VstNr          INTEGER REFERENCES Veranstaltungen ON DELETE CASCADE,
        PRIMARY KEY    (MatrNr, VstNr));

CREATE TABLE voraussetzen
       (Vorgaenger     INTEGER REFERENCES Veranstaltungen ON DELETE CASCADE,
        Nachfolger     INTEGER REFERENCES Veranstaltungen ON DELETE CASCADE,
        PRIMARY KEY    (Vorgaenger, Nachfolger));

CREATE TABLE pruefen
       (MatrNr         INTEGER,
        VstNr          INTEGER,
        PersNr         INTEGER,
        Note           NUMERIC(2,1) CHECK (Note BETWEEN 1.0 AND 5.0),
        PRIMARY KEY    (MatrNr, VstNr),
        FOREIGN KEY(PersNr) REFERENCES Professoren(PersNr),
        FOREIGN KEY(MatrNr) REFERENCES Studenten(MatrNr) ON DELETE CASCADE,
        FOREIGN KEY(VstNr) REFERENCES Veranstaltungen(VstNr)
        FOREIGN KEY(MatrNr, VstNr) REFERENCES hoeren(MatrNr, VstNr));
