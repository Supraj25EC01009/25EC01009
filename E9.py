import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("MOSFET_ID_VGS.csv")

vds_values = df["V_DS (V)"].unique()

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

for vds in vds_values:
    data = df[df["V_DS (V)"] == vds].copy()

    vgs = data["V_GS (V)"].values
    id = data["I_D (mA)"].values

    gm = np.gradient(id, vgs)

    ax[0].plot(vgs, id, label=f"V_DS = {vds} V")
    ax[1].plot(vgs, gm, label=f"V_DS = {vds} V")

    peak_index = np.argmax(gm)

    if gm[peak_index] > 0:
        ax[1].scatter(vgs[peak_index], gm[peak_index])
        ax[1].annotate(
            f"Peak gm = {gm[peak_index]:.2f} mS\nV_GS = {vgs[peak_index]:.2f} V",
            (vgs[peak_index], gm[peak_index])
        )

        print(
            f"V_DS = {vds} V : "
            f"Peak gm = {gm[peak_index]:.2f} mS, "
            f"V_GS = {vgs[peak_index]:.2f} V"
        )

ax[0].set_xlabel("V_GS (V)")
ax[0].set_ylabel("I_D (mA)")
ax[0].set_title("MOSFET Transfer Characteristics")
ax[0].legend()
ax[0].grid(True)

ax[1].set_xlabel("V_GS (V)")
ax[1].set_ylabel("g_m (mS)")
ax[1].set_title("MOSFET Transconductance")
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()

plt.savefig("E9_transconductance.png", dpi=350)
plt.show()