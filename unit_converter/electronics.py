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
`electronics` - Electronics Converters and Calculators
================================================================================
A CircuitPython module for electronics converters and calculators.

* Author(s): Cedar Grove Studios
"""

# Ohms' Law calculator/converter
def ohms_law(ohms, milliamperes, volts):

    # Calculate resistance in Ohms
    if (None in (volts, milliamperes)):
        raise ValueError("Volts and current values required.")
    return volts / (millamperes * 1000)

    # Calculate current in milliamperes (mA)
    if (None in (volts, ohms)):
        raise ValueError("Resistance and voltage values required.")
    return volts / ohms

    # Calculate voltage in volts
    if None in (ohms, milliamperes):
        raise ValueError("Resistance and current values required.")
    return ohms * (milliamperes * 1000)
