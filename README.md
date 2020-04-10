# Unit Converter
 An in-development Cornucopia of CircuitPython Unit Converters and maybe a few Constants.

 ![Image of Module](https://github.com/CedarGroveStudios/Unit_Converter/blob/master/photos%20and%20graphics/social_wide.png)
 ![WARNING](https://github.com/CedarGroveStudios/Unit_Converter/blob/master/photos%20and%20graphics/WARNING.jpg)

#### Acoustics
#### Angle
#### Area
#### [Chronos (Time)](https://github.com/CedarGroveStudios/Unit_Converter/blob/master/docs/pseudo_readthedocs_chronos.pdf)
>##### Leap Year
>##### Automatic Daylight Saving Time
#### Coordinates
#### [Electronics](https://github.com/CedarGroveStudios/Unit_Converter/blob/master/docs/pseudo_readthedocs_electronics.pdf)
>##### Ohm's Law
#### Energy
#### Length
#### Mass/Weight
#### Music
>##### [MIDI](https://github.com/CedarGroveStudios/Unit_Converter/blob/master/docs/pseudo_readthedocs_music_MIDI.pdf)
>>##### Note Or Note Name
>>##### Note to Note Name
>>##### Note Name to Note
>>##### Note to Frequency
>>##### Frequency to Note
>>##### Decode Control Change Code
#### Power
#### Pressure
#### RF Communications
#### [Speed/Velocity](https://github.com/CedarGroveStudios/Unit_Converter/blob/master/docs/pseudo_readthedocs_velocity.pdf)
>##### Meters-Per-Second to Feet-Per-Second
>##### Feet-Per-Second to Meters-Per-Second
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
#### [Temperature](https://github.com/CedarGroveStudios/Unit_Converter/blob/master/docs/pseudo_readthedocs_temperature.pdf)
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
#### Volume
