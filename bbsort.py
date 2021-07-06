import matplotlib.pyplot as plt
from matplotlib import animation

import outils

def sort(array):
    #print(array)
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            #print(array)
            yield array

fig = plt.figure()
nbr = 10                      # length of array to sort
x = range(1, nbr)             # generate indexes
y = outils.barlist(nbr)       # generate initial values
barcollection = plt.bar(x, y) # generate bar graph
delay = 10                    # interval of time between each iteration
generator = sort(y)           # function to sort incrementally

def animate(i):
    for i, b in enumerate(barcollection):
        b.set_height(y[i]) # dynamically set height & color
        b.set_color(outils.scale_hue(245/255, 29/255, 30/255, y[i]/max(y)))

def make_a_gif(file):
    anim=animation.FuncAnimation(fig, animate, repeat=True, blit=False, frames=generator, interval=delay)
    #plt.show() # uncomment to show in real time
    #f = r"c://Path/to/file.gif"
    f = fr'c://Users/Youssef/code/python/bubbleVis/{file}.gif'
    writergif = animation.PillowWriter(fps=5)
    anim.save(f, writer=writergif)

