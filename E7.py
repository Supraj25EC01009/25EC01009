import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("MOSFET_ID_VDS.xlsx")

vgs_values = df["V_GS (V)"].unique()

plt.figure(figsize=(8, 6))

for vgs in vgs_values:
    data = df[df["V_GS (V)"] == vgs]
    plt.plot(data["V_DS (V)"], data["I_D (mA)"], label=f"V_GS = {vgs} V")

plt.xlabel("V_DS (V)")
plt.ylabel("I_D (mA)")
plt.title("MOSFET Output Characteristics")
plt.legend()
plt.grid(True)

plt.savefig("E7_output_characteristics.png", dpi=300)
plt.show()