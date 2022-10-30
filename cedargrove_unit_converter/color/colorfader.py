# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: MIT
"""
`cedargrove_colorfader`
================================================================================
Adjusts the brightness of a single color value.

* Author(s): JG for Cedar Grove Maker Studios

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  <https://circuitpython.org/downloads>

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/CedarGroveStudios/Unit_Converter.git"


def color_fader(source_color=None, brightness=1.0, gamma=1.0):
    """Scale a 24-bit RGB source color value in proportion to the brightness
    setting (0 to 1.0). Returns an adjusted 24-bit RGB color value or None if
    the source color is None (transparent). The adjusted color's gamma value is
    typically from 0.0 to 2.0 with a default of 1.0 for no gamma adjustment.

    :param int source_color: The color value to be adjusted. Default is None.
    :param float brightness: The brightness value for color value adjustment.
      Value range is 0.0 to 1.0. Default is 1.0 (maximum brightness).
    :param float gamma: The gamma value for color value adjustment. Value range
      is 0.0 to 2.0. Default is 1.0 (no gamma adjustment).

    :return int: The adjusted color value."""

    if source_color is None:
        return source_color

    # Extract primary colors and scale to brightness
    r = min(int(brightness * ((source_color & 0xFF0000) >> 16)), 0xFF)
    g = min(int(brightness * ((source_color & 0x00FF00) >> 8)), 0xFF)
    b = min(int(brightness * ((source_color & 0x0000FF) >> 0)), 0xFF)

    # Adjust result for gamma
    r = min(int(round((r**gamma), 0)), 0xFF)
    g = min(int(round((g**gamma), 0)), 0xFF)
    b = min(int(round((b**gamma), 0)), 0xFF)

    return (r << 16) + (g << 8) + b
