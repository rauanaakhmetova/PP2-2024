import csv
import psycopg2
from db import insert_data, query_data, delete_data, update_data, enter_data, upload_csv

conn = psycopg2.connect("postgres://pp2_db_test_user:lfFfLH7HjK2ivnEzcN1ZokpgdhFi3WEZ@dpg-cohofjtjm4es739ccgn0-a.oregon-postgres.render.com/pp2_db_test", sslmode='require')
cur = conn.cursor()




# enter_data()
# upload_csv('numbers.csv')
# enter_data()

delete_data(name='PP2')

query_data()