try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        print("Connection failure.")
        pass

def download_score():
    return interact_database("SELECT * FROM score")
    for i in interact_database("SELECT * FROM score"):
        x = ""
        if y[i] != '(' and y[i] != ')' and y[i] != '[' and y[i] != ']':
            x += y[i]
    return x


def download_highscore():
    return interact_database("SELECT * FROM score ORDER BY score DESC;")[0][1]

print(download_score())
print(download_highscore())

INSERT INTO Score(Name, Score)
VALUES('Jasper', 100),
('Daryl', 0),
('Xin', 69)
