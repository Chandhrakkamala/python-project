import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame

pygame.init()
seconds = 0
clock = pygame.time.Clock()

l = float(input("Enter value of Inductance : "))
c = float(input("Enter value of Capacitance : "))
vo = float(input("Enter value of Vo: "))

w = math.sqrt(1/(l*c))


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
vs = []
k=0
def animate(i, xs, ys,vs):
    global k
    global seconds
    dt = clock.tick()
    s=(2*math.pi)/w
    seconds += dt
    final_sec = (seconds*s)/10000
    xs.append(final_sec)

    i = (-1)*(vo/(l*w)) * math.sin(w*t)
    v= (-1) *vo * math.cos(w*t)
    print(xs[k])
    print(i)


    # Add x and y to lists
    ys.append(i)
    vs.append(v)
    # Limit x and y lists to 20 items
    xs = xs[-50:]
    ys = ys[-50:]
    vs = vs[-50:]
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys , label = "current in the circuit")
    ax.plot(xs, vs , label = "voltage across inductor")
    plt.legend()


    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('LC CIRCUIT')
    #plt.ylabel('Current')
    k+=1

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys , vs), interval=100)
plt.show()