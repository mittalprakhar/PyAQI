import mysql.connector
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import matplotlib.pyplot as plt
from decimal import Decimal


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
    return get_columns(cursor, "Delhi") != cols or get_columns(cursor, "Gurgaon") != cols


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

    cursor.execute("CREATE TABLE Chart(S_No integer, Category varchar(25), AQI_Min integer, \
                    AQI_Max integer, Description varchar(200));")

    cursor.execute("CREATE TABLE Delhi(Year integer NOT NULL, Season varchar(7) NOT NULL, \
                    PM10_Min integer, PM10_Max integer, PM2_5_Min integer, PM2_5_Max integer, \
                    NO2_Min integer, NO2_Max integer, SO2_Min integer, SO2_Max integer, \
                    O3_Min integer, O3_Max integer, CO_Min decimal(3,1), CO_Max decimal(3,1), \
                    NH3_Min integer, NH3_Max integer, \
                    CONSTRAINT Valid CHECK (Year BETWEEN 1990 AND 2018 AND \
                    Season IN ('Summer', 'Monsoon', 'Winter', 'Spring') AND \
                    PM10_Min >= 0 AND PM10_Max >= PM10_Min AND PM2_5_Min >= 0 AND PM2_5_Max >= PM2_5_Min AND \
                    NO2_Min >= 0 AND NO2_Max >= NO2_Min AND SO2_Min >= 0 AND SO2_Max >= SO2_Min AND \
                    O3_Min >= 0 AND O3_Max >= O3_Min AND CO_Min >= 0 AND CO_Max >= CO_Min AND \
                    NH3_Min >= 0 AND NH3_Max >= NH3_Min), CONSTRAINT PK_D PRIMARY KEY (Year, Season));")

    cursor.execute("CREATE TABLE Gurgaon(Year integer NOT NULL, Season varchar(7) NOT NULL, \
                    PM10_Min integer, PM10_Max integer, PM2_5_Min integer, PM2_5_Max integer, \
                    NO2_Min integer, NO2_Max integer, SO2_Min integer, SO2_Max integer, \
                    O3_Min integer, O3_Max integer, CO_Min decimal(3,1), CO_Max decimal(3,1), \
                    NH3_Min integer, NH3_Max integer, \
                    CONSTRAINT Valid CHECK (Year BETWEEN 1990 AND 2018 AND \
                    Season IN ('Summer', 'Monsoon', 'Winter', 'Spring') AND \
                    PM10_Min >= 0 AND PM10_Max >= PM10_Min AND PM2_5_Min >= 0 AND PM2_5_Max >= PM2_5_Min AND \
                    NO2_Min >= 0 AND NO2_Max >= NO2_Min AND SO2_Min >= 0 AND SO2_Max >= SO2_Min AND \
                    O3_Min >= 0 AND O3_Max >= O3_Min AND CO_Min >= 0 AND CO_Max >= CO_Min AND \
                    NH3_Min >= 0 AND NH3_Max >= NH3_Min), CONSTRAINT PK_G PRIMARY KEY (Year, Season));")

    db.commit()

    for i in dd:
        add(cursor, "Delhi", i)
    db.commit()

    for i in dg:
        add(cursor, "Gurgaon", i)
    db.commit()

    for i in da:
        add(cursor, "Chart", i)
    db.commit()

    return db, cursor


def home(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nWelcome to PyAQI")
    print("\nPyAQI is a Python script that can be used to access annual pollution data for Delhi and Gurgaon, \
            \nand predict the Air Quality Index for the two cities in the next 5 years.")

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
        user(db, cursor, admins)
    elif inp in ['2', 'admin']:
        print("\nLogging in as admin...")
        admin(db, cursor, admins)
    else:
        print("\nThank you.")
        quit()


def user(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nUser Menu: \n")
    while True:
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
        else:
            break

    if inp in ['1', 'access', 'data', 'access data']:
        access(db, cursor, admins)
    elif inp in ['2', 'trends', 'see trends', 'trend', 'see trend']:
        trends(db, cursor, admins)
    elif inp in ['3',  'predictions', 'prediction', 'see predictions', 'see prediction']:
        predictions(db, cursor, admins)
    elif inp in ['4', 'info', 'information', 'see info', 'see information']:
        info(db, cursor, admins)
    else:
        home(db, cursor, admins)


def admin(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nAdmin Menu: \n")
    while True:
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
                city = "Delhi"
                break
            elif int(city) == 2 or city.lower() == "gurgaon":
                city = "Gurgaon"
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
            if inp.lower() == "null" or int(inp) == -1:
                return -1
            elif float(inp) < min:
                print("Value must be above " + str(min) + "." + "\n")
            elif column[:3] == "CO_":
                return float(inp)
            else:
                return int(inp)
        except ValueError:
            print("Invalid input.\n")


def access(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nAccess Data")
    prim = inp_primary()
    if prim == "x":
        user(db, cursor, admins)
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
                print("1. City: \t\t" + city)
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
                print("\n1. City: \t\t\t" + city)
                for cno in range(len(cols)):
                    if cno < 2:
                        tab = "\t\t\t"
                    elif cno < 18:
                        tab = "\t\t"
                    else:
                        tab = "\t"
                    print(str(cno + 2) + ". " + cols[cno] + ": " + tab + str(indices[cno]))
        user(db, cursor, admins)


def trends(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nTrends\n")
    print("\nTip: Type X to go back\n")
    while True:
        try:
            print("Choose city: ")
            print("\t1. Delhi")
            print("\t2. Gurgaon")
            print("\t3. Both")
            city = input("\nEnter 1, 2 or 3: ")
            if city.lower() == "x":
                return "x"
            elif int(city) == 1 or city.lower() == "delhi":
                city = "Delhi"
                break
            elif int(city) == 2 or city.lower() == "gurgaon":
                city = "Gurgaon"
                break
            elif int(city) == 3 or city.lower() == "both":
                city = "Both"
            else:
                print("\nInvalid input.\n")
        except ValueError:
            print("\nInvalid input.\n")
    if city == "x":
        user(db, cursor, admins)
    else:
        while True:
            try:
                print("\nChoose season: ")
                print("\t1. Spring")
                print("\t2. Summer")
                print("\t3. Monsoon")
                print("\t4. Winter")
                print("\t5. Average")
                season = input("\nEnter 1, 2, 3, 4 or 5: ")
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
                elif int(season) == 5 or season.lower() == "average":
                    season = "Average"
                else:
                    print("\nInvalid input.")
            except ValueError:
                print("\nInvalid input.")
        if season == "x":
            user(db, cursor, admins)
        else:
            if city == "Both":
                pass
            else:
                pass


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
        if i % 4 == 0:
            years += [all[i][0], all[i][0] + 0.25, all[i][0] + 0.5, all[i][0] + 0.75]
    return years


def return_column(all, one, two):
    col = []
    for i in all:
        col.append((i[one]+i[two])/2)
    return col


def smooth(x1, y1):
    x2 = np.linspace(min(x1), max(x1), 400)
    spl = make_interp_spline(x1, y1, k=3)
    y2 = spl(x2)
    return x2, y2


def test(db, cursor, admins):
    all_d = return_all(cursor, "Delhi")
    all_g = return_all(cursor, "Gurgaon")
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

        plt.figure(figsize=(12, 6.5))

        plt.rc('axes', titlesize=9)
        plt.rc('axes', labelsize=9)
        plt.rc('xtick', labelsize=7)
        plt.rc('ytick', labelsize=7)

        x = [0, 1, 4]
        y = [3, 1, 0]

        plt.subplot(3, 3, 1)
        plt.xlabel('Years')
        plt.ylabel('PM 10')
        xd, yd = smooth(years_d, pm10_d)
        xg, yg = smooth(years_g, pm10_g)
        plt.plot(xd, yd, label="Delhi")
        plt.plot(xg, yg, label="Gurgaon")
        plt.legend(loc=2, fontsize = 'xx-small')

        plt.subplot(3, 3, 2)
        plt.xlabel('Years')
        plt.ylabel('PM 2.5')
        xd, yd = smooth(years_d, pm25_d)
        xg, yg = smooth(years_g, pm25_g)
        plt.plot(xd, yd, label="Delhi")
        plt.plot(xg, yg, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.subplot(3, 3, 3)
        plt.xlabel('Years')
        plt.ylabel('NO₂')
        xd, yd = smooth(years_d, no2_d)
        xg, yg = smooth(years_g, no2_g)
        plt.plot(xd, yd, label="Delhi")
        plt.plot(xg, yg, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.subplot(3, 3, 4)
        plt.xlabel('Years')
        plt.ylabel('SO₂')
        xd, yd = smooth(years_d, so2_d)
        xg, yg = smooth(years_g, so2_g)
        plt.plot(xd, yd, label="Delhi")
        plt.plot(xg, yg, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.subplot(3, 3, 5)
        plt.xlabel('Years')
        plt.ylabel('O₃')
        xd, yd = smooth(years_d, o3_d)
        xg, yg = smooth(years_g, o3_g)
        plt.plot(xd, yd, label="Delhi")
        plt.plot(xg, yg, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.subplot(3, 3, 6)
        plt.xlabel('Years')
        plt.ylabel('CO')
        xd, yd = smooth(years_d, co_d)
        xg, yg = smooth(years_g, co_g)
        plt.plot(xd, yd, label="Delhi")
        plt.plot(xg, yg, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.subplot(3, 3, 7)
        plt.xlabel('Years')
        plt.ylabel('NH₃')
        xd, yd = smooth(years_d, nh3_d)
        xg, yg = smooth(years_g, nh3_g)
        plt.plot(xd, yd, label="Delhi")
        plt.plot(xg, yg, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.subplot(3, 3, 8)
        plt.xlabel('Years')
        plt.ylabel('AQI')
        xd, yd = smooth(years_d, aqi_d)
        xg, yg = smooth(years_g, aqi_g)
        plt.plot(xd, yd, label="Delhi")
        plt.plot(xg, yg, label="Gurgaon")
        plt.legend(loc=2, fontsize='xx-small')

        plt.tight_layout()
        plt.show()

    '''years_delhi_new = np.linspace(min(years_delhi), max(years_delhi), 400)
        spl = make_interp_spline(years_delhi, pm10_delhi, k=3)
        power_smooth = spl(years_delhi_new)
        plt.plot(years_delhi_new, power_smooth, label="Delhi")

        plt.ylim(min(pm10_delhi) - 50, max(pm10_delhi) + 50)
        plt.xlabel('Years')
        plt.ylabel('Raw Values')
        plt.title('PM10')

        plt.legend()
        plt.show()'''


def predictions(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nPredictions\n")


def info(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nInformation\n")


def admin_add(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nAdd Data")
    prim = inp_primary()
    if prim == "x":
        admin(db, cursor, admins)
    else:
        city, year, season = prim[0], prim[1], prim[2]
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
                    admin(db, cursor, admins)
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
            admin(db, cursor, admins)


def admin_modify(db, cursor, admins, primary=None):
    print("\n", "-" * 30, sep="")
    print("\nModify Data")
    city, year, season = "", 0, 0
    if primary is None:
        prim = inp_primary()
        if prim == "x":
            admin(db, cursor, admins)
        else:
            city, year, season = prim[0], prim[1], prim[2]
    else:
        city, year, season = primary[0], primary[1], primary[2]
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
                    query = "SELECT * FROM " + city + " WHERE YEAR = " + str(year) + ' AND Season LIKE "' + season + '";'
                    cursor.execute(query)
                    result = cursor.fetchall()
                    for i in result:
                        if float(inp) <= i[cno + 2]:
                            flag = False
                        else:
                            print("\nValue must be below " + str(i[cno + 2]) + ".")
                elif column[-3:] == "Max":
                    query = "SELECT * FROM " + city + " WHERE YEAR = " + str(year) + ' AND Season LIKE "' + season + '";'
                    cursor.execute(query)
                    result = cursor.fetchall()
                    for i in result:
                        if float(inp) >= i[cno]:
                            flag = False
                        else:
                            print("\nValue must be above " + str(i[cno]) + ".")
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

    admin(db, cursor, admins)


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
            admin(db, cursor, admins)
        else:
            city, year, season = prim[0], prim[1], prim[2]
            query = "DELETE FROM " + city + " WHERE Year = " + str(year) + ' AND Season LIKE "' + season + '";'
            cursor.execute(query)
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
                    city = "Delhi"
                    break
                elif int(city) == 2 or city.lower() == "gurgaon":
                    city = "Gurgaon"
                    break
                else:
                    print("\nInvalid input.\n")
            except ValueError:
                print("\nInvalid input.\n")
        if city != "x":
            try:
                print("\nComplete command with desired condition or Type X to go back: \n")
                query = "DELETE FROM " + city + " WHERE "
                inp = input(query)
                query += inp
                cursor.execute(query)
                db.commit()
                print("\nTable updated.")
            except:
                print("\nInvalid command.")
    admin(db, cursor, admins)


def admin_sql(db, cursor, admins):
    print("\n", "-" * 30, sep="")
    print("\nSQL Interface\n")
    try:
        query = input("Enter SQL command: ")
        cursor.execute(query)
    except:
        print("\nInvalid command.")
        admin(db, cursor, admins)
    print("\nCommand run successfully.")
    admin(db, cursor, admins)
