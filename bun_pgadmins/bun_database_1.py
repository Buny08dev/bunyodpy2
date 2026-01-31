from psycopg2 import Error,connect



def database_create_table(password_,table_name):
    try:
        connection=connect(user="postgres",
                           password=password_,
                           host="localhost",
                           port="5432",
                           database="bundatabase")
        cursor=connection.cursor()
        cursor.execute(f"""
                       create table {table_name}(
                       id serial primary key not null,
                       user_name varchar(30) not null,
                       age int not null
                       );""")
        connection.commit()
    except(Exception,Error) as error:
        print("xato", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("S t o p  w o r k e d")


def database_add_users():
    try:
        connection=connect(user="postgres",
                           password="bunyod",
                           host="localhost",
                           port="5432",
                           database="bundatabase")
        cursor=connection.cursor()
        cursor.execute(f"""
                       insert into users(user_name,age) values('bunyod',16);
                       """)
        connection.commit()
    except(Exception,Error) as error:
        print("xato", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("S t o p  w o r k e d")


def database_read_users():
    try:
        connection=connect(user="postgres",
                           password="bunyod",
                           host="localhost",
                           port="5432",
                           database="bundatabase")
        cursor=connection.cursor()
        cursor.execute(f"""
                       select * from users 
                       """)
        print(cursor.fetchall())
    except(Exception,Error) as error:
        print("xato", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("S t o p  w o r k e d")
database_read_users()