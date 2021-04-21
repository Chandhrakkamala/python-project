import matplotlib.pyplot as plt
import time
from collections import deque
import math

i=0

def sin_gen():
    t=0
    while True:
        val = math.sin(0.1*t)
        yield val
        t+=1
        time.sleep(0.1)

a1 = deque([0]*100)

d=sin_gen()

line, = plt.plot(a1)
plt.ion()
plt.ylim([-1,1])
plt.show()

while True:
    a1.appendleft(next(d))
    datatoplot = a1.pop()
    line.set_ydata(a1)
    plt.draw()
    print (a1[0])
    i += 1
    time.sleep(0.1)
    plt.pause(0.1)