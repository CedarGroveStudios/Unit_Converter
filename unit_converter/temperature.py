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
`temperature`
================================================================================
temperature 2020-01-13 v0.0 04:30PM
A CircuitPython class for converting temperature measurement units between
degrees Fahrenheit and degrees Celsius.

* Author(s): Cedar Grove Studios

Implementation Notes
--------------------
**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/CedarGroveStudios/unit_converter.git"

# Celsius to Fahrenheit converter
def celsius_to_fahrenheit(deg_c=None):
    if deg_c == None:
        raise RuntimeError("Invalid value")
    return (((9 / 5) * deg_c) + 32)

# Fahrenheit to Celsius converter
def fahrenheit_to_celsius(deg_f=None):
    if deg_f == None:
        raise RuntimeError("Invalid value")
    return ((deg_f - 32) * (5 / 9))
