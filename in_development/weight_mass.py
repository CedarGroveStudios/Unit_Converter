# The MIT License (MIT)

# Copyright (c) 2019 Cedar Grove Studios

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
`weight_mass`
================================================================================
weight_mass 2020-01-10 v0.0 10:30PM
A CircuitPython class for converting weight/mass units between xx, yy, and zz.
Part of the CedarGrove Converters library.

* Author(s): Cedar Grove Studios

Implementation Notes
--------------------
**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/CedarGroveStudios/Range_Slicer.git"

class ConvertWeightMass:
    """weight_mass helper class."""

    def __init__(self, temperature=None, debug=False):
        # input parameters
        self._deg_c = temperature  # initial temperature in Celsius

        # debug parameters
        self._debug = debug
        if self._debug:
            print("*Init:", self.__class__)
            print("*Init: ", self.__dict__)


    @property
    def deg_c(self):
        """The converter's Celcius value. Default is None."""
        return self._deg_c

    @deg_c.setter
    def deg_c(self, temperature=None):
        self._deg_c = temperature

    @property
    def deg_f(self):
        """The converter's Farenheit value. Default is None."""
        if self._deg_c == None:
            return None
        else:
            return (((9 / 5) * self._deg_c) + 32)  # C to F

    @deg_f.setter
    def deg_f(self, temperature=None):
        self._deg_c = ((temperature - 32) * (5 / 9))  # F to C

    @property
    def deg_k(self):
        """The converter's Kelvin value. Default is None."""
        if self._deg_c == None:
            return None
        else:
            return self._deg_c + 273.15

    @deg_k.setter
    def deg_k(self, temperature=None):
        self._deg_c = temperature - 273.15


    @property
    def debug(self):
        """The class debugging mode. Default is False."""
        return self._debug

    @debug.setter
    def debug(self, debug=False):
        self._debug = debug
        if self._debug:
            print("*Init:", self.__class__)
            print("*Init: ", self.__dict__)
