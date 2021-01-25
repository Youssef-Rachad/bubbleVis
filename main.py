import matplotlib.pyplot as plt
from matplotlib import animation
import random
import colorsys

def scale_hue(r, g, b, factor):
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return colorsys.hls_to_rgb(h*factor, 0.54, 0.92)

def barlist(): 
    return [random.randint(1, 10) for i in range(1, 10)]

colors=[]
fig=plt.figure()

n=100 #Number of frames
x=range(1, 10)
barcollection = plt.bar(x,barlist())

def animate(i):
    y=barlist()
    for i, b in enumerate(barcollection):
        b.set_height(y[i])
        #b.set_color((0.1*y[i], 0.1*y[i], 0.1*y[i]))
        b.set_color(scale_hue(245/255, 29/255, 30/255, y[i]/max(y)))

anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=n,
                             interval=250)

plt.show()
