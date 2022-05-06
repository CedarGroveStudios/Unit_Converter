import time
import board
from simpleio import map_range
from index_to_rgb import visible_spectrum as index_to_rgb
import displayio
from adafruit_display_shapes.rect import Rect

# Instantiate display and fonts
print("*** Instantiate the display")

spectrum_group = displayio.Group()
print("show display")

display = board.DISPLAY
display.brightness = 1.0
display.show(spectrum_group)

for lmda in range(380, 780, 4):
    pos_x = int(round(map_range(lmda, 380, 780, 0, 240), 0))
    # print(lmda, pos_x)
    pos_y = 0
    color = index_to_rgb(lmda)
    slice = Rect(
        x=pos_x, y=pos_y, width=3, height=240, fill=color, outline=None, stroke=0
    )
    spectrum_group.append(slice)

while True:
    time.sleep(0.1)
    pass
