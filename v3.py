import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

master = tk.Tk()

tk.Label(master, text="Value of Inductance").grid(row=0)
tk.Label(master, text="Value of Capacitance").grid(row=1)
tk.Label(master, text="Value of Vo").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

def executeThis():
    l = float(e1.get())
    c = float(e2.get())
    v = float(e3.get())
    w = np.sqrt(1/(l*c))
    p=(2*np.pi)/w
    t = np.arange(0,(3*p),p/100)
    d= (v/(w*l)) * np.sin(w*t)
    vc= v * np.cos(w*t)

    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.plot(t, d , label = "current in the circuit")
    plt.plot(t, vc , label = "voltage across inductor")
    plt.legend()
    plt.show()

button1 = tk.Button(text='Enter', command=executeThis)
button1.grid(row=4, column=1)

master.mainloop()
