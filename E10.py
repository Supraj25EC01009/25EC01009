import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("MOSFET_ID_VGS.csv")

vgs = df["V_GS (V)"]
id = df["I_D (mA)"]

# Select the approximately linear region
mask = (vgs >= 2) & (vgs <= 5)

x = vgs[mask]
y = id[mask]

# Linear fit: ID = m*VGS + c
m, c = np.polyfit(x, y, 1)

# Threshold voltage where ID = 0
vt = -c / m

print("Threshold Voltage (Vt) =", vt, "V")

plt.figure(figsize=(8, 6))
plt.scatter(vgs, id, label="Measured data")
plt.plot(x, m * x + c, label="Linear fit")
plt.axvline(vt, linestyle="--", label=f"Vt = {vt:.2f} V")

plt.xlabel("V_GS (V)")
plt.ylabel("I_D (mA)")
plt.title("MOSFET Threshold Voltage Extraction")
plt.legend()
plt.grid(True)

plt.savefig("E10_threshold_voltage.png", dpi=300)
plt.show()