import random
import colorsys
def scale_hue(r, g, b, factor):
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    # Return an rgb color based off of a scaled hue
    # Light and Saturation are constant
    return colorsys.hls_to_rgb(h*factor, 0.54, 0.92)

def barlist(nbr):
    return [random.randint(1, 10) for i in range(1, nbr)]

