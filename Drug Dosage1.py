import matplotlib.pyplot as plt
import math

# Explicitly entered values for one-compartment model of aspirin
half_life = 3.2  # hours
plasma_volume = 3000  # mL
initial_aspirin_plasma = 2 * 325 * 1000  # μg
elimination_constant = -math.log(0.5) / half_life

# Simulation parameters
dt = 0.01
duration = 8  # 8 hours
iterations = int(duration / dt)
drug_in_system = initial_aspirin_plasma
time = 0
t = []
y = []

for i in range(iterations):
    time = i * dt
    concentration = drug_in_system / plasma_volume
    elimination = elimination_constant * drug_in_system * dt
    drug_in_system -= elimination
    t.append(time)
    y.append(concentration)

# Plotting
plt.plot(t, y, label="Plasma Concentration (μg/mL)")
plt.xlabel("Time (hours)")
plt.ylabel("Concentration (μg/mL)")
plt.title("One-Compartment Model of Aspirin Concentration")
0plt.axhline(y=217, color='r', linestyle='--', label="Safe Therapeutic Level (217 μg/mL)")
plt.legend()
plt.grid(True)
plt.show()
