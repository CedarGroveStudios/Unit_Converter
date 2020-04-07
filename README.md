# Unit Converter
 An in-development Cornucopia of CircuitPython Unit Converters
 
 ![Image of Module](https://github.com/CedarGroveStudios/Unit_Converter/blob/master/photos%20and%20graphics/social_wide.png)
 ![WARNING](https://github.com/CedarGroveStudios/Unit_Converter/blob/master/photos%20and%20graphics/WARNING.jpg)

### Angle
### Area
### Chronos (Time)
```python
>>> leap_year(2000)  # Leap Year Determination
True
>>> leap_year(2020)
True
>>> leap_year(2021)
False
>>> leap_year(2024)
True
>>> leap_year(2100)
False
>>> leap_year(2104)
True

```
```python
# Structured Time to DST Converter
# Example code
import time
from cedargrove_unit_converter.chronos import adjust_dst

# Today's date: 11/01/2020 00:00 Standard Time (xST)
datetime = time.struct_time((2020,11,1,0,0,0,6,0,-1))

# Check datetime and adjust if DST
adj_datetime, is_dst = adjust_dst(datetime)

if is_dst:
    flag_text = "DST"
else:
    flag_text = "xST"

# Print the submitted time    
print("     {}/{}/{} {:02}:{:02}:{:02}  week_day={}".format(
      datetime.tm_mon, datetime.tm_mday, datetime.tm_year,
      datetime.tm_hour, datetime.tm_min, datetime.tm_sec,
      datetime.tm_wday))

# Print the adjusted time
print("{}: {}/{}/{} {:02}:{:02}:{:02}  week_day={}".format(flag_text,
      adj_datetime.tm_mon, adj_datetime.tm_mday, adj_datetime.tm_year,
      adj_datetime.tm_hour, adj_datetime.tm_min, adj_datetime.tm_sec,
      adj_datetime.tm_wday))

```
```python
# for 11/1/2020 00:00 xST input; first Sunday of November 01:00 DST
code.py output:
     11/1/2020 00:00:00  week_day=6
DST: 11/1/2020 01:00:00  week_day=6
```
```python
# for 11/1/2020 01:00 xST input; first Sunday of November 02:00 DST
# falls back to 01:00 xST
code.py output:
     11/1/2020 01:00:00  week_day=6
xST: 11/1/2020 01:00:00  week_day=6

```
### Coordinates
### Electronics
```python
>>> ohms_law(ohms=1000, volts=3.3)  # Ohm's Law Calculator
3.3  # current in milliamperes
>>> ohms_law(volts=5, milliamperes=100)
50.0  # resistance in ohms
>>> ohms_law(milliamperes=5, ohms=2000)
10.0  # voltage in volts

```
### Energy
### Frequency
### Length
### Mass/Weight
### Music
### Power
### Pressure
### Speed/Velocity
```python
>>> mps_to_fps(100)        # Meters-Per-Second to Feet-Per-Second Converter
328.1

```
```python
>>> fps_to_mps(328.1)      # Feet-Per-Second to Meters-Per-Second Converter
100.0

```
```python
>>> kmph_to_mph(68)        # Kilometers-Per_Hour to Miles-Per_Hour Converter
42.2552

```
```python
>>> mph_to_kmph(42.2552)   # Miles-Per_Hour to Kilometers-Per_Hour Converter
68.0

```
```python
>>> knots_to_kmph(22)      # Knots to Kilometers-Per-Hour Converter
40.744

```
```python
>>> kmph_to_knots(40.744)  # Kilometers-Per-Hour to Knots Converter
22.0

```
```python
>>> knots_to_mph(22)       # Knots to Miles-Per-Hour Converter
25.322

```
```python
>>> mph_to_knots(25.322)   # Miles-Per-Hour to Knots Converter
22.0

```
### Temperature
```python
>>> celsius_to_fahrenheit(100)  # Celsius to Fahrenheit Converter
212.0
>>> celsius_to_fahrenheit(0) 
32.0

```
```python
>>> fahrenheit_to_celsius(32)   # Fahrenheit to Celsius Converter
0.0
>>> fahrenheit_to_celsius(212)
100.0

```
```python
>>> celsius_to_kelvin(0)        # Celsius to Kelvin Converter
273.15

```
```python
>>> kelvin_to_celsius(273.15)   # Kelvin to Celsius Converter
0.0

```
```python
>>> dew_point(30, 50)           # Dew Point Converter
18.46
>>> dew_point(30, 50, verbose=True)
(18.46, 'Caution: Somewhat uncomfortable for most people.')

```
```python
>>> heat_index(30, 50)          # Heat Index Converter
31.1
>>> heat_index(30, 50, verbose=True)
(31.1, 'Caution: Fatigue is possible with prolonged exposure and activity. 
           Continuing activity could result in heat cramps.')

```
```python
>>> wind_chill(tt, ww)  # Wind Chill Converter (_under development_)
wcwcwcwcwc

```
```python
>>> apparent_temperature(tt, hh, ww)  # Apparent Temperature Converter (_under development_)
atatatatat

```
### Volume


