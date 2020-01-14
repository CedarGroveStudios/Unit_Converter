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
`chronos`
================================================================================
chronos 2020-01-10 v0.0 10:30PM
A CircuitPython collection of time classes for calculating:
    LeapYear: The number of monthdays in February.

    ConvertDST: North American Daylight Saving Time from Standard Time using
    structured time values. Input to this class should always be expressed in
    Standard Time (xST). The value is analyzed and converted to
    Daylight Saving Time (DST) if appropriate.

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
__repo__ = "https://github.com/CedarGroveStudios/Converters.git"

import time

class LeapYear:
    """leap year helper class."""

    def __init__(self, debug=False):

        self._datetime = time.struct_time((0,0,0,0,0,0,0,0,0))
        self._year = 0
        self._leap_flag = False
        self._feb_days = 28

        # debug parameters
        self._debug = debug
        if self._debug:
            print("*Init:", self.__class__)
            print("*Init: ", self.__dict__)

    @property
    def datetime(self):
        """The converter's structure time value. Default is None."""
        return self._datetime

    @datetime.setter
    def datetime(self, datetime=None):
        if datetime == None:
            self._datetime = time.struct_time((2000,1,1,0,0,0,5,1,-1))
        else:
            self._datetime = datetime
            self._datetime.tm_year = self._year

    @property
    def year(self):
        """The converter's year value. Default is None."""
        if self._year == None:
            return None
        else:
            return self._year

    @year.setter
    def year(self, year=None):
        self._year = year
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    self._feb_days = 29  # leap year
                    self._leap_flag = True
                else:
                    self._feb_days = 28  # not leap year
                    self._leap_flag = False
            else:
                self._feb_days = 29      # leap year
                self._leap_flag = True
        else:
            self._feb_days = 28          # not leap year
            self._leap_flag = False

    @property
    def days_feb(self):
        """The number of days in February. Default is 28."""
        return self._feb_days

    @days_feb.setter
    def days_feb(self, days=28):
        self._feb_days = days

    @property
    def leap_year_flag(self):
        """Set to True if a leap year. Default is False."""
        return self._leap_flag

    @leap_year_flag.setter
    def leap_year_flag(self, flag=False):
        self._leap_flag = flag

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

class ConvertDST:
    """Daylight Saving Time (DST) helper class."""

    def __init__(self, debug=False):
        # default date (2000-Jan-1) and is_DST flag values
        self._datetime = time.struct_time((2000,1,1,0,0,0,5,1,-1))
        self._is_dst = False

        # debug parameters
        self._debug = debug
        if self._debug:
            print("*Init: ", self.__class__)
            print("*Init: ", self.__dict__)

    @property
    def date_time(self):
        """The converter's structured time value. Default is None."""
        return self._datetime

    @date_time.setter
    def date_time(self, datetime=None):
        if datetime == None:  # Check for empty datetime input
            raise RuntimeError("Invalid datetime value")
        # Fix structure errors, check if DST, and adjust if needed
        datetime = time.localtime(time.mktime(datetime))
        self._is_dst = self.detect_dst(datetime)
        self._datetime = self.adjust_dst(datetime, self._is_dst)

    @property
    def is_dst(self):
        """The converter's is DST flag value. Default is False."""
        return self._is_dst

    @property
    def debug(self):
        """The class debugging mode. Default is False."""
        return self._debug

    @debug.setter
    def debug(self, debug=False):
        self._debug = debug
        if self._debug:
            print("*Init: ", self.__class__)
            print("*Init: ", self.__dict__)

    def detect_dst(self, datetime):
        # Returns logical flag True if datetime is North American DST;
        #   false if standard time (xST)

        # Preliminary filtering for April to October
        if datetime.tm_mon < 3 or datetime.tm_mon > 11:  # Dec - Feb: Standard
            return False  # xST
        if datetime.tm_mon > 3 and datetime.tm_mon < 11:  # Apr - Oct: DST
            return True   # DST

        # Convert Python time structure Monday-origin to Sunday-origin.
        weekday = (datetime.tm_wday + 1) % 7

        # Get the date of the previous Sunday or today's date if Sunday.
        prev_sunday_date = datetime.tm_mday - weekday

        # March: Second Sunday occurs on the 8th through 14th of the month.
        if datetime.tm_mon == 3:
            if prev_sunday_date <= 7:   # First Sunday of month or before
                return False      # xST
            if prev_sunday_date <= 14:  # Second Sunday of month
                # determine current DST threshold
                dst_thresh = time.mktime(time.struct_time((datetime.tm_year,
                                                           3, prev_sunday_date,
                                                           1, 0, 0, 0, -1, -1)))
                print(time.mktime(datetime), dst_thresh)
                if time.mktime(datetime) < dst_thresh:
                    return False # xST
                return True      # DST

        # November: First Sunday occurs on the 1st through 7th of the month.
        if prev_sunday_date < 1:   # Before first Sunday of month
            return True      # DST
        if prev_sunday_date <= 7:  # First Sunday of month
            # determine current xST threshold
            xst_thresh = time.mktime(time.struct_time((datetime.tm_year,
                                                       11, prev_sunday_date, 1,
                                                       0, 0, 0, -1, -1)))
            if time.mktime(datetime) < xst_thresh:
                return True  # DST
            return False     # xST
        raise RuntimeError("Invalid datetime value")  # should never get here
        return  # Error

    def adjust_dst(self, datetime, is_dst):
        if is_dst:  # Add an hour
            dst_date_time = time.mktime(datetime) + 3600
            return time.localtime(dst_date_time)
        return datetime
