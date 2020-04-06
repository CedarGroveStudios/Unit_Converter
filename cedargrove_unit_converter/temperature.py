# The MIT License (MIT)

# Copyright (c) 2020 Cedar Grove Studios

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`temperature` - Temperature Converters
================================================================================
A CircuitPython module for temperature conversion.

* Author(s): Cedar Grove Studios
"""

# Celsius to Fahrenheit converter
def celsius_to_fahrenheit(deg_c):
    return (((9 / 5) * deg_c) + 32)

# Fahrenheit to Celsius converter
def fahrenheit_to_celsius(deg_f):
    return ((deg_f - 32) * (5 / 9))

# Celsius to Kelvin converter
def celsius_to_kelvin(deg_c):
    return (deg_c + 273.15)

# Kelvin to Celsius converter
def kelvin_to_celsius(kelvins):
    return (kelvins - 273.15)

# Dew Point converter (degrees Celsius)
def dew_point(deg_c, humidity):
    return (pow(humidity / 100.0, 0.125) * (112.0 + (0.9 * deg_c)) +
            (0.1 * deg_c) - 112.0)

# Heat/Comfort index (degrees Fahrenheit)
def heat_index(deg_c, humidity):
    """ (source: https://en.wikipedia.org/wiki/Heat_index)
    26–32 °C	80–90 °F
        Caution: fatigue is possible with prolonged exposure and activity.
        Continuing activity could result in heat cramps.
    32–41 °C	90–105 °F
    	Extreme caution: heat cramps and heat exhaustion are possible.
        Continuing activity could result in heat stroke.
    41–54 °C	105–130 °F
    	Danger: heat cramps and heat exhaustion are likely; heat stroke is
        probable with continued activity.
    over 54 °C	over 130 °F
    	Extreme danger: heat stroke is imminent.
    """
    t = ((9 / 5) * deg_c) + 32  # dry-bulb temperature in degrees Fahrenheit
    r = humidity                # percentage value between 0 and 100

    # Fahrenheit coefficients
    c = (0, -42.379, 2.04901523, 10.14333127, -0.22475541, -0.00683783,
         -0.05481717, 0.00122874, 0.00085282, -0.00000199)

    # Formula (Fahrenheit method: Schoen 2005)
    h_index_f = c[1] + (c[2] * t) + (c[3] * r) + (c[4] * t * r) +
                (c[5] * t**2) + (c[6] * r**2) + (c[7] * t**2 * r) +
                (c[8] * t * r**2) + (c[9] * t**2 * r**2)
    h_index_c = (h_index_f - 32)*(5/9)  # convert to degrees Celsius

    return h_index_c
