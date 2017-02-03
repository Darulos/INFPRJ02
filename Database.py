# Copyright 'We gaan voor een 10', 2017

import psycopg2


def interact_database(command, params=None):
    connection = psycopg2.connect("dbname=INF1H_Project_2_Group_4 user=postgres password=M1ho1337@lice")
    cursor = connection.cursor()
    cursor.execute(command, params)
    connection.commit()

    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        print("Connection failure.")
        pass

    cursor.close()
    connection.close()

    return results

# Function to get the question from the database depending on the ID number
def question(number):
    return interact_database("SELECT Question FROM Questions WHERE Question_ID = %s", (number,))[0][0]

# Functions to get the possibilities from the database depending on the ID number, this also indicates which type of question
def possibilities1(number):
    return interact_database("SELECT Possibilities1 FROM Questions WHERE Question_ID = %s", (number,))[0][0]

def possibilities2(number):
    return interact_database("SELECT Possibilities2 FROM Questions WHERE Question_ID = %s", (number,))[0][0]

def possibilities3(number):
    return interact_database("SELECT Possibilities3 FROM Questions WHERE Question_ID = %s", (number,))[0][0]


def answers(number):
    return interact_database("SELECT Answers FROM Questions WHERE Question_ID = %s", (number,))[0][0]
