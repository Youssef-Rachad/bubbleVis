import matplotlib.pyplot as plt
from matplotlib import animation
import random
import colorsys

def sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def scale_hue(r, g, b, factor):
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    # Return an rgb color based off of a scaled hue
    # Light and Saturation are constant
    return colorsys.hls_to_rgb(h*factor, 0.54, 0.92)

def barlist(nbr):
    return [random.randint(1, 10) for i in range(1, nbr)]

fig=plt.figure()
#length of array to sort
nbr = 20
# generate indexes
x=range(1, nbr)
# generate initial values
y=barlist(nbr)
# generate bar graph
barcollection = plt.bar(x, y)
#interval of time between each iteration
delay = 10

def animate(i):
    for i, b in enumerate(barcollection):
        # dynamically set height & color
        b.set_height(y[i])
        b.set_color(scale_hue(245/255, 29/255, 30/255, y[i]/max(y)))
    # if out of order, then swap
    for j in range(len(y)-1):
        if y[j] > y[j+1]:
            y[j], y[j+1] = y[j+1], y[j]
            # break to get one step at a time
            break
def make_a_gif():
    #number of frames is max iteration (nbr^2) which is bbsort worst case
    anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=(nbr*nbr),interval=delay)
    # uncomment to show in real time
    #plt.show()

    # Make a gif

    # Change the below path
    # note r"" means a raw string --> dont worry about backslashes
    f = r"c://path/to/file.gif"
    #f = r"c://Users/Youssef/code/python/bubbleVis/hm.gif"
    writergif = animation.PillowWriter(fps=5)
    anim.save(f, writer=writergif)

