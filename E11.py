import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Diode_IV_Temperature.csv")

temperatures = df["T (C)"].unique()

plt.figure(figsize=(8, 6))

for temp in temperatures:
    data = df[df["T (C)"] == temp]

    plt.plot(
        data["V (V)"],
        data["I (mA)"],
        label=f"T = {temp} °C"
    )

plt.xlabel("Voltage V (V)")
plt.ylabel("Current I (mA)")
plt.title("Diode I-V Characteristics at Different Temperatures")
plt.legend()
plt.grid(True)

plt.savefig("E11_diode_characteristics.png", dpi=350)

plt.show()