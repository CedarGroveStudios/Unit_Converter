# SPDX-FileCopyrightText: 2022 Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT
#
# n_color_spectrum_tester.py  2022-04-19 v0.0419  Cedar Grove Studios


import gc
import time
import supervisor
import displayio
from adafruit_display_shapes.rect import Rect

# from cedargrove_unit_converter.index_to_rgb.n_color_spectrum_table import Spectrum
from cedargrove_unit_converter.index_to_rgb.n_color_spectrum import Spectrum
from neko_configuration import Configuration as config
import neko_helpers.cedargrove_display as cedargrove_display

# Instantiate the display and touchscreen
display = cedargrove_display.Display(
    name=config.DISPLAY_NAME,
    calibration=config.CALIBRATION,
    brightness=config.DISPLAY_BRIGHTNESS,
)
ts = display.ts

main_group = displayio.Group()

# Define a few test spectra
#   about 264 colors can be defined per spectrum before the pystack is exhausted
#   first color will blend with last color unless mode = "light"
#
# Color definitions are from:
#  https://en.wikipedia.org/wiki/List_of_colors:_A–F
#  https://en.wikipedia.org/wiki/List_of_colors:_G–M
#  https://en.wikipedia.org/wiki/List_of_colors:_N–Z

VISIBLE = [
    # Newtonian primay colors
    0xFF0000,  # Red
    0xFF7F00,  # Orange
    0xFFFF00,  # Yellow
    0x00FF00,  # Green
    0x0000FF,  # Blue
    0x4B0082,  # Indigo
    0x300040,  # Violet
]

IRON = [
    0x202040,  # Dark Gray (coolest)
    0x0000FF,  # Blue
    0xA000FF,  # Violet
    0xFF0000,  # Red
    0xFF8000,  # Orange
    # 0xFFFF00,  # Yellow (optional)
    0xFFFFFF,  # White (warmest)
]

FALSE_THERMO = [
    0x202040,  # Dark Gray (coolest)
    0x0000FF,  # Blue
    0x00FF00,  # Green
    0xFFFF00,  # Yellow
    0xFF7F00,  # Orange
    0xFF0000,  # Red
    0xFF00FF,  # Magenta (warmest)
]

STOPLIGHT = [
    0xFF0000,  # Red
    0xFFFF00,  # Yellow
    0x00FF00,  # Green
]

GAMMA = 0.80  # 0.45 to 0.80 is best for TFT display

# Instantiate the color spectrum
gc.collect()
m0 = gc.mem_free()
tt0 = supervisor.ticks_ms()
spectrum = Spectrum(VISIBLE, mode="light", gamma=GAMMA)
print(
    f"initialize: {(supervisor.ticks_ms() - tt0)/1000:6.3f} msec  memory used: {m0 - gc.mem_free()} bytes"
)

neo_brightness = config.DISPLAY_BRIGHTNESS / 5

width_of_band = 2
granularity = display.width / width_of_band

# Define displayio rectangles
for i in range(granularity):
    color = 0x808080
    band = Rect(
        x=int(display.width / granularity * i),
        y=0,
        width=width_of_band,
        height=display.height // 2,
        fill=color,
    )
    main_group.append(band)

display.show(main_group)

# This does something wierd and reduces the benchmark execution time
#   significantly just for the table version; don't know why
# spectrum.gamma = 0.55

# Perform a 1000 count benchmark
tt0 = supervisor.ticks_ms()
for i in range(1001):
    color = spectrum.color(0.5)
print(f"benchmark: {(supervisor.ticks_ms() - tt0)/1000:6.3f} msec")

while True:
    # print(f"mode: {spectrum.mode}  gamma: {spectrum.gamma:3.1f}")
    for i in range(granularity):
        color = spectrum.color(i / granularity)
        main_group[i].fill = color

    time.sleep(3)
