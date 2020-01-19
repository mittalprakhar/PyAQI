import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal


mysql_password = 'PyAQI@42'
admins = [('Prakhar', 'PM')]


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


def check_corrupted(cursor):
    cols = ['Year', 'Season', 'PM10_Min', 'PM10_Max', 'PM2_5_Min', 'PM2_5_Max', 'NO2_Min', 'NO2_Max', 'SO2_Min', 'SO2_Max', 'O3_Min', 'O3_Max', 'CO_Min', 'CO_Max', 'NH3_Min', 'NH3_Max']
    return get_columns(cursor, "delhi") != cols or get_columns(cursor, "gurgaon") != cols


def add(cursor, table, data):
    if table in get_tables(cursor) and len(data) == len(get_columns(cursor, table)):
        query = "INSERT INTO " + table + " VALUES(" + "%s, " * (len(data) - 1) + "%s);"
        cursor.execute(query, data)
    else:
        print("Add Error")


def rawToIndices(inp):
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


def init(user='root', password='PyAQI@42', host='localhost', database='pyaqi'):
    db = mysql.connector.connect(user=user, password=password, host=host, database=database)
    return db, db.cursor()


def reset(dd, dg, da, user='root', password='PyAQI@42', host='localhost'):
    db = mysql.connector.connect(user=user, password=password, host=host)
    cursor = db.cursor()

    cursor.execute("DROP DATABASE IF EXISTS pyaqi;")
    db.commit()

    cursor.execute("CREATE DATABASE pyaqi;")

    cursor.execute("USE pyaqi;")
    db.commit()

    cursor.execute("CREATE TABLE chart(S_No integer, Category varchar(25), AQI_Min integer, \
                    AQI_Max integer, Description varchar(200));")

    cursor.execute("CREATE TABLE delhi(Year integer NOT NULL, Season varchar(7) NOT NULL, \
                    PM10_Min integer, PM10_Max integer, PM2_5_Min integer, PM2_5_Max integer, \
                    NO2_Min integer, NO2_Max integer, SO2_Min integer, SO2_Max integer, \
                    O3_Min integer, O3_Max integer, CO_Min decimal(3,1), CO_Max decimal(3,1), \
                    NH3_Min integer, NH3_Max integer, \
                    CONSTRAINT pk_d PRIMARY KEY (Year, Season));")

    cursor.execute("CREATE TABLE gurgaon(Year integer NOT NULL, Season varchar(7) NOT NULL, \
                    PM10_Min integer, PM10_Max integer, PM2_5_Min integer, PM2_5_Max integer, \
                    NO2_Min integer, NO2_Max integer, SO2_Min integer, SO2_Max integer, \
                    O3_Min integer, O3_Max integer, CO_Min decimal(3,1), CO_Max decimal(3,1), \
                    NH3_Min integer, NH3_Max integer, \
                    CONSTRAINT pk_g PRIMARY KEY (Year, Season));")

    db.commit()

    for i in dd:
        add(cursor, "delhi", i)
    db.commit()

    for i in dg:
        add(cursor, "gurgaon", i)
    db.commit()

    for i in da:
        add(cursor, "chart", i)
    db.commit()

    return db, cursor


def home(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nWelcome to PyAQI")
    print("\nPyAQI is a Python script that can be used to access annual pollution data for Delhi and Gurgaon, \
            \nand evaluate Air Quality Index values for the same.")

    while True:
        while True:
            print("\nChoose login type: ")
            print("\t1. User")
            print("\t2. Admin")
            print("\t3. Quit")
            inp = input("\nEnter 1, 2 or 3: ")
            inp = inp.lower()
            if inp not in ['1', '2', '3', 'user', 'admin', 'quit', 'exit']:
                print("\nInvalid input.")
            else:
                break

        if inp in ['2', 'admin']:
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
        else:
            break

    if inp in ['1', 'user']:
        print("\nLogging in as user...")
        user(db, cursor, admins, False)
    elif inp in ['2', 'admin']:
        print("\nLogging in as admin...")
        admin(db, cursor, admins, True)
    else:
        print("\nThank you.")
        quit()


def user(db, cursor, admins, adm):
    print("\n", "-" * 30, sep="")
    print("\nUser Menu: \n")
    while True:
        print("Choose task: ")
        print("\t1. Access Data")
        print("\t2. See Trends")
        print("\t3. See AQI Chart")
        print("\t4. Go Back")
        inp = input("\nEnter 1, 2, 3 or 4: ")
        inp = inp.lower()
        if inp not in ['1', '2', '3', '4', 'access', 'data', 'access data', 'trends', 'see trends',
                       'trend', 'see trend', 'see chart', 'chart', 'see aqi chart', 'aqi chart', 'back', 'go back']:
            print("\nInvalid input.\n")
        else:
            break

    if inp in ['1', 'access', 'data', 'access data']:
        access(db, cursor, admins, adm)
    elif inp in ['2', 'trends', 'see trends', 'trend', 'see trend']:
        trends(db, cursor, admins, adm)
    elif inp in ['3', 'see chart', 'chart', 'see aqi chart', 'aqi chart']:
        chart(db, cursor, admins, adm)
    else:
        home(db, cursor, admins)


def admin(db, cursor, admins, adm):
    print("\n", "-" * 30, sep="")
    print("\nAdmin Menu: \n")
    while True:
        print("Choose task: ")
        print("\t1. Add Data")
        print("\t2. Modify Data")
        print("\t3. Delete Data")
        print("\t4. SQL Interface")
        print("\t5. Access Data")
        print("\t6. See Trends")
        print("\t7. See AQI Chart")
        print("\t8. Log Out")
        inp = input("\nEnter option number: ")
        inp = inp.lower()
        if inp not in ['1', '2', '3', '4', '5', 'add', 'add data', 'modify', 'modify data', 'delete', 'delete data'
                       'sql', 'mysql', 'sql interface', 'mysql interface', 'back', 'log out', '6', '7', '8',
                       'access', 'data', 'access data', 'trends', 'see trends',
                       'trend', 'see trend', 'see chart', 'chart', 'see aqi chart', 'aqi chart']:
            print("\nInvalid input.\n")
        else:
            break

    if inp in ['1', 'add', 'add data']:
        admin_add(db, cursor, admins)
    elif inp in ['2', 'modify', 'modify data']:
        admin_modify(db, cursor, admins)
    elif inp in ['3', 'delete', 'delete data']:
        admin_delete(db, cursor, admins)
    elif inp in ['4', 'sql', 'mysql', 'sql interface', 'mysql interface']:
        admin_sql(db, cursor, admins)
    elif inp in ['5', 'access', 'data', 'access data']:
        access(db, cursor, admins, adm)
    elif inp in ['6', 'trends', 'see trends', 'trend', 'see trend']:
        trends(db, cursor, admins, adm)
    elif inp in ['7', 'see chart', 'chart', 'see aqi chart', 'aqi chart']:
        chart(db, cursor, admins, adm)
    else:
        print("\nLogging out...")
        home(db, cursor, admins)


def inp_primary():
    print("\nTip: Type X to go back\n")
    while True:
        try:
            print("Choose city: ")
            print("\t1. Delhi")
            print("\t2. Gurgaon")
            city = input("\nEnter 1 or 2: ")
            if city.lower() == "x":
                return "x"
            elif int(city) == 1 or city.lower() == "delhi":
                city = "delhi"
                break
            elif int(city) == 2 or city.lower() == "gurgaon":
                city = "gurgaon"
                break
            else:
                print("\nInvalid input.\n")
        except ValueError:
            print("\nInvalid input.\n")

    while True:
        try:
            year = input("\nEnter year: ")
            if year.lower() == "x":
                return "x"
            else:
                year = int(year)
                break
        except ValueError:
            print("\nInvalid input.")

    while True:
        try:
            print("\nChoose season: ")
            print("\t1. Spring")
            print("\t2. Summer")
            print("\t3. Monsoon")
            print("\t4. Winter")
            season = input("\nEnter 1, 2, 3 or 4: ")
            if season.lower() == "x":
                return "x"
            elif int(season) == 1 or season.lower() == "spring":
                season = "Spring"
                break
            elif int(season) == 2 or season.lower() == "summer":
                season = "Summer"
                break
            elif int(season) == 3 or season.lower() == "monsoon":
                season = "Monsoon"
                break
            elif int(season) == 4 or season.lower() == "winter":
                season = "Winter"
                break
            else:
                print("\nInvalid input.")
        except ValueError:
            print("\nInvalid input.")
    return city, year, season


def inp_value(column, min):
    while True:
        try:
            string = column + " value: "
            inp = input(string)
            if min == -1:
                min = 0
            if inp.lower() == "null" or int(inp) == -1:
                return -1
            elif float(inp) < 0 or float(inp) < min:
                print("Value must be above " + str(min) + "." + "\n")
            elif column[:3] == "CO_":
                return float(inp)
            else:
                return int(inp)
        except ValueError:
            print("Invalid input.\n")


def access(db, cursor, admins, adm):
    print("\n", "-" * 30, sep="")
    print("\nAccess Data")
    prim = inp_primary()
    if prim == "x":
        if adm:
            admin(db, cursor, admins, adm)
        else:
            user(db, cursor, admins, adm)
    else:
        city, year, season = prim[0], prim[1], prim[2]
        while True:
            print("\nChoose an option:\n")
            print("\t1. Raw values")
            print("\t2. Sub-index values")
            print("\t3. Go back")
            inp = input("\nEnter 1, 2 or 3: ")
            inp = inp.lower()
            if inp not in ['1', '2', '3', 'raw', 'sub-index', 'raw values', 'sub-index values', 'back', 'quit', 'exit']:
                print("\nInvalid input.\n")
            else:
                break
        if inp in ['1', 'raw', 'raw values']:
            query = "SELECT * FROM " + city + " WHERE YEAR = " + str(year) + ' AND Season LIKE "' + season + '";'
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) == 0:
                print("\nNo data found.")
            elif check_corrupted(cursor):
                print("\nTable corrupted.")
            else:
                cno = 3
                print()
                print("1. City: \t\t" + city.capitalize())
                print("2. Year: \t\t" + str(year))
                print("3. Season: \t\t" + season)
                array = [year, season]
                for j in result[0][cno-1:]:
                    col = get_columns(cursor, city)[cno-1].replace("2_5", "2.5").replace("_", " ")
                    unit = u"μ" + "g/m" + u"³"
                    if col[:2] == "CO":
                        unit = "mg/m" + u"³"
                    print(str(cno + 1) + ". " + col + ": " + "\t" + str(result[0][cno-1]) + "\t" + unit)
                    cno += 1
                    if type(j) is Decimal:
                        j = float(j)
                    array.append(j)
                print(str(cno + 2) + ". AQI Category: \t" + rawToIndices(array)[-1])
        elif inp in ['2', 'sub-index', 'sub-index values']:
            if check_corrupted(cursor):
                print("\nTable corrupted.")
            else:
                query = "SELECT * FROM " + city + " WHERE YEAR = " + str(year) + ' AND Season LIKE "' + season + '";'
                cursor.execute(query)
                result = cursor.fetchall()
                if len(result) == 0:
                    print("\nNo data found.")
                else:
                    array = []
                    for i in result[0]:
                        if type(i) is Decimal:
                            i = float(i)
                        array.append(i)
                    indices = rawToIndices(array)
                    cols = []
                    for i in get_columns(cursor, city):
                        cols.append(i.replace("2_5", "2.5").replace("_", " "))
                    cols += ["AQI Min", "AQI Max", "AQI Average", "AQI Category"]
                    print("\n1. City: \t\t" + city.capitalize())
                    for cno in range(len(cols)):
                        if cno < 2:
                            tab = "\t\t"
                        elif cno < 18:
                            tab = "\t\t"
                        else:
                            tab = "\t"
                        print(str(cno + 2) + ". " + cols[cno] + ": " + tab + str(indices[cno]))
        if adm:
            admin(db, cursor, admins, adm)
        else:
            user(db, cursor, admins, adm)


def return_all(cursor, table):
    query = "SELECT * FROM " + table + " ORDER BY Year, FIELD(Season, 'Spring', 'Summer', 'Monsoon', 'Winter');"
    cursor.execute(query)
    all = cursor.fetchall()
    if check_corrupted(cursor):
        return []
    else:
        all_new = []
        for i in range(len(all)):
            row = []
            for j in range(len(all[i])):
                if type(all[i][j]) is Decimal:
                    row.append(float(all[i][j]))
                else:
                    row.append(all[i][j])
            all_new.append(tuple(row))
        return all_new


def return_years(all):
    years = []
    for i in range(len(all)):
        plus = 0
        if all[i][1] == "Summer":
            plus = 0.25
        elif all[i][1] == "Monsoon":
            plus = 0.5
        elif all[i][1] == "Winter":
            plus = 0.75
        years += [all[i][0] + plus]
    return years


def return_column(all, one, two):
    col = []
    for i in all:
        onev = i[one]
        twov = i[two]
        if onev == -1:
            col.append(twov * 0.7)
        elif twov == -1:
            col.append(onev * 1.3)
        else:
            col.append((i[one]+i[two])/2)
    return col


def trends(db, cursor, admins, adm):
    all_d = return_all(cursor, "delhi")
    all_g = return_all(cursor, "gurgaon")
    if all_d == [] or all_g == []:
        print("Tables corrupted.")
    else:
        years_d = return_years(all_d)
        years_g = return_years(all_g)

        pm10_d = return_column(all_d, 2, 3)
        pm10_g = return_column(all_g, 2, 3)

        pm25_d = return_column(all_d, 4, 5)
        pm25_g = return_column(all_g, 4, 5)

        no2_d = return_column(all_d, 6, 7)
        no2_g = return_column(all_g, 6, 7)

        so2_d = return_column(all_d, 8, 9)
        so2_g = return_column(all_g, 8, 9)

        o3_d = return_column(all_d, 10, 11)
        o3_g = return_column(all_g, 10, 11)

        co_d = return_column(all_d, 12, 13)
        co_g = return_column(all_g, 12, 13)

        nh3_d = return_column(all_d, 14, 15)
        nh3_g = return_column(all_g, 14, 15)

        aqi_d = []
        for i in all_d:
            aqi_d.append(rawToIndices(i)[-2])

        aqi_g = []
        for i in all_g:
            aqi_g.append(rawToIndices(i)[-2])

        plt.figure(figsize=(12, 6.5), facecolor="#eeeeee")

        plt.rc('axes', titlesize=9)
        plt.rc('axes', labelsize=9)
        plt.rc('xtick', labelsize=7)
        plt.rc('ytick', labelsize=7)

        plt.subplot(3, 3, 1)
        plt.xlabel('Years')
        plt.ylabel('PM 10')
        plt.plot(years_d, pm10_d, label="Delhi")
        plt.plot(years_g, pm10_g, label="Gurgaon")
        plt.legend(loc = 2, fontsize = 'xx-small')

        plt.subplot(3, 3, 2)
        plt.xlabel('Years')
        plt.ylabel('PM 2.5')
        plt.plot(years_d, pm25_d, label="Delhi")
        plt.plot(years_g, pm25_g, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.subplot(3, 3, 3)
        plt.xlabel('Years')
        plt.ylabel('NO₂')
        plt.plot(years_d, no2_d, label="Delhi")
        plt.plot(years_g, no2_g, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.subplot(3, 3, 4)
        plt.xlabel('Years')
        plt.ylabel('SO₂')
        plt.plot(years_d, so2_d, label="Delhi")
        plt.plot(years_g, so2_g, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')
                
        plt.subplot(3, 3, 5)
        plt.xlabel('Years')
        plt.ylabel('CO')
        plt.plot(years_d, co_d, label="Delhi")
        plt.plot(years_g, co_g, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.subplot(3, 3, 6)
        plt.xlabel('Years')
        plt.ylabel('NH₃')
        plt.plot(years_d, nh3_d, label="Delhi")
        plt.plot(years_g, nh3_g, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.subplot(3, 3, 7)
        plt.xlabel('Years')
        plt.ylabel('O₃')
        plt.plot(years_d, o3_d, label="Delhi")
        plt.plot(years_g, o3_g, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')
        
        plt.subplot(3, 3, 8)
        plt.xlabel('Years')
        plt.ylabel('AQI')
        plt.plot(years_d, aqi_d, label="Delhi")
        plt.plot(years_g, aqi_g, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.tight_layout()
        plt.show()

        if adm:
            admin(db, cursor, admins, adm)
        else:
            user(db, cursor, admins, adm)


def chart(db, cursor, admins, adm):
    print("\n", "-" * 30, sep="")
    print("\nInformation\n")
    query = "SELECT * from chart;"
    cursor.execute(query)
    result = cursor.fetchall()
    print("{0:<7}{1:<20}{2:<5}{3:<5}{4:<100}".format("S.No.", "Category", "Low", "High", "Description"))
    print("-" * 125, sep="")
    for i in result:
        print("{0:<7}{1:<20}{2:<5}{3:<5}{4:<100}".format(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4])))
    if adm:
        admin(db, cursor, admins, adm)
    else:
        user(db, cursor, admins, adm)


def admin_add(db, cursor, admins, primary = None):
    print("\n", "-" * 30, sep="")
    print("\nAdd Data")
    if primary == None:
        prim = inp_primary()
        if prim == "x":
            admin(db, cursor, admins, True)
        else:
            city, year, season = prim[0], prim[1], prim[2]
    else:
        city, year, season = primary[0], primary[1], primary[2]

    query = "SELECT * from " + city + ";"
    cursor.execute(query)
    result = cursor.fetchall()
    flag = False
    for i in result:
        if i[0] == year and i[1] == season:
            flag = True
    if flag:
        while True:
            inp = input("\nRecord already exists. Do you wish to modify record instead? (Y/N): ")
            if inp.lower() in ["yes", "y", "yeah"]:
                admin_modify(db, cursor, admins, primary=prim)
                break
            elif inp.lower() in ["no", "n", "nah"]:
                print("\nRedirecting to Admin menu...")
                admin(db, cursor, admins, True)
                break
            else:
                print("Please enter Y or N.")
    else:
        print("\nAccepting Values (Type Null or -1 if value missing):\n")
        array = [year, season]
        for i in get_columns(cursor, city):
            if i not in ["Year", "Season"]:
                if len(array) % 2 == 0:
                    min = 0
                else:
                    min = array[-1]
                array.append(inp_value(i, min))
        add(cursor, city, array)
        db.commit()
        print("\nTable updated.")
        admin(db, cursor, admins, True)


def admin_modify(db, cursor, admins, primary=None):
    print("\n", "-" * 30, sep="")
    print("\nModify Data")
    city, year, season = "", 0, 0
    if primary is None:
        prim = inp_primary()
        if prim == "x":
            admin(db, cursor, admins, True)
        else:
            city, year, season = prim[0], prim[1], prim[2]
    else:
        city, year, season = primary[0], primary[1], primary[2]
    query = "SELECT * FROM " + city + " WHERE YEAR = " + str(year) + ' AND Season LIKE "' + season + '";'
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
        while True:
            inp = input("\nRecord does not exist. Do you wish to add record instead? (Y/N): ")
            if inp.lower() in ["yes", "y", "yeah"]:
                admin_add(db, cursor, admins, primary=prim)
                break
            elif inp.lower() in ["no", "n", "nah"]:
                print("\nRedirecting to Admin menu...")
                admin(db, cursor, admins, True)
                break
            else:
                print("Please enter Y or N.")
    while True:
        print("\nChoose an option:\n")
        print("\t1. Single column")
        print("\t2. Several columns")
        print("\t3. Go back")
        inp = input("\nEnter 1, 2 or 3: ")
        inp = inp.lower()
        if inp not in ['1', '2', '3', 'single', 'several', 'multiple', 'back', 'quit', 'exit']:
            print("\nInvalid input.\n")
        else:
            break
    if inp in ['1', 'single']:
        while True:
            try:
                print("\nChoose column: ")
                sno = 1
                col_list = get_columns(cursor, city)[2:]
                for i in col_list:
                    print("\t " + str(sno) + ". " + i)
                    sno += 1
                cno = int(input("\nEnter column number: "))
                if 0 < cno < len(col_list) + 1:
                    break
                else:
                    print("\nInvalid input.")
            except ValueError:
                print("\nInvalid input.")
        column = col_list[cno - 1]
        flag = True
        while flag:
            try:
                string = "\nEnter new value for " + column + ": "
                inp = input(string)
                if column[-3:] == "Min":
                    for i in result:
                        maxv = i[cno + 2]
                        if float(inp) == -1 or float(inp) >= 0 and maxv == -1 or maxv >= float(inp) >= 0:
                            flag = False
                        else:
                            print("\nValue must be below " + str(maxv) + ".")
                elif column[-3:] == "Max":
                    for i in result:
                        minv = i[cno]
                        if minv == -1:
                            minv = 0
                        if float(inp) == -1 or float(inp) >= minv:
                            flag = False
                        else:
                            print("\nValue must be above " + str(minv) + ".")
                else:
                    break
            except ValueError:
                print("\nInvalid input.")
        query = "UPDATE " + city + " SET " + column + " = " + inp + " WHERE YEAR = " + str(year) + ' AND Season LIKE "' + season + '";'
        cursor.execute(query)
        db.commit()
        print("\nTable updated.")

    elif inp in ['2', 'several', 'multiple']:
        print("\nAccepting Values (Type Null or -1 if value missing):\n")
        array = [year, season]
        for i in get_columns(cursor, city):
            if i not in ["Year", "Season"]:
                if get_columns(cursor, city)[len(array)][-3:] == "Max":
                    min = array[-1]
                else:
                    min = 0
                array.append(inp_value(i, min))
        query = "DELETE FROM " + city + " WHERE Year = " + str(year) + ' AND Season LIKE "' + season + '";'
        cursor.execute(query)
        db.commit()
        add(cursor, city, array)
        db.commit()
        print("\nTable updated.")

    admin(db, cursor, admins, True)


def admin_delete(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nDelete Data")
    while True:
        try:
            print("\nChoose method: ")
            print("\t1. By Primary Key")
            print("\t2. By Condition")
            inp = input("\nEnter 1 or 2: ")
            if inp.lower() in ['1', 'primary', 'key', 'primary key', 'by primary key', '2', 'condition', 'by condition']:
                break
            else:
                print("\nInvalid input.")
        except ValueError:
            print("\nInvalid input.")
    if inp.lower() in ['1', 'primary', 'key', 'primary key', 'by primary key']:
        prim = inp_primary()
        if prim == "x":
            admin(db, cursor, admins, True)
        else:
            city, year, season = prim[0], prim[1], prim[2]
            query = "DELETE FROM " + city + " WHERE Year = " + str(year) + ' AND Season LIKE "' + season + '";'
            cursor.execute(query)
            print("\nTable updated.")
            db.commit()
    else:
        print("\nTip: Type X to go back\n")
        while True:
            try:
                print("Choose city: ")
                print("\t1. Delhi")
                print("\t2. Gurgaon")
                city = input("\nEnter 1 or 2: ")
                if city.lower() == "x":
                    city = "x"
                    break
                elif int(city) == 1 or city.lower() == "delhi":
                    city = "delhi"
                    break
                elif int(city) == 2 or city.lower() == "gurgaon":
                    city = "gurgaon"
                    break
                else:
                    print("\nInvalid input.\n")
            except ValueError:
                print("\nInvalid input.\n")
        if city != "x":
            try:
                print("\nComplete command with desired condition or type X to go back: \n")
                query = "DELETE FROM " + city + " WHERE "
                inp = input(query)
                query += inp
                cursor.execute(query)
                db.commit()
                print("\nTable updated.")
            except:
                print("\nInvalid command.")
    admin(db, cursor, admins, True)


def admin_sql(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nSQL Interface\n")
    flag = True
    try:
        query = input("Enter SQL command or type X to go back: ")
        if query not in ["x", "X", "back", "quit"]:   
            if query.lower().find("drop") != -1:
                print("\nDrop command cannot be executed.")
                flag = False
            else:
                cursor.execute(query)
            if query.lower().find("desc") != -1 or query.lower().find("select") != -1:
                result = cursor.fetchall()
                print()
                if len(result) == 0:
                    print("Empty set")
                else:
                    for i in result:
                        print(i)
            else:
                db.commit()
        else:
            flag = False
    except:
        print("\nInvalid command.")
        admin(db, cursor, admins, True)
    if flag:
        print("\nCommand run successfully.")
    admin(db, cursor, admins, True)


data_delhi = [
    (2009, "Spring", 57, 185, 23, 105, 9, 44, 18, 37, 16, 44, 0.2, 1.5, 16, 29),
    (2010, "Spring", 55, 186, 28, 134, 13, 60, 15, 42, 19, 63, 0.3, 1.4, 22, 33),
    (2011, "Spring", 61, 205, 39, 154, 18, 70, 16, 38, 21, 71, 0.2, 1.4, 20, 35),
    (2012, "Spring", 54, 217, 34, 148, 17, 66, 12, 40, 18, 64, 0.2, 1.5, 19, 35),
    (2013, "Spring", 57, 212, 47, 162, 20, 70, 11, 29, 25, 78, 0.3, 1.7, 24, 44),
    (2014, "Spring", 65, 239, 53, 171, 25, 72, 14, 38, 23, 70, 0.3, 1.6, 23, 41),
    (2015, "Spring", 68, 215, 60, 175, 26, 78, 12, 36, 26, 81, 0.3, 1.8, 27, 50),
    (2016, "Spring", 68, 243, 55, 159, 23, 80, 8, 28, 31, 96, 0.4, 2.0, 29, 53),
    (2017, "Spring", 73, 264, 52, 162, 20, 73, 11, 34, 33, 98, 0.3, 1.9, 30, 56),
    (2018, "Spring", 72, 275, 55, 161, 24, 70, 9, 29, 32, 102, 0.4, 2.0, 32, 59),

    (2009, "Summer", 53, 274, 20, 211, 13, 58, 13, 28, 18, 67, 0.2, 0.6, 14, 47),
    (2010, "Summer", 50, 300, 23, 208, 14, 56, 10, 26, 18, 63, 0.2, 0.5, 14, 42),
    (2011, "Summer", 57, 298, 24, 217, 15, 61, 9, 23, 19, 66, 0.2, 0.5, 16, 46),
    (2012, "Summer", 60, 326, 21, 231, 15, 64, 7, 18, 21, 69, 0.3, 0.6, 17, 59),
    (2013, "Summer", 69, 346, 25, 246, 16, 63, 8, 20, 20, 71, 0.2, 0.7, 19, 61),
    (2014, "Summer", 62, 342, 26, 248, 17, 68, 6, 17, 25, 80, 0.3, 0.8, 19, 64),
    (2015, "Summer", 63, 368, 26, 251, 16, 71, 6, 18, 24, 78, 0.5, 0.7, 18, 67),
    (2016, "Summer", 68, 370, 25, 258, 18, 71, 5, 14, 24, 82, 0.4, 0.6, 20, 78),
    (2017, "Summer", 67, 392, 28, 280, 20, 76, 3, 12, 27, 85, 0.4, 0.7, 22, 81),
    (2018, "Summer", 72, 413, 30, 285, 20, 80, 4, 14, 27, 100, 0.5, 0.9, 22, 87),

    (2009, "Monsoon", 36, 174, 37, 127, 22, 56, 5, 18, 20, 98, 0.1, 1.2, 8, 29),
    (2010, "Monsoon", 40, 170, 34, 130, 24, 58, 4, 16, 23, 99, 0.2, 1.4, 9, 32),
    (2011, "Monsoon", 35, 172, 39, 129, 24, 62, 6, 13, 21, 97, 0.2, 1.5, 12, 28),
    (2012, "Monsoon", 41, 177, 40, 135, 26, 61, 4, 15, 25, 102, 0.3, 1.6, 9, 33),
    (2013, "Monsoon", 43, 182, 39, 133, 22, 62, 3, 14, 29, 106, 0.2, 1.5, 14, 36),
    (2014, "Monsoon", 43, 180, 37, 138, 26, 66, 5, 12, 31, 104, 0.4, 1.7, 12, 39),
    (2015, "Monsoon", 41, 184, 40, 143, 27, 64, 2, 11, 30, 108, 0.4, 1.7, 11, 35),
    (2016, "Monsoon", 45, 187, 42, 142, 29, 68, 3, 13, 35, 111, 0.3, 1.8, 15, 40),
    (2017, "Monsoon", 46, 191, 45, 141, 28, 69, 2, 10, 37, 112, 0.4, 1.9, 11, 42),
    (2018, "Monsoon", 48, 190, 48, 145, 31, 72, 3, 12, 39, 119, 0.5, 1.8, 17, 39),

    (2009, "Winter", 98, 334, 54, 325, 42, 121, 4, 15, 20, 102, 0.6, 2.2, 54, 129),
    (2010, "Winter", 104, 348, 59, 359, 47, 135, 6, 16, 25, 118, 0.8, 2.4, 58, 133),
    (2011, "Winter", 123, 394, 63, 372, 41, 139, 6, 18, 28, 103, 0.5, 2.3, 62, 138),
    (2012, "Winter", 102, 413, 55, 386, 50, 142, 5, 14, 23, 124, 0.7, 2.6, 63, 142),
    (2013, "Winter", 116, 402, 62, 378, 58, 148, 8, 17, 32, 129, 0.7, 2.8, 67, 149),
    (2014, "Winter", 99, 489, 59, 410, 54, 145, 9, 12, 35, 132, 0.7, 2.7, 71, 152),
    (2015, "Winter", 134, 524, 74, 427, 61, 153, 11, 11, 39, 137, 0.8, 3.0, 62, 158),
    (2016, "Winter", 145, 594, 78, 469, 67, 161, 12, 13, 43, 135, 0.8, 3.1, 73, 149),
    (2017, "Winter", 129, 634, 71, 503, 71, 165, 9, 9, 36, 143, 0.9, 3.1, 74, 128),
    (2018, "Winter", 141, 794, 82, 525, 69, 159, 10, 12, 37, 132, 1.0, 2.9, 79, 135)
]

data_gurgaon = [
    (2009, "Spring", 47, 179, 32, 87, 30, 63, 19, 66, 25, 48, 0.6, 2.0, 19, 30),
    (2010, "Spring", 48, 230, 44, 99, 35, 69, 18, 60, 27, 45, 0.6, 2.3, 18, 35),
    (2011, "Spring", 50, 205, 39, 103, 33, 75, 15, 62, 23, 55, 0.6, 2.0, 17, 31),
    (2012, "Spring", 54, 216, 40, 100, 35, 83, 18, 59, 29, 50, 0.8, 2.4, 20, 37),
    (2013, "Spring", 58, 230, 49, 95, 34, 82, 16, 50, 26, 59, 0.7, 2.3, 22, 40),
    (2014, "Spring", 63, 235, 46, 93, 38, 79, 16, 54, 31, 64, 0.7, 2.5, 26, 42),
    (2015, "Spring", 67, 274, 55, 110, 40, 89, 15, 52, 34, 63, 0.8, 2.6, 19, 39),
    (2016, "Spring", 68, 298, 62, 123, 45, 91, 13, 43, 32, 70, 0.7, 2.7, 24, 40),
    (2017, "Spring", 71, 302, 63, 127, 46, 95, 12, 47, 34, 74, 0.9, 2.7, 26, 46),
    (2018, "Spring", 74, 345, 67, 133, 50, 100, 14, 42, 36, 78, 0.9, 3.0, 26, 47),

    (2009, "Summer", 47, 274, 17, 230, 12, 62, 16, 28, 17, 61, 0.3, 0.9, 18, 54),
    (2010, "Summer", 53, 300, 21, 227, 16, 63, 16, 26, 16, 62, 0.3, 0.9, 19, 51),
    (2011, "Summer", 51, 298, 29, 240, 19, 69, 15, 23, 18, 66, 0.2, 0.9, 22, 52),
    (2012, "Summer", 58, 326, 33, 239, 21, 76, 15, 18, 20, 69, 0.4, 1.0, 25, 58),
    (2013, "Summer", 63, 346, 39, 243, 28, 74, 16, 20, 23, 71, 0.5, 1.3, 29, 63),
    (2014, "Summer", 65, 342, 40, 254, 34, 82, 14, 17, 22, 80, 0.4, 1.2, 30, 68),
    (2015, "Summer", 71, 368, 38, 269, 28, 85, 12, 18, 24, 78, 0.5, 1.4, 34, 71),
    (2016, "Summer", 73, 370, 44, 258, 36, 97, 10, 14, 25, 82, 0.4, 1.4, 35, 82),
    (2017, "Summer", 81, 392, 46, 280, 40, 101, 9, 12, 24, 85, 0.5, 1.5, 36, 91),
    (2018, "Summer", 85, 438, 53, 330, 49, 126, 7, 22, 29, 101, 0.6, 1.7, 39, 102),

    (2009, "Monsoon", 42, 184, 22, 142, 12, 38, 5, 20, 13, 53, 0.3, 1.2, 5, 30),
    (2010, "Monsoon", 43, 203, 25, 155, 13, 42, 4, 19, 14, 66, 0.3, 1.5, 9, 35),
    (2011, "Monsoon", 51, 197, 37, 153, 12, 51, 5, 23, 17, 62, 0.4, 1.3, 13, 33),
    (2012, "Monsoon", 47, 198, 33, 157, 16, 48, 5, 18, 15, 76, 0.5, 1.3, 11, 39),
    (2013, "Monsoon", 52, 205, 36, 169, 18, 56, 4, 17, 19, 74, 0.4, 1.5, 19, 42),
    (2014, "Monsoon", 57, 206, 44, 175, 14, 55, 3, 16, 23, 77, 0.2, 1.8, 21, 47),
    (2015, "Monsoon", 56, 223, 51, 170, 20, 62, 3, 16, 25, 89, 0.5, 1.9, 23, 44),
    (2016, "Monsoon", 62, 225, 49, 181, 23, 65, 5, 19, 21, 97, 0.6, 1.7, 22, 52),
    (2017, "Monsoon", 75, 242, 53, 191, 21, 68, 6, 17, 29, 102, 0.7, 1.7, 26, 58),
    (2018, "Monsoon", 66, 230, 57, 206, 25, 70, 2, 13, 31, 99, 0.7, 1.9, 25, 53),

    (2009, "Winter", 99, 436, 69, 362, 38, 119, 5, 12, 19, 92, 0.7, 2.3, 56, 140),
    (2010, "Winter", 104, 461, 74, 381, 41, 123, 4, 11, 21, 97, 0.8, 2.3, 62, 148),
    (2011, "Winter", 116, 496, 72, 408, 43, 128, 3, 9, 24, 102, 0.8, 2.4, 68, 151),
    (2012, "Winter", 132, 523, 79, 423, 46, 125, 4, 8, 29, 109, 0.7, 2.5, 71, 157),
    (2013, "Winter", 164, 587, 83, 455, 51, 131, 6, 9, 32, 114, 0.9, 2.1, 69, 159),
    (2014, "Winter", 156, 568, 88, 420, 48, 135, 3, 11, 37, 118, 1.0, 2.0, 73, 163),
    (2015, "Winter", 175, 635, 94, 473, 46, 139, 4, 10, 35, 124, 0.9, 2.7, 76, 165),
    (2016, "Winter", 158, 686, 102, 487, 52, 143, 5, 9, 42, 128, 1.0, 2.9, 79, 169),
    (2017, "Winter", 145, 728, 134, 495, 57, 148, 3, 9, 46, 131, 0.9, 3.1, 81, 172),
    (2018, "Winter", 130, 801, 126, 472, 59, 151, 3, 8, 51, 129, 0.9, 3.1, 83, 175)
]

data_aqi = [
    (1, "Good", 0, 50, "People are not exposed to any health risk as the air is pure."),
    (2, "Satisfactory", 51, 100, "Minor discomfort to sensitive people."),
    (3, "Moderately Polluted", 101, 200, "Discomfort to people with lung disease, asthma or heart disease, and to children and older adults."),
    (4, "Poor", 201, 300, "Discomfort to people on prolonged exposure."),
    (5, "Very Poor", 301, 400, "Respiratory illness on prolonged exposure, more pronounced in people with lung/heart disease."),
    (6, "Severe", 401, 500, "Respiratory impact even on healthy people, and serious impact on people with lung/heart disease.")
]

# If database is already set up
# db, cursor = init(password=mysql_password)

# If database is not set up
db, cursor = reset(data_delhi, data_gurgaon, data_aqi, password=mysql_password)

home(db, cursor, admins)

db.commit()
db.close()
