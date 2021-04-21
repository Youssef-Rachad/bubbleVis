import matplotlib.pyplot as plt
from matplotlib import animation
import random
import colorsys

def sort(array):
    for i in range(1, len(array)):
        temp_i = i
        temp_val = array[i]
        while temp_i and (temp_val < array[temp_i-1]):
            array[temp_i] = array[temp_i - 1]
            temp_i = temp_i - 1
        array[temp_i] = temp_val

def scale_hue(r, g, b, factor):
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    # Return an rgb color based off of a scaled hue
    # Light and Saturation are constant
    return colorsys.hls_to_rgb(h*factor, 0.54, 0.92)

def barlist(nbr):
    return [random.randint(1, 10) for i in range(1, nbr)]

fig=plt.figure()

#length of array to sort
nbr = 50
# generate indexes
x=range(1, nbr)
# generate initial values
y=barlist(nbr)
# generate bar graph
barcollection = plt.bar(x, y)
#interval of time between each iteration
delay = 100

def animate(i):
    for i, b in enumerate(barcollection):
        # dynamically set height & color
        b.set_height(y[i])
        b.set_color(scale_hue(245/255, 29/255, 30/255, y[i]/max(y)))
    for i in range(1, len(y)):
        temp_i = i
        temp_val = y[i]
        while temp_i and (temp_val < y[temp_i-1]):
            y[temp_i] = y[temp_i - 1]
            temp_i = temp_i - 1
            break
        y[temp_i] = temp_val

def make_a_gif():
    #number of frames is max iteration (nbr^2) which is bbsort worst case
    anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=(nbr*nbr),interval=delay)

    # uncomment to show in real time
    #plt.show()

    # Make a gif

    # Change the below path
    # note r"" means a raw string --> dont worry about backslashes
    f = r"c://Users/Youssef/insertion.gif"
    writergif = animation.PillowWriter(fps=5)
    anim.save(f, writer=writergif)
