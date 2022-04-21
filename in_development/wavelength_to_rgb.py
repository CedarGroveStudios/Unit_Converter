# light wavelength to rgb converter
# Based on original 1996 Fortran code by Dan Bruton:
#   physics.sfasu.edu/astro/color/spectra.html

def wavelength_to_rgb(wavelength, gamma=0.8, depth=255):
    """Convert wavelength to RGB value. Wavelength in nanometers in range of
    380nm to 780nm (violet --> red). Gamma in range of 0 to 1.0 (1.0=linear),
    default 0.8 (typical). Intensity falls off near vision limits.
    Returns an RGB tuple, default 8-bit depth."""

    wl = wavelength
    red = 0.0
    grn = 0.0
    blu = 0.0

    if wl >= 380 and wl < 440:
        intensity = 0.3 + (0.7 * (wl - 380) / (440 - 380))
        red = ((-1.0 * (wl - 440) / (440 - 380)) * intensity) ** gamma
        grn = 0.0
        blu = (1.0 * intensity) ** gamma
    if wl >= 440 and wl < 490:
        red = 0.0
        grn = (1.0 * (wl - 440) / (490 - 440)) ** gamma
        blu = 1.0 ** gamma
    if wl >= 490 and wl < 510:
        red = 0.0
        grn = 1.0 ** gamma
        blu = (-1.0 * (wl - 510) / (510 - 490)) ** gamma
    if wl >= 510 and wl < 580:
        red = (1.0 * (wl - 510) / (580 - 510)) ** gamma
        grn = 1.0 ** gamma
        blu = 0.0
    if wl >= 580 and wl < 645:
        red = 1.0 ** gamma
        grn = (-1.0 * (wl - 645) / (645 - 580)) ** gamma
        blu = 0.0
    if wl >= 645 and wl <= 780:
        intensity = 0.3 + (0.7 * (780 - wl) / (780 - 645))
        red = (1.0 * intensity) ** gamma
        grn = 0.0
        blu = 0.0

    return (int(red * depth), int(grn * depth), int(blu * depth))
