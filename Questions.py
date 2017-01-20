import random
import psycopg2
import Variables


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


def pick_number(type):
    if type == 'g':
        QuestionID = random.randint(1, 38)
    elif type == 'gr':
        QuestionID = random.randint(39, 60)
    elif type == 'r':
        QuestionID = random.randint(61, 89)
    elif type == 'b':
        QuestionID = random.randint(90, 119)
    else:
        QuestionID = random.randint(1, 119)
    return QuestionID


def question(number):
    return interact_database("SELECT Question FROM Questions WHERE Question_ID = %s", (number,))[0][0]


def possibilities(number):
    return interact_database("SELECT Possibilities FROM Questions WHERE Question_ID = %s", (number,))[0][0]


def answers(number):
    return interact_database("SELECT Answers FROM Questions WHERE Question_ID = %s", (number,))[0][0]


def begin():
    num = random.randint(1, 119)
    Variables.questionint = num
    print(question(num))
    print(possibilities(num))

# Copyright 2017 Sjors van Gelderen
