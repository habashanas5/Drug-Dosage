import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
import math

half_life = 22
plasma_volum = 3000
elimination_constant = -math.log(0.5) / half_life
aspirin_in_plasma = 2*325 * 1000
dt = 0.01
duration = 168
ite = int (duration/dt)
drug_in_system = 0
time = 0
t = []
y = []
interval = 8

for i in range (ite):
time = i * dt
if time % interval == 0:
drug_in_system += 100 * 1000 * 0.12
consintration= drug_in_system / plasma_volum
elimination = drug_in_system * elimination_constant * dt
drug_in_system -= elimination
t.append(time)
y.append(consintration)

plt.plot(t,y)
plt.plot(t,[10 for i in range(ite)])
plt.plot(t,[20 for i in range(ite)])

plt.show()
