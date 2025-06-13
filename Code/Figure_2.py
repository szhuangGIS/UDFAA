import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./Data/Figure_2_D2W.csv')  # D2W/W2D
df = df.sort_values(by="urbanArea")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
fig, ax = plt.subplots(figsize=(10, 14))
y_pos = range(len(df))
pattern = '/'
density = 4 
d_bars = ax.barh(y_pos, -df['D_Percent'], align='center', 
                 color=np.array([166/255,202/255,236/255]),edgecolor='black', linewidth=1)
d_sig_bars = ax.barh(y_pos, -df['D_Sig_Percent'], align='center',
                     color=np.array([220/255,234/255,247/255]), hatch=pattern,edgecolor='black', linewidth=1)

s_bars = ax.barh(y_pos, df['S_Percent'], align='center',
                 color=np.array([246/255,198/255,173/255]),edgecolor='black', linewidth=1)
s_sig_bars = ax.barh(y_pos, df['S_Sig_Percent'], align='center',
                     color=np.array([251/255,227/255,214/255]), hatch=pattern,edgecolor='black', linewidth=1)
ax.set_yticks(y_pos,df['Clabel'].values)

max_d_percent = df['D_Percent'].max()
ax.grid(True, linestyle='--', alpha=0.7,axis="x")
ax.set_xticks([-1,-0.75,-0.5,-0.25,0,0.25,0.50,0.75,1],["1","0.75","0.50","0.25","0","0.25","0.50","0.75","1"])
ax.set_xlabel('Percentage of Area',size=25)
ax.set_ylabel('City No.',size=25)
ax.set_xlim(-1,1)
ax.axvline(x=0, color='black', linewidth=0.8)
plt.tick_params(labelsize=23)
plt.tight_layout()
plt.show()