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
    if table in get_tables(cursor) and len(data) == len(get_columns(cursor, table)):
        query = "INSERT INTO " + table + " VALUES(" + "%s, " * (len(data) - 1) + "%s);"
        cursor.execute(query, data)
    else:
        print("Add Error")


def calc(inp):
    j = [inp[0], inp[1]]
    for i in range(2, 4):
        if inp[i] in range(0, 101):
            j.append(int(inp[i]))
        elif inp[i] in range(101, 251):
            j.append(int(100 + ((inp[i] - 100) * (100 / 150))))
        elif inp[i] in range(251, 351):
            j.append(int(200 + ((inp[i] - 250) * (100 / 100))))
        elif inp[i] in range(351, 431):
            j.append(int(300 + ((inp[i] - 350) * (100 / 80))))
        else:
            j.append(int(400 + ((inp[i] - 430) * (100 / 100))))
    for i in range(4, 6):
        if inp[i] in range(0, 31):
            j.append(int(0 + ((inp[i] - 0) * (50 / 30))))
        elif inp[i] in range(31, 61):
            j.append(int(50 + ((inp[i] - 30) * (50 / 30))))
        elif inp[i] in range(61, 91):
            j.append(int(100 + ((inp[i] - 60) * (100 / 30))))
        elif inp[i] in range(91, 121):
            j.append(int(200 + ((inp[i] - 90) * (100 / 30))))
        elif inp[i] in range(121, 251):
            j.append(int(300 + ((inp[i] - 120) * (100 / 130))))
        else:
            j.append(int(400 + ((inp[i] - 250) * (100 / 130))))
    for i in range(6, 8):
        if inp[i] in range(0, 41):
            j.append(int(0 + ((inp[i] - 0) * (50 / 40))))
        elif inp[i] in range(41, 81):
            j.append(int(50 + ((inp[i] - 40) * (50 / 40))))
        elif inp[i] in range(81, 181):
            j.append(int(100 + ((inp[i] - 80) * (100 / 100))))
        elif inp[i] in range(181, 281):
            j.append(int(200 + ((inp[i] - 180) * (100 / 100))))
        elif inp[i] in range(281, 401):
            j.append(int(300 + ((inp[i] - 280) * (100 / 120))))
        else:
            j.append(int(400 + ((inp[i] - 400) * (100 / 120))))
    for i in range(8, 10):
        if inp[i] in range(0, 41):
            j.append(int(0 + ((inp[i] - 0) * (50 / 40))))
        elif inp[i] in range(41, 81):
            j.append(int(50 + ((inp[i] - 40) * (50 / 40))))
        elif inp[i] in range(81, 381):
            j.append(int(100 + ((inp[i] - 80) * (100 / 300))))
        elif inp[i] in range(381, 801):
            j.append(int(200 + ((inp[i] - 380) * (100 / 420))))
        elif inp[i] in range(801, 1601):
            j.append(int(300 + ((inp[i] - 800) * (100 / 800))))
        else:
            j.append(int(400 + ((inp[i] - 1600) * (100 / 800))))
    for i in range(10, 12):
        if inp[i] in range(0, 51):
            j.append(int(0 + ((inp[i] - 0) * (50 / 50))))
        elif inp[i] in range(51, 101):
            j.append(int(50 + ((inp[i] - 50) * (50 / 50))))
        elif inp[i] in range(101, 169):
            j.append(int(100 + ((inp[i] - 100) * (100 / 68))))
        elif inp[i] in range(169, 209):
            j.append(int(200 + ((inp[i] - 168) * (100 / 40))))
        elif inp[i] in range(209, 749):
            j.append(int(300 + ((inp[i] - 208) * (100 / 540))))
        else:
            j.append(int(400 + ((inp[i] - 748) * (100 / 540))))
    for i in range(12, 14):
        if 0 <= inp[i] < 1.1:
            j.append(int(0 + ((inp[i] - 0) * (50 / 1))))
        elif 1.1 <= inp[i] < 2.1:
            j.append(int(50 + ((inp[i] - 1.1) * (50 / 1))))
        elif 2.1 <= inp[i] < 10:
            j.append(int(100 + ((inp[i] - 2.1) * (100 / 8))))
        elif 10 <= inp[i] < 17:
            j.append(int(200 + ((inp[i] - 10) * (100 / 7))))
        elif 17 <= inp[i] < 34:
            j.append(int(300 + ((inp[i] - 17) * (100 / 17))))
        else:
            j.append(int(400 + ((inp[i] - 34) * (100 / 17))))
    for i in range(14, 16):
        if inp[i] in range(0, 201):
            j.append(int(0 + ((inp[i] - 0) * (50 / 200))))
        elif inp[i] in range(201, 401):
            j.append(int(50 + ((inp[i] - 200) * (50 / 200))))
        elif inp[i] in range(401, 801):
            j.append(int(100 + ((inp[i] - 400) * (100 / 400))))
        elif inp[i] in range(801, 1201):
            j.append(int(200 + ((inp[i] - 800) * (100 / 400))))
        elif inp[i] in range(1201, 1801):
            j.append(int(300 + ((inp[i] - 1200) * (100 / 600))))
        else:
            j.append(int(400 + ((inp[i] - 1800) * (100 / 600))))
    low = max([j[2], j[4], j[6], j[8], j[10], j[12], j[14]])
    high = max([j[3], j[5], j[7], j[9], j[11], j[13], j[15]])
    if j[1] == "Spring":
        k = 0.9
    elif j[1] == "Summer":
        k = 0.8
    elif j[1] == "Monsoon":
        k = 0.7
    else:
        k = 0.65
    avg = int((low * k) + (high * (1-k)))
    if avg in range(0, 51):
        category = "Good"
    elif avg in range(51, 101):
        category = "Satisfactory"
    elif avg in range(101, 201):
        category = "Moderately Polluted"
    elif avg in range(201, 301):
        category = "Poor"
    elif avg in range(301, 401):
        category = "Very Poor"
    else:
        category = "Severe"
    j += [low, high, avg, category]
    return j


def init(user='root', password='PyAQI@42', host='localhost', database='PyAQI'):
    db = mysql.connector.connect(user=user, password=password, host=host, database=database)
    return db, db.cursor()


def reset(dd, dg, da, user='root', password='PyAQI@42', host='localhost'):
    db = mysql.connector.connect(user=user, password=password, host=host)
    cursor = db.cursor()

    cursor.execute("DROP DATABASE IF EXISTS PyAQI;")
    db.commit()

    cursor.execute("CREATE DATABASE PyAQI;")

    cursor.execute("USE PyAQI;")
    db.commit()

    cursor.execute("CREATE TABLE Chart(S_No integer, Category varchar(25) PRIMARY KEY NOT NULL, AQI_Min integer, \
                    AQI_RH integer, Description varchar(200));")

    cursor.execute("CREATE TABLE Delhi_Raw(Year integer NOT NULL, Season varchar(7) NOT NULL, \
                    PM10_RL integer, PM10_RH integer, PM2_5_RL integer, PM2_5_RH integer, \
                    NO2_RL integer, NO2_RH integer, SO2_RL integer, SO2_RH integer, \
                    O3_RL integer, O3_RH integer, CO_RL decimal(3,1), CO_RH decimal(3,1), \
                    NH3_RL integer, NH3_RH integer, \
                    CONSTRAINT Valid CHECK (Year BETWEEN 1990 AND 2018 AND \
                    Season IN ('Summer', 'Monsoon', 'Winter', 'Spring') AND \
                    PM10_RL >= 0 AND PM10_RH >= PM10_RL AND PM2_5_RL >= 0 AND PM2_5_RH >= PM2_5_RL AND \
                    NO2_RL >= 0 AND NO2_RH >= NO2_RL AND SO2_RL >= 0 AND SO2_RH >= SO2_RL AND \
                    O3_RL >= 0 AND O3_RH >= O3_RL AND CO_RL >= 0 AND CO_RH >= CO_RL AND \
                    NH3_RL >= 0 AND NH3_RH >= NH3_RL), CONSTRAINT PK_DR PRIMARY KEY (Year, Season));")

    cursor.execute("CREATE TABLE Gurgaon_Raw(Year integer NOT NULL, Season varchar(7) NOT NULL, \
                    PM10_RL integer, PM10_RH integer, PM2_5_RL integer, PM2_5_RH integer, \
                    NO2_RL integer, NO2_RH integer, SO2_RL integer, SO2_RH integer, \
                    O3_RL integer, O3_RH integer, CO_RL decimal(3,1), CO_RH decimal(3,1), \
                    NH3_RL integer, NH3_RH integer, \
                    CONSTRAINT Valid CHECK (Year BETWEEN 1990 AND 2018 AND \
                    Season IN ('Summer', 'Monsoon', 'Winter', 'Spring') AND \
                    PM10_RL >= 0 AND PM10_RH >= PM10_RL AND PM2_5_RL >= 0 AND PM2_5_RH >= PM2_5_RL AND \
                    NO2_RL >= 0 AND NO2_RH >= NO2_RL AND SO2_RL >= 0 AND SO2_RH >= SO2_RL AND \
                    O3_RL >= 0 AND O3_RH >= O3_RL AND CO_RL >= 0 AND CO_RH >= CO_RL AND \
                    NH3_RL >= 0 AND NH3_RH >= NH3_RL), CONSTRAINT PK_GR PRIMARY KEY (Year, Season));")

    cursor.execute("CREATE TABLE Delhi_Calc(Year integer NOT NULL, Season varchar(7) NOT NULL, \
                    PM10_IL integer, PM10_IH integer, PM2_5_IL integer, PM2_5_IH integer, \
                    NO2_IL integer, NO2_IH integer, SO2_IL integer, SO2_IH integer, \
                    O3_IL integer, O3_IH integer, CO_IL integer, CO_IH integer, \
                    NH3_IL integer, NH3_IH integer, AQI_IL integer, AQI_IH integer, \
                    AQI_Avg integer, Category varchar(25), \
                    CONSTRAINT Valid CHECK (Year BETWEEN 1990 AND 2018 AND \
                    Season IN ('Summer', 'Monsoon', 'Winter', 'Spring') AND \
                    PM10_IL >= 0 AND PM10_IH >= PM10_IL AND PM2_5_IL >= 0 AND PM2_5_IH >= PM2_5_IL AND \
                    NO2_IL >= 0 AND NO2_IH >= NO2_IL AND SO2_IL >= 0 AND SO2_IH >= SO2_IL AND \
                    O3_IL >= 0 AND O3_IH >= O3_IL AND CO_IL >= 0 AND CO_IH >= CO_IL AND \
                    NH3_IL >= 0 AND NH3_IH >= NH3_IL AND AQI_IL >= 0 AND AQI_IH >= AQI_IL),\
                    CONSTRAINT FK_DC FOREIGN KEY (Year, Season) References Delhi_Raw (Year, Season), \
                    CONSTRAINT PK_DC PRIMARY KEY (Year, Season));")

    cursor.execute("CREATE TABLE Gurgaon_Calc(Year integer NOT NULL, Season varchar(7) NOT NULL, \
                    PM10_IL integer, PM10_IH integer, PM2_5_IL integer, PM2_5_IH integer, \
                    NO2_IL integer, NO2_IH integer, SO2_IL integer, SO2_IH integer, \
                    O3_IL integer, O3_IH integer, CO_IL integer, CO_IH integer, \
                    NH3_IL integer, NH3_IH integer, AQI_IL integer, AQI_IH integer, \
                    AQI_Avg integer, Category varchar(25), \
                    CONSTRAINT Valid CHECK (Year BETWEEN 1990 AND 2018 AND \
                    Season IN ('Summer', 'Monsoon', 'Winter', 'Spring') AND \
                    PM10_IL >= 0 AND PM10_IH >= PM10_IL AND PM2_5_IL >= 0 AND PM2_5_IH >= PM2_5_IL AND \
                    NO2_IL >= 0 AND NO2_IH >= NO2_IL AND SO2_IL >= 0 AND SO2_IH >= SO2_IL AND \
                    O3_IL >= 0 AND O3_IH >= O3_IL AND CO_IL >= 0 AND CO_IH >= CO_IL AND \
                    NH3_IL >= 0 AND NH3_IH >= NH3_IL AND AQI_IL >= 0 AND AQI_IH >= AQI_IL),\
                    CONSTRAINT FK_GC FOREIGN KEY (Year, Season) References Gurgaon_Raw (Year, Season), \
                    CONSTRAINT PK_GC PRIMARY KEY (Year, Season));")

    db.commit()

    for i in dd:
        add(cursor, "Delhi_Raw", i)
        add(cursor, "Delhi_Calc", calc(i))
    db.commit()

    for i in dg:
        add(cursor, "Gurgaon_Raw", i)
        add(cursor, "Gurgaon_Calc", calc(i))
    db.commit()

    for i in da:
        add(cursor, "Chart", i)
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
            print("\t4. SQL Interface")
            print("\t5. Log Out")
            inp = input("\nEnter 1, 2, 3, 4 or 5: ")
            inp = inp.lower()
            if inp not in ['1', '2', '3', '4', '5', 'add', 'add data', 'modify', 'modify data', 'delete', 'delete data'
                           'sql', 'mysql', 'sql interface', 'mysql interface', 'back', 'log out']:
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
    elif inp in ['4', 'sql', 'mysql', 'sql interface', 'mysql interface']:
        admin_sql(admins)
    else:
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


def admin_sql(admins):
    print("\n", "-" * 30, sep="")
    print("\nSQL Interface\n")
