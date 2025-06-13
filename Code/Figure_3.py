import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_csv('./Data/Figure_3_D2W.csv') #  D2W/W2D
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
plt.figure(figsize=(16, 10))

base_size = 1500
sizes = df['Both_Worse'] * base_size

scatter = plt.scatter(
    x=df['Duration_Worse'],
    y=df['Severity_Worse'],
    s=sizes,
    alpha=0.7,
    c=df['Both_Worse'],
    cmap='RdYlBu_r',
    edgecolors='black',
    linewidth=0.5,
    zorder=10
)

sorted_df = df.sort_values('Both_Worse', ascending=False)

plt.gca().xaxis.set_major_formatter(PercentFormatter(1.0))
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))
cbar = plt.colorbar(scatter, pad=0.02)
cbar.ax.yaxis.set_major_formatter(PercentFormatter(1.0))
cbar.ax.tick_params(labelsize=20)

plt.axvline(x=0.5, color='gray', linestyle='--', linewidth=1, alpha=0.7, label='x = 50%')
plt.axhline(y=0.5, color='gray', linestyle='--', linewidth=1, alpha=0.7, label='y = 50%')
plt.axvspan(xmin=0.5, xmax=1.0, ymin=0.287, ymax=1.0, color='lightcoral', alpha=0.2)

plt.tick_params(labelsize=20)
plt.grid(True, linestyle='--', alpha=0.4)
plt.xlim(0.1, 1.0)
plt.ylim(0.3, 1.0)
plt.tight_layout()
plt.show()