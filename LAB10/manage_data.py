import psycopg2

conn = psycopg2.connect("postgres://snake_pp2_stats_user:TvG6D7Dw4osz3HV4AMAI8IBva5mCb98N@dpg-cohp3fn79t8c7385l7j0-a.oregon-postgres.render.com/snake_pp2_stats", sslmode='require')
cur = conn.cursor()


def get_all_data():
    cur.execute("SELECT * FROM snakegame ORDER BY user_score DESC")
    rows = cur.fetchall()
    for row in rows:
        print(f"Username = {row[0]} Score = {row[1]} Level = {row[2]}")

get_all_data()
