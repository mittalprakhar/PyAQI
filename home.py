import pyaqilib as lib

password = 'PyAQI@42'

data_delhi = [
    (2009, "Spring", 95, 185, 23, 105, 9, 44, 18, 37, 16, 44, 0.2, 1.5, 16, 29, 39, 165),
    (2010, "Spring", 91, 186, 28, 134, 13, 60, 15, 42, 19, 63, 0.3, 1.4, 22, 33, 40, 186),
    (2011, "Spring", 105, 205, 39, 154, 18, 70, 16, 38, 21, 71, 0.2, 1.4, 20, 35, 38, 205),
    (2012, "Spring", 92, 217, 34, 148, 17, 66, 12, 40, 18, 64, 0.2, 1.5, 19, 35, 36, 197),
    (2013, "Spring", 89, 212, 47, 162, 20, 70, 11, 29, 25, 78, 0.3, 1.7, 24, 44, 45, 212),
    (2014, "Spring", 108, 239, 53, 171, 25, 72, 14, 38, 23, 70, 0.3, 1.6, 23, 41, 43, 239),
    (2015, "Spring", 123, 215, 60, 175, 26, 78, 12, 36, 26, 81, 0.3, 1.8, 27, 50, 48, 215),
    (2016, "Spring", 135, 243, 55, 159, 23, 80, 8, 28, 31, 96, 0.4, 2.0, 29, 53, 50, 243),
    (2017, "Spring", 127, 264, 52, 162, 20, 73, 11, 34, 33, 98, 0.3, 1.9, 30, 56, 51, 264),
    (2018, "Spring", 137, 275, 55, 161, 24, 70, 9, 29, 32, 102, 0.4, 2.0, 32, 59, 49, 275)
]

data_gurgaon = [
    (2009, "Spring", 60, 179, 32, 87, 30, 63, 13, 42, 25, 48, 0.6, 2.0,	19, 30, 48, 179),
    (2010, "Spring", 56, 230, 44, 99, 35, 69, 12, 47, 27, 45, 0.6, 2.3, 18, 35, 49, 230),
    (2011, "Spring", 76, 205, 39, 103, 33, 75, 13, 43, 23, 55, 0.6, 2.0, 17, 31, 47, 205),
    (2012, "Spring", 89, 216, 40, 100, 35, 83, 15, 52, 29, 50, 0.8, 2.4, 20, 37, 40, 216),
    (2013, "Spring", 106, 230, 49, 95, 34, 82, 16, 54, 26, 59, 0.7, 2.3, 22, 40, 42, 230),
    (2014, "Spring", 107, 235, 46, 93, 38, 79, 16, 50, 31, 64, 0.7, 2.5, 26, 42, 46, 235),
    (2015, "Spring", 125, 274, 55, 110, 40, 89, 18, 59, 34, 63, 0.8, 2.6, 19, 39, 48, 274),
    (2016, "Spring", 136, 298, 62, 123, 45, 91, 15, 62, 32, 70, 0.7, 2.7, 24, 40, 49, 298),
    (2017, "Spring", 138, 302, 63, 127, 46, 95, 18, 60, 34, 74, 0.9, 2.7, 26, 46, 52, 302),
    (2018, "Spring", 148, 345, 67, 133, 50, 100, 19, 66, 36, 78, 0.9, 3.0, 26, 47, 51, 345)
]

# If database is already set up
# db, cursor = lib.init(password=password)

# If database is not set up
db, cursor = lib.reset(data_delhi, data_gurgaon, password=password)
