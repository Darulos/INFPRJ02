import psycopg2


def interact_database(command, upload, params=None):
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
    if not uploadcheck:
        print('je moeder')
        interact_database("INSERT INTO Score(Name, Score) VALUES (%s, %s);", True, (name, score))


def download_score():
    return interact_database("SELECT * FROM score ORDER BY score DESC;", False)


def download_highscore():
    return interact_database("SELECT Name, MAX(Score) FROM score GROUP BY Name;", False)

print(download_score())
print(download_highscore())
# Copyright 2017 Sjors van Gelderen
