import mysql.connector


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
