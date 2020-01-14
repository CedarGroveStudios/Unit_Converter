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
`electronics`
================================================================================
electronics 2020-01-13 v0.0 04:30PM
A CircuitPython collection of electronics helpers for calculating:
    Ohm's Law

Part of the CedarGrove Unit_Converter library.

* Author(s): Cedar Grove Studios

Implementation Notes
--------------------
**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/CedarGroveStudios/Converters.git"

# Ohms' Law calculator/converter
def ohms_law(ohms=None, milliamperes=None, volts=None):
    if (None in (ohms, millamperes, volts)):
        raise RuntimeError("Invalid value")

    # Calculate resistance in Ohms
    if (None in (volts, milliamperes)) or (milliamperes == 0):
        raise RuntimeError("Invalid value")
    return volts / (millamperes * 1000)

    # Calculate current in milliamperes (mA)
    if (None in (volts, ohms)) or (ohms == 0):
        raise RuntimeError("Invalid value")
    return volts / ohms

    # Calculate voltage in volts
    if None in (ohms, milliamperes):
        raise RuntimeError("Invalid value")
    return ohms * (milliamperes * 1000)
