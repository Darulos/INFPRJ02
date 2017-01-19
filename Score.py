import psycopg2


def interact_database(command, upload, params=None):
    # Voer achter user uw postgres inlognaam in, voer achter password uw postgres password in.
    connection = psycopg2.connect("dbname=INF1H_Project_2_Group_4 user=postgres password=INF1HGroup4")
    cursor = connection.cursor()

    cursor.execute(command, params)
    connection.commit()

    results = None

    if upload is False:
        try:
            results = cursor.fetchall()
        except psycopg2.ProgrammingError:
            print("Connection failure.")
            pass

    cursor.close()
    connection.close()

    return results


def upload_score(score, name):
    uploadcheck = interact_database("SELECT * FROM score WHERE Score = %s and Name = %s;", False, (score, name))
    if uploadcheck:
        print('Upload succesful')
        interact_database("UPDATE Score SET Score = %s WHERE Name = %s;", True, (score + 10, name))

# alle scores en namen in de database
def download_score():
    return interact_database("SELECT * FROM score ORDER BY score DESC;", False)

# hoogste score in de database
def download_highscore():
    return interact_database("SELECT MAX(Score) FROM score;", False)[0][0]

# score die op het scherm wordt weergegeven
def download_display_score():
    return interact_database("SELECT * FROM score WHERE Score = %s and Name = %s;", False, (score, name))[0][1]


# Copyright 2017 Sjors van Gelderen
