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

def merge_sort(array):
    if len(array) <= 1:
        return array
    right = []
    left = []
    middle = len(array)//2
    for i in range(0, middle):
        left.append(array[i])
    for i in range(middle, len(array)):
        right.append(array[i])
    right = merge_sort(right)
    left = merge_sort(left)
    yield  merge_arrays(left, right)


def merge_arrays(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    result.extend(left)
    result.extend(right)
    yield result

fig=plt.figure()

#length of array to sort
nbr = 10
# generate indexes
x=range(1, nbr)
# generate initial values
y=outils.barlist(nbr)
# generate bar graph
barcollection = plt.bar(x, y)
#interval of time between each iteration
delay = 100

def animate(arr):
    for i, b in enumerate(barcollection):
        # dynamically set height & color
        b.set_height(arr[i])
        b.set_color(outils.scale_hue(245/255, 29/255, 30/255, arr[i]/max(arr)))

def make_a_gif():
    generator = merge_sort(y)
    #number of frames is max iteration (nbr^2) which is bbsort worst case
    anim=animation.FuncAnimation(fig,animate,frames=generator,repeat=True,blit=False,interval=delay)

    # uncomment to show in real time
    #plt.show()

    # Make a gif

    # Change the below path
    # note r"" means a raw string --> dont worry about backslashes
    f = r"c://Users/Youssef/insertion.gif"
    writergif = animation.PillowWriter(fps=5)
    anim.save(f, writer=writergif)

make_a_gif();

