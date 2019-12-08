# PyAQI
PyAQI is a Python script that can be used to access annual pollution data for Delhi and Gurgaon, and calculate Air Quality Index.

## What is AQI?
The Air Quality Index (AQI) is a measure of how polluted the air in a particular region is. Public health risks increase as the AQI increases.

## How is AQI calculated in India?
The National Air Quality Index considers eight pollutants:
- PM10
- PM2.5
- NO2
- SO2
- CO
- O3
- NH3
- Pb

Short-term National Ambient Air Quality Standards are prescribed for each pollutant. It is recognized that air concentrations of Pb are not known in real-time and cannot contribute to real-time AQI.

Based on the measured ambient concentrations, corresponding standards and likely health impact, a sub-index is calculated for each of these pollutants.

The worst sub-index reflects overall AQI. Likely health impacts for different AQI categories and pollutants have also been suggested, with primary inputs from the medical experts in the group.

## National Air Quality Index Chart
| Category                      | PM10    | PM2.5   | NO2     | O3      | CO      | SO2      | NH3       |
|-------------------------------|---------|---------|---------|---------|---------|----------|-----------|
| Good (0-50)                   | 0-50    | 0-30    | 0-40    | 0-50    | 0-1.0   | 0-40     | 0-200     |
| Satisfactory (51-100)         | 51-100  | 31-60   | 41-80   | 51-100  | 1.1-2.0 | 41-80    | 201-400   |
| Moderately Polluted (101-200) | 101-250 | 61-90   | 81-180  | 101-168 | 2.1-10  | 81-380   | 401-800   |
| Poor (201-300)                | 251-350 | 91-120  | 181-280 | 169-208 | 10-17   | 381-800  | 801-1200  |
| Very Poor (301-400)           | 351-430 | 121-250 | 281-400 | 209-748 | 17-34   | 801-1600 | 1200-1800 |
| Severe (401-500)              | 430+    | 250+    | 400+    | 748+    | 34+     | 1600+    | 1800+     |
