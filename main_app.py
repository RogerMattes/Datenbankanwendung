from query_functions import *



def main():
    #database = r"C:\sqlite\db\pythonsqlite.db"
    database = "administration_database.db"

    # create a database connection
    conn = create_connection(database)

    with conn:
        #print("1. Query task by priority:")
        #select_task_by_priority(conn, 1)

        #tables = ['Professoren']

        #for table in tables:
            #print('------{}-----'.format(table.upper()))
            #select_all_from_table(conn, table)
        print("############")
        #insert_new_student(conn, matr_nr=7143550, name="Mattes", vorname="Roger", semester=3, kurs="B")
        #insert_new_event(conn, 225, "test", 1, 2125)
        #insert_new_testresult(conn, 25403, 4052, 2125, 7)
        #insert_new_student_to_event(conn, 7143550, 5259)
        print("------------")
        #select_all_from_professors(conn)
        #print("#############")
        #select_all_from_assistants(conn)
        #print("#############")
        #select_all_from_students(conn)
        #print("#############")
        #select_all_from_events(conn)
        #get_person_by_name(conn, name='Jonas', vorname="")
        #get_person_by_number(conn, 24002)
        #get_event_by_person(conn, 2125)
        #get_event_listend_by_student(conn, 25403)

        #insert_new_testresult(conn, 25403, 5001, 2126, 1.5)
        #insert_new_student_to_event(conn, 25403, 4052)
if __name__ == '__main__':
    main()