import psycopg2
from config import host, user, password, db_name

try:
    #connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    
    #the cursor for perfoming database operations
    #cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")
    
    
    
    #create a new table
    # with connection.cursor() as cursor:
    #     # Удаление существующей таблицы (если она существует)
        # cursor.execute("DROP TABLE IF EXISTS users;")
        
        # # Создание новой таблицы
        # cursor.execute("""
        #     CREATE TABLE users (
        #         id serial PRIMARY KEY,
        #         name varchar(50) NOT NULL,
        #         phone_number varchar(50) NOT NULL
        #     )
        # """)
        # print(f"[INFO] Table created successfully")
        



    #ВВОД ДАННЫХ В ТАБЛИЦУ
    # insert data into a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (name, phone_number) VALUES
    #         ('Username_Ru', '87770182608'),
    #         ('RU_KULPUNAI', '77777777777'),
    #         ('Rauana', '87072589647');"""
    #     )
    #     print(f"[INFO] Data was succesfully inserted")



    #Получения данных с таблицы ПО ИМЕНИ
    #get data from a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT * FROM users WHERE name = 'Zhuma'"""
            
    #     )
    #     print(cursor.fetchone())

    #Получения данных с таблицы ПО ТЕЛЕФОНУ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT * FROM users WHERE name LIKE 'A%'"""
    #     )
    #     rows = cursor.fetchall()
    #     for row in rows:
    #         print(row)



    #ВЫВОД ВСЕХ ДАННЫХ В ТАБЛИЦ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT * FROM users WHERE phone_number = '%22%';"""
    #     )
    #     print(cursor.fetchone())
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)



    #delete a table(УДАЛИТЬ ВСЮ ТАБЛИЦУ)
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )
    #     print("[INFO] Table was deleted")

    # #УДАЛИТЬ ЗАПИСЬ ПО АЙДИ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM users WHERE id = '7'"""
            
    #     )
    # #УДАЛИТЬ ЗАПИСЬ ПО ИМЕНИ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM users WHERE name ='имя по которому нужно удалить' """  
    #     )
    # УДАЛИТЬ ЗАПИСЬ ПО НОМЕРУ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM users WHERE phone_number ='номер по которому нужно удалить'"""
            
    #     )

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM users WHERE phone_number ~ '[0-9]{2}';""" 
    #     )
    #ОБНОВИТЬ ИМЯ ПО НОМЕРУ ТЕЛЕФОНА
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """UPDATE users
    #         SET name = 'новое-имя' 
    #         WHERE phone_number = номер телефона """
            
    #     )
    # #ОБНОВИТЬ НОМЕР ТЕЛЕФОНА ПО ИМЕНИ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """UPDATE users
    #         SET phone_number = 'новый номер' 
    #         WHERE name = 'по имени'"""
            
    #     )
    # #ОБНОВИТЬ ИМЯ ПО АЙДИ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """UPDATE users
    #         SET id = 'новое имя' 
    #         WHERE name = по номеру"""
            
    #     )
    # #ОБНОВИТЬ НОМЕР ТЕЛЕФОНА ПО АЙДИ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """UPDATE users
    #         SET phone_number = 'новый-номер' 
    #         WHERE name = по имени"""
            
    #     )



except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")

