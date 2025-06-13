import numpy as np
import pandas as pd
from osgeo import gdal
import matplotlib.pyplot as plt
from matplotlib import rcParams


bths=pd.read_csv("./Data/Figure_4_BTH.csv")
prbs=pd.read_csv("./Data/Figure_4_PRB.csv")
yrds=pd.read_csv("./Data/Figure_4_YRD.csv")
cases=["D2W_D","W2D_D","D2W_S","W2D_S"]
colors=["#ebae66","#0D95CE","#ED4043"]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
plt.figure(figsize=(10,18))
for p in range(1,5,1):
    case=cases[p-1]
    bth=bths[case].values
    prb=prbs[case].values
    yrd=yrds[case].values
    bth=bth[np.isnan(bth)==False]
    prb=prb[np.isnan(prb)==False]
    yrd=yrd[np.isnan(yrd)==False]
    
    ax1=plt.subplot(2,2,p)
    bp=plt.boxplot([yrd,prb,bth],positions=[1,2,3],showfliers=False,patch_artist=True,whiskerprops={'linestyle':'--','linewidth':2},
                    boxprops={'facecolor':'none'},widths=0.3,showmeans=True,vert=False,meanprops=dict(marker='o', markerfacecolor='violet', markeredgecolor='violet'))
    for i in range(len(bp['boxes'])):
        bp['boxes'][i].set(edgecolor=colors[i])
        bp['boxes'][i].set(linewidth=3)
        bp['medians'][i].set(color=colors[i])
        bp['medians'][i].set(linewidth=3)  
    tnum=0
    for i in range(0,len(bp['whiskers']),2):
        bp['whiskers'][i].set(color=colors[tnum])
        bp['whiskers'][i].set(linewidth=3)
        bp['whiskers'][i+1].set(color=colors[tnum])
        bp['whiskers'][i+1].set(linewidth=3)
        bp['caps'][i].set(color=colors[tnum])
        bp['caps'][i+1].set(color=colors[tnum])
        bp['caps'][i].set(linewidth=3)
        bp['caps'][i+1].set(linewidth=3)
        tnum=tnum+1
    
    plt.yticks([1,2,3],["YRD","PRB","BTH"])
    plt.axvline(x=0, color='red', linestyle='dashed',linewidth=2)
    plt.tick_params(labelsize=18)
    plt.xlabel("Change Rate",size=19)
    plt.grid(linestyle="--",alpha=0.3,axis="x")
plt.show()