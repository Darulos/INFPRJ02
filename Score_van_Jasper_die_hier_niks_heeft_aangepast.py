import psycopg2
import Variables

# communicatie met de database
def interact_database(command, upload, params=None):
    # Voer achter user uw postgres inlognaam in, voer achter password uw postgres password in.
    connection = psycopg2.connect("dbname=INF1H_Project_2_Group_4 user=postgres password=a")
    cursor = connection.cursor()

    cursor.execute(command, params)
    connection.commit()

    results = None

    # als deze niet wordt gebruikt of upload True is bij een UPDATE command krijg je een error. HOU DIT ERIN.
    if upload is False:
        try:
            results = cursor.fetchall()
        except psycopg2.ProgrammingError:
            print("Connection failure.")
            pass

    cursor.close()
    connection.close()

    return results


# upload de score als je naam bestaat
def upload_score(score, name):
    interact_database("UPDATE Score SET Score = %s WHERE Name = %s;", True, (score, name))


# score van de huidige speler
def download_currentscore():
    return Variables.PlayerScore


# Copyright 2017 "We gaan voor een 10"
