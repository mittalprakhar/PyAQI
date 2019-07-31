import mysql.connector
from time import sleep


def get_tables(cursor):
    table_list = []
    cursor.execute("SHOW TABLES;")
    result = cursor.fetchall()
    for i in result:
        table_list.append(i[0])
    return table_list


def get_columns(cursor, table):
    if table in get_tables(cursor):
        column_list = []
        query = "DESC " + table + ";"
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            column_list.append(i[0])
        return column_list
    else:
        return []


def add(cursor, table, data):
    if table in get_tables(cursor):
        query = "INSERT INTO " + table + " VALUES(" + "%s, " * (len(data) - 1) + "%s);"
        cursor.execute(query, data)
    else:
        return -1


def init(user='root', password='PyAQI@42', host='localhost', database='PyAQI'):
    db = mysql.connector.connect(user=user, password=password, host=host, database=database)
    return db, db.cursor()


def reset(dd, dg, user='root', password='PyAQI@42', host='localhost'):
    db = mysql.connector.connect(user=user, password=password, host=host)
    cursor = db.cursor()

    cursor.execute("DROP DATABASE IF EXISTS PyAQI;")
    db.commit()

    cursor.execute("CREATE DATABASE PyAQI;")

    cursor.execute("USE PyAQI;")
    db.commit()

    cursor.execute("CREATE TABLE Delhi(Year integer NOT NULL, Season varchar(7) NOT NULL, PM10_Min integer, PM10_Max integer, \
                   PM2_5_Min integer, PM2_5_Max integer, NO2_Min integer, NO2_Max integer, \
                   SO2_Min integer, SO2_Max integer, O3_Min integer, O3_Max integer, \
                   CO_Min decimal(3,1), CO_Max decimal(3,1), NH3_Min integer, NH3_Max integer, \
                   AQI_Min integer, AQI_Max integer, \
                   CONSTRAINT Valid CHECK (Year BETWEEN 1990 AND 2018 AND \
                   Season IN ('Summer', 'Monsoon', 'Winter', 'Spring') AND \
                   PM10_Min >= 0 AND PM10_Max >= PM10_Min AND PM2_5_Min >= 0 AND PM2_5_Max >= PM2_5_Min AND \
                   NO2_Min >= 0 AND NO2_Max >= NO2_Min AND SO2_Min >= 0 AND SO2_Max >= SO2_Min AND \
                   O3_Min >= 0 AND O3_Max >= O3_Min AND CO_Min >= 0 AND CO_Max >= CO_Min AND \
                   NH3_Min >= 0 AND NH3_Max >= NH3_Min AND AQI_Min >= 0 AND AQI_Max >= AQI_Min));")
    cursor.execute("CREATE TABLE Gurgaon(Year integer NOT NULL, Season varchar(7) NOT NULL, PM10_Min integer, PM10_Max integer, \
                    PM2_5_Min integer, PM2_5_Max integer, NO2_Min integer, NO2_Max integer, \
                    SO2_Min integer, SO2_Max integer, O3_Min integer, O3_Max integer, \
                    CO_Min decimal(3,1), CO_Max decimal(3,1), NH3_Min integer, NH3_Max integer, \
                    AQI_Min integer, AQI_Max integer, \
                    CONSTRAINT Valid CHECK (Year BETWEEN 1990 AND 2018 AND \
                    Season IN ('Summer', 'Monsoon', 'Winter', 'Spring') AND \
                    PM10_Min >= 0 AND PM10_Max >= PM10_Min AND PM2_5_Min >= 0 AND PM2_5_Max >= PM2_5_Min AND \
                    NO2_Min >= 0 AND NO2_Max >= NO2_Min AND SO2_Min >= 0 AND SO2_Max >= SO2_Min AND \
                    O3_Min >= 0 AND O3_Max >= O3_Min AND CO_Min >= 0 AND CO_Max >= CO_Min AND \
                    NH3_Min >= 0 AND NH3_Max >= NH3_Min AND AQI_Min >= 0 AND AQI_Max >= AQI_Min));")
    db.commit()

    for i in dd:
        add(cursor, "Delhi", i)
    db.commit()

    for i in dg:
        add(cursor, "Gurgaon", i)
    db.commit()

    return db, cursor


def home(admins):
    while True:
        print("\n", "-" * 30, sep="")
        print("\nWelcome to PyAQI")
        print("\nPyAQI is a Python script that can be used to access annual pollution data for Delhi and Gurgaon, \
        \nand predict the Air Quality Index for the two cities in the next 5 years.\n")

        while True:
            try:
                print("Choose login type: ")
                print("\t1. User")
                print("\t2. Admin")
                inp = input("\nEnter 1 or 2: ")
                inp = inp.lower()
                if inp not in ['1', '2', 'user', 'admin']:
                    print("\nInvalid input.\n")
                    sleep(1)
                else:
                    break
            except ValueError:
                print("\nInvalid input.\n")
                sleep(1)

        if inp in ['1', 'user']:
            break

        else:
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            success = False
            for i in admins:
                if username == i[0] and password == i[1]:
                    success = True
                    break
            if success:
                break
            else:
                print("\nIncorrect username or password.")
                sleep(1)

    if inp in ['1', 'user']:
        print("\nLogging in as user...")
        user(admins)

    else:
        print("\nLogging in as admin...")
        admin(admins)


def user(admins):
    print("\n", "-" * 30, sep="")
    print("\nUser Menu: \n")
    while True:
        try:
            print("Choose task: ")
            print("\t1. Access Data")
            print("\t2. See Trends")
            print("\t3. See Predictions")
            print("\t4. Information")
            print("\t5. Go Back")
            inp = input("\nEnter 1, 2, 3, 4 or 5: ")
            inp = inp.lower()
            if inp not in ['1', '2', '3', '4', '5', 'access', 'data', 'access data', 'trends', 'see trends',
                           'trend', 'see trend', 'predictions', 'prediction', 'see predictions', 'see prediction',
                           'info', 'information', 'see info', 'see information', 'back', 'go back']:
                print("\nInvalid input.\n")
                sleep(1)
            else:
                break
        except ValueError:
            print("\nInvalid input.\n")
            sleep(1)

    if inp in ['1', 'access', 'data', 'access data']:
        access(admins)
    elif inp in ['2', 'trends', 'see trends', 'trend', 'see trend']:
        trends(admins)
    elif inp in ['3',  'predictions', 'prediction', 'see predictions', 'see prediction']:
        predictions(admins)
    elif inp in ['4', 'info', 'information', 'see info', 'see information']:
        info(admins)
    else:
        home(admins)


def admin(admins):
    print("\n", "-" * 30, sep="")
    print("\nAdmin Menu: \n")
    while True:
        try:
            print("Choose task: ")
            print("\t1. Add Data")
            print("\t2. Modify Data")
            print("\t3. Delete Data")
            print("\t4. Log Out")
            inp = input("\nEnter 1, 2, 3 or 4: ")
            inp = inp.lower()
            if inp not in ['1', '2', '3', '4', 'add', 'add data', 'modify', 'modify data', 'delete', 'delete data'
                           'back', 'log out']:
                print("\nInvalid input.\n")
                sleep(1)
            else:
                break
        except ValueError:
            print("\nInvalid input.\n")
            sleep(1)

    if inp in ['1', 'add', 'add data']:
        admin_add(admins)
    elif inp in ['2', 'modify', 'modify data']:
        admin_modify(admins)
    elif inp in ['3', 'delete', 'delete data']:
        admin_delete(admins)
    elif inp in ['4', 'back', 'log out']:
        print("\nLogging out...")
        home(admins)


def access(admins):
    print("\n", "-" * 30, sep="")
    print("\nAccess Data\n")


def trends(admins):
    print("\n", "-" * 30, sep="")
    print("\nTrends\n")


def predictions(admins):
    print("\n", "-" * 30, sep="")
    print("\nPredictions\n")


def info(admins):
    print("\n", "-" * 30, sep="")
    print("\nInformation\n")


def admin_add(admins):
    print("\n", "-" * 30, sep="")
    print("\nAdd Data\n")


def admin_modify(admins):
    print("\n", "-" * 30, sep="")
    print("\nModify Data\n")


def admin_delete(admins):
    print("\n", "-" * 30, sep="")
    print("\nDelete Data\n")
