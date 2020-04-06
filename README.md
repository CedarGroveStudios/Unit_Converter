# Unit Converter
 An in-development Cornucopia of CircuitPython Unit Converters
 
 ![Image of Module](https://github.com/CedarGroveStudios/Unit_Converter/blob/master/photos%20and%20graphics/social_wide.png)

### Angle
### Area
### Chronos (Time)
>##### Leap Year Determination
>>###### leap_year(year)
```python
>>> from cedargrove_unit_converter.chronos import leap_year
>>> leap_year(2000)
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
>>>
```
>##### Structured Time to DST Converter
>>###### adjust_dst(datetime)
```python
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
>##### Ohm's Law Calculator
>>###### ohms_law(ohms, milliamperes, volts)
```python
>>> from cedargrove_unit_converter.electronics import ohms_law
>>> ohms_law(ohms=1000, volts=3.3)
3.3  # current in milliamperes
>>> ohms_law(volts=5, milliamperes=100)
50.0  # resistance in ohms
>>> ohms_law(milliamperes=5, ohms=2000)
10.0  # voltage in volts
>>> 
```
### Energy
### Frequency
### Length
### Mass/Weight
### Music
### Power
### Pressure
### Speed/Velocity
### Temperature
>##### Celsius to Fahrenheit Converter
>>###### celsius_to_fahrenheit(deg_c)
```python
>>> from cedargrove_unit_converter.temperature import celsius_to_fahrenheit
>>> celsius_to_fahrenheit(100)
212.0
>>> celsius_to_fahrenheit(0)
32.0
>>>
```
>##### Fahrenheit to Celsius Converter
>>###### fahrenheit_to_celsius(deg_f)
```python
>>> from cedargrove_unit_converter.temperature import fahrenheit_to_celsius
>>> fahrenheit_to_celsius(32)
0.0
>>> fahrenheit_to_celsius(212)
100.0
>>>
```
>##### Celsius to Kelvin Converter
>>###### celsius_to_kelvin(deg_c)

```python
>>> from cedargrove_unit_converter.temperature import celsius_to_kelvin
>>> celsius_to_kelvin(0)
273.15
>>>
```
>##### Kelvin to Celsius Converter
>>###### kelvin_to_celsius(kelvins)
```python
>>> from cedargrove_unit_converter.temperature import kelvin_to_celsius
>>> kelvin_to_celsius(273.15)
0.0
>>>
```
>##### Dew Point Converter
>>###### dew_point(deg_c, humidity)
```python
>>> from cedargrove_unit_converter.temperature import dew_point
>>> dew_point(30, 50)
18.4635
>>>
```
>##### Heat Index Converter
>>###### heat_index(deg_c, humidity)
```python
>>> from cedargrove_unit_converter.temperature import heat_index
>>> heat_index(27, 40)
26.8632
>>>
```
>##### Wind Chill Converter
>>###### wind_chill(deg_c, wind_vel, humidity)
```python
>>> from cedargrove_unit_converter.temperature import wind_chill
>>> wind_chill(tt, ww, hh)
wcwcwcwcwc
>>>
```
### Volume

