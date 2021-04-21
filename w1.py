import matplotlib
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt

l = int(input("Enter value of Inductance : "))
c = int(input("Enter value of Capacitance : "))
vo = int(input("Enter value of Vo: "))

w = math.sqrt(1/(l*c))

#i = (vo/(l*w)) * math.sin(w*t)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
k=0
def animate(i, xs, ys):
    global k
    xs.append(dt.datetime.now().strftime('%M:%S.%f'))

    i = (vo/(l*w)) * math.sin(w)
    #print(float(xs[k]))

    # Add x and y to lists
    ys.append(i)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')
    k+=1
# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()