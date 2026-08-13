import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("MOSFET_ID_VDS.xlsx")

vgs_values = df["V_GS (V)"].unique()

plt.figure(figsize=(8, 6))

for vgs in vgs_values:
    data = df[df["V_GS (V)"] == vgs]

    vds = data["V_DS (V)"].values
    id = data["I_D (mA)"].values

    gd = np.gradient(id, vds)

    plt.plot(vds, gd, label=f"V_GS = {vgs} V")

plt.xlabel("V_DS (V)")
plt.ylabel("g_d (mS)")
plt.title("MOSFET Output Conductance")
plt.legend()
plt.grid(True)

plt.savefig("E8_output_conductance.png", dpi=300)
plt.show()