# iron_spectrum_poly.py
# 2021-05-26 version 1.0
# Copyright 2021 Cedar Grove Studios
# Temperature Index to Iron Pseudocolor Spectrum RGB Converter Helper

def index_to_rgb(index=0, gamma=0.5):
    """
    Converts a temperature index to an iron thermographic pseudocolor spectrum
    RGB value. Temperature index in range of 0.0 to 1.0. Gamma in range of
    0.0 to 1.0 (1.0=linear), default 0.5 for color TFT displays.
    :return: Returns a 24-bit RGB value
    :rtype: integer
    """

    band = index * 600  # an arbitrary spectrum band index; 0 to 600

    red = ((1.242e-10 * (band ** 4)) + (1.637e-7 * (band ** 3)) +
          (6.479e-5 * (band ** 2)) - (0.0053 * band) + 0.1002)

    grn = ((-1.093e-10 * (band ** 4)) + (1.138e-7 * (band ** 3)) -
          (2.829e-5 * (band ** 2)) + (0.0012 * band) + 0.0785)

    blu = ((7.986e-8 * (band ** 3)) -
          (6.816e-5 * (band ** 2)) + (0.0134 * band) + 0.2699)

    red = max(min(red, 1.0), 0.0)
    grn = max(min(grn, 1.0), 0.0)
    blu = max(min(blu, 1.0), 0.0)

    return (int(red * 255) << 16) + (int(grn * 255) << 8) + int(blu * 255)
