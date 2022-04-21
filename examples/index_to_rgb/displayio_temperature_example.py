import time
import board
from simpleio import map_range
from temperature_index_to_rgb.iron_spectrum import iron_spectrum as index_to_rgb
import displayio
from adafruit_display_shapes.rect import Rect

# Instantiate display and fonts
print('*** Instantiate the display')

spectrum_group = displayio.Group()
print('show display')

display = board.DISPLAY
display.brightness = 1.0
display.show(spectrum_group)

for index in range(0, 101, 1):
    pos_y = int(round(map_range(index, 0, 100, 240, 0),0))
    pos_x = 0
    color = index_to_rgb(index/100, gamma=0.5)
    print(pos_y, index/100, color)
    slice = Rect(x=pos_x, y=pos_y, width=240, height=3,
                 fill=color, outline=None, stroke=0)
    spectrum_group.append(slice)

while True:
    time.sleep(0.1)
    pass
