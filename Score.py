import psycopg2


def interact_database(command, upload, params=None):
    # indien nodig kunnen we van user en password variabelen maken die door de speler kunnen worden ingevoerd.
    # Standaard waardes: postgres, INF1HGroup4.
    connection = psycopg2.connect("dbname=INF1H_Project_2_Group_4 user=%s password=%s")(DBUser, SBPassword)
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

# als de score naam combinatie nog niet in de database staat wordt deze geupload
def upload_score(score, name):
    uploadcheck = interact_database("SELECT * FROM score WHERE Score = %s and Name = %s;", False, (score, name))
    if not uploadcheck:
        print('Upload succesful')
        interact_database("UPDATE Score SET Score = %s WHERE Name = %s);", True, (score, name))

# alle scores en namen in de database
def download_score():
    return interact_database("SELECT * FROM score ORDER BY score DESC;", False)

# hoogste score in de database
def download_highscore():
    return interact_database("SELECT MAX(Score) FROM score;", False)[0][0]

# score die op het scherm wordt weergegeven
def download_display_score():
    return interact_database("SELECT * FROM score ORDER BY score;", False)[0][1]

print(download_score())
print(download_highscore())
# Copyright 2017 Sjors van Gelderen
