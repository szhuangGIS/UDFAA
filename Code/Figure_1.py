import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Latitude Pattern
df = pd.read_csv('../Data/Figure_1_UE.csv')
metrics=["DW_D_UE","DW_S_UE","WD_D_UE","WD_S_UE"]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
plt.figure(figsize=(12, 8))
plt.subplots_adjust(wspace=0.5)
for p in range(1,5,1):
    plt.subplot(1,4,p) 
    lat_bins = list(range(18, 49,1))
    lat_centers = lat_bins[:-1]
    avg_values = []
    percentile_25 = []
    percentile_75 = []
    
    for i in range(len(lat_bins)-1):
        mask = (df['Lat'] >= lat_bins[i]) & (df['Lat'] < lat_bins[i+1])
        data = df.loc[mask, metrics[p-1]]
        avg=data.mean()
        p25 = data.quantile(0.25)
        p75 = data.quantile(0.75)
        
        avg_values.append(avg)
        percentile_25.append(p25)
        percentile_75.append(p75)
     
    plt.fill_betweenx(lat_centers, percentile_25, percentile_75, 
                     alpha=0.3, color='lightblue', 
                     label='25-75 Percentile Range')
    plt.plot(avg_values,lat_centers, 'b-', 
             linewidth=2, marker='o', markersize=6,
             label='Mean Value')
    plt.ylabel('Latitude (°)', fontsize=14)
    plt.xlabel('UE', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.yticks(lat_centers[0:-1:2], rotation=0)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.grid(True, linestyle='--', alpha=0.6, which='both')
    x_min = min(percentile_25) * 1.1
    x_max = max(percentile_75) * 1.1
    plt.xlim(x_min, x_max)
    plt.ylim(17, 48)
    plt.axvline(x=0,c="orange",linestyle="--")
plt.show()

# Climate
ues=pd.read_csv("./Data/Figure_1_UE.csv")
matchIDs=pd.read_csv("./Data/Figure_1_Climate.csv")
dwd,dws,wdd,wds=[],[],[],[]
for climate in range(1,8,1):
    cids=matchIDs[matchIDs.CID==climate]["CityID"].values
    dwd.append(np.mean(ues[ues["ID"].isin(cids)]["DW_D_UE"].values))
    dws.append(np.mean(ues[ues["ID"].isin(cids)]["DW_S_UE"].values))
    wdd.append(np.mean(ues[ues["ID"].isin(cids)]["WD_D_UE"].values))
    wds.append(np.mean(ues[ues["ID"].isin(cids)]["WD_S_UE"].values))

c1=np.array([220/255,234/255,247/255])
c2=np.array([166/255,202/255,236/255])
c3=np.array([251/255,227/255,214/255])
c4=np.array([246/255,198/255,173/255])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
plt.figure(figsize=(13, 4))
ax1=plt.subplot(111)
plt.bar(np.arange(1,8,1),dwd,color=c1)
plt.bar(np.arange(1,8,1),wdd,width=0.5,color=c2)
plt.ylim(-0.030,0)
plt.tick_params(labelsize=15)
plt.ylabel("UE of Transition Duration",size=16)
plt.xticks(np.arange(1,15,1),["C1","C2","C3","C4","C5","C6","C7","C1","C2","C3","C4","C5","C6","C7"])
ax2=ax1.twinx()
plt.bar(np.arange(8,15,1),dws,color=c3)
plt.bar(np.arange(8,15,1),wds,width=0.5,color=c4)
plt.xlim(0.5,14.5)
plt.tick_params(labelsize=15)
plt.ylabel("UE of  Severity",size=16)
plt.show()

# Basin
matchIDs=pd.read_csv("./Data/Figure_1_Basin.csv")
ues=pd.read_csv("./Data/Figure_1_UE.csv")
dwd,dws,wdd,wds=[],[],[],[]
for basin in range(1,10,1):
    cids=matchIDs[matchIDs.BID==basin]["CityID"].values
    dwd.append(np.mean(ues[ues["ID"].isin(cids)]["DW_D_UE"].values))
    dws.append(np.mean(ues[ues["ID"].isin(cids)]["DW_S_UE"].values))
    wdd.append(np.mean(ues[ues["ID"].isin(cids)]["WD_D_UE"].values))
    wds.append(np.mean(ues[ues["ID"].isin(cids)]["WD_S_UE"].values))

c1=np.array([220/255,234/255,247/255])
c2=np.array([166/255,202/255,236/255])
c3=np.array([251/255,227/255,214/255])
c4=np.array([246/255,198/255,173/255])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
plt.figure(figsize=(13, 4))
ax1=plt.subplot(111)
plt.bar(np.arange(1,10,1),dwd,color=c1)
plt.bar(np.arange(1,10,1),wdd,width=0.5,color=c2)
plt.ylim(-0.030,0)
plt.tick_params(labelsize=15)
plt.ylabel("UE of Transition Duration",size=16)

ax2=ax1.twinx()
plt.bar(np.arange(10,19,1),dws,color=c3)
plt.bar(np.arange(10,19,1),wds,width=0.5,color=c4)
plt.xlim(0.5,18.5)
plt.tick_params(labelsize=15)
plt.ylabel("UE of Severity",size=16)
plt.xticks(np.arange(1,19,1),["B1","B2","B3","B4","B5","B6","B7","B8","B9",
                             "B1","B2","B3","B4","B5","B6","B7","B8","B9"])
plt.show()