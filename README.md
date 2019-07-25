# PyAQI

PyAQI is a Python script that analyzes pollution data to predict the Air Quality Index of Delhi-NCR in the upcoming week.

## What is Air Quality Index?
The air quality index (AQI) is a measure of how polluted the air in a particular region is. Public health risks increase as the AQI increases.

## How is Air Quality Index calculated in India?
The National Air Quality Index considers eight pollutants:
- PM10
- PM2.5
- NO2
- SO2
- CO
- O3
- NH3
- Pb

for which short-term National Ambient Air Quality Standards are prescribed.

Based on the measured ambient concentrations, corresponding standards and likely health impact, a sub-index is calculated for each of these pollutants.

The worst sub-index reflects overall AQI. Likely health impacts for different AQI categories and pollutants have also been suggested, with primary inputs from the medical experts in the group.

## National Air Quality Index Chart
| Category                      | PM10    | PM2.5   | NO2     | O3      | CO      | SO2      | NH3       | Pb      |
|-------------------------------|---------|---------|---------|---------|---------|----------|-----------|---------|
| Good (0-50)                   | 0-50    | 0-30    | 0-40    | 0-50    | 0-1.0   | 0-40     | 0-200     | 0-0.5   |
| Satisfactory (51-100)         | 51-100  | 31-60   | 41-80   | 51-100  | 1.1-2.0 | 41-80    | 201-400   | 0.5-1.0 |
| Moderately Polluted (101-200) | 101-250 | 61-90   | 81-180  | 101-168 | 2.1-10  | 81-380   | 401-800   | 1.1-2.0 |
| Poor (201-300)                | 251-350 | 91-120  | 181-280 | 169-208 | 10-17   | 381-800  | 801-1200  | 2.1-3.0 |
| Very Poor (301-400)           | 351-430 | 121-250 | 281-400 | 209-748 | 17-34   | 801-1600 | 1200-1800 | 3.1-3.5 |
| Severe (401-500)              | 430+    | 250+    | 400+    | 748+    | 34+     | 1600+    | 1800+     | 3.5+    |
