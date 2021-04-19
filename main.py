import matplotlib.pyplot as plt
from matplotlib import animation
import random
import colorsys

def scale_hue(r, g, b, factor):
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return colorsys.hls_to_rgb(h*factor, 0.54, 0.92)

def barlist(nbr):
    return [random.randint(1, 10) for i in range(1, nbr)]

colors=[]
fig=plt.figure()

n=1 #Number of frames
#length of array to sort
nbr = 50
x=range(1, nbr)
barcollection = plt.bar(x,barlist(nbr))
y=barlist(nbr)
#interval of time between each iteration
delay = 250

def animate(i):
    for i, b in enumerate(barcollection):
        b.set_height(y[i])
        b.set_color(scale_hue(245/255, 29/255, 30/255, y[i]/max(y)))
    for j in range(len(y)-1):
        if y[j] > y[j+1]:
            y[j], y[j+1] = y[j+1], y[j]
            break
    return

anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=n,
        interval=delay)

plt.show()

