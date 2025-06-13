import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Exposure
colors=["#ebae66","#0D95CE","#ED4043"]
widths=[1,1.5,2.2]
i=0
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
plt.figure(figsize=(9,4.5))
ax1=plt.subplot(111)
exposure=pd.read_csv("./Data/Figure_6_Exposure_D2W_Historical.csv").values  # D2W/W2D
meanvals=np.mean(exposure,axis=0)
time_axis = np.arange(0,len(meanvals),1)
plt.plot(time_axis,meanvals,c="grey",linewidth=1.5)
coefficients = np.polyfit(time_axis, meanvals, 1)
fit_line = np.polyval(coefficients, time_axis)
plt.plot(time_axis, fit_line, color="grey", linestyle="--",alpha=0.8)
plt.ylabel("Historical Exposure",size=22)
plt.tick_params(labelsize=20)

ax2=ax1.twinx()
for case in ["SSP1","SSP2","SSP5"]:
    exposure=pd.read_csv("./Data/Figure_6_Exposure_D2W_"+case+".csv").values  #D2W/W2D
    meanvals=np.mean(exposure,axis=0)
    time_axis = np.arange(25,len(meanvals)+25,1)
    plt.plot(time_axis,meanvals,c=colors[i],linewidth=widths[i])

    coefficients = np.polyfit(time_axis, meanvals, 1)
    fit_line = np.polyval(coefficients, time_axis)
    plt.plot(time_axis, fit_line, color=colors[i], linestyle="--",alpha=0.8)
    i+=1
plt.grid(linestyle="--",alpha=0.3)
plt.xticks(np.arange(0,len(meanvals)+25,15),np.arange(1990,2101,15))
plt.ylabel("Future Exposure",size=22)
plt.tick_params(labelsize=20)
plt.show()

 
 # Duration/Severity
 
 def calculate_moving_average(data, window=5):
    moving_avg = np.full_like(data, np.nan, dtype=float)
    for i in range(len(data) - window + 1):
        window_data = data[i:i + window]
        if np.sum(~np.isnan(window_data)) > 0:
            moving_avg[i + window - 1] = np.nanmean(window_data)
    return moving_avg
    
hist=pd.read_csv("./Data/Figure_6_Hist_D2W_D.csv").values   # D2W/W2D  D/S
ssp1=pd.read_csv("./Data/Figure_6_SSP1_D2W_D.csv").values   # D2W/W2D  D/S
ssp2=pd.read_csv("./Data/Figure_6_SSP2_D2W_D.csv").values   # D2W/W2D  D/S
ssp5=pd.read_csv("./Data/Figure_6_SSP5_D2W_D.csv").values   # D2W/W2D  D/S

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
plt.figure(figsize=(9,5.5))

hist_mean=np.nanmean(hist, axis=1)
hist_mean=calculate_moving_average(hist_mean,5)[10:]
q25 = np.nanpercentile(hist, 25, axis=1)
q75 = np.nanpercentile(hist, 75, axis=1)
time_axis = np.arange(0,len(hist_mean),1)
plt.plot(time_axis,hist_mean,c="grey",linewidth=2)
plt.fill_between(time_axis, calculate_moving_average(q25,5)[10:], calculate_moving_average(q75,5)[10:], color='grey', alpha=0.1, 
                     label='25-75 percentile range')

ssp1_mean=np.nanmean(ssp1, axis=1)
ssp1_mean=calculate_moving_average(ssp1_mean,5)[4:]
time_axis = np.arange(len(hist_mean)+1,len(ssp1_mean)+len(hist_mean)+1,1)
q25 = np.nanpercentile(ssp1, 25, axis=1)
q75 = np.nanpercentile(ssp1, 75, axis=1)
plt.plot(time_axis,ssp1_mean,c="#ebae66",linewidth=2)
plt.fill_between(time_axis, calculate_moving_average(q25,5)[4:], calculate_moving_average(q75,5)[4:], color='#ebae66', alpha=0.1, 
                     label='25-75 percentile range')

ssp2_mean=np.nanmean(ssp2, axis=1)
ssp2_mean=calculate_moving_average(ssp2_mean,5)[4:]
q25 = np.nanpercentile(ssp2, 25, axis=1)
q75 = np.nanpercentile(ssp2, 75, axis=1)
plt.plot(time_axis,ssp2_mean,c="#0D95CE",linewidth=2)
plt.fill_between(time_axis, calculate_moving_average(q25,5)[4:], calculate_moving_average(q75,5)[4:], color='#0D95CE', alpha=0.1, 
                     label='25-75 percentile range')

ssp5_mean=np.nanmean(ssp5, axis=1)
ssp5_mean=calculate_moving_average(ssp5_mean,5)[4:]
q25 = np.nanpercentile(ssp5, 25, axis=1)
q75 = np.nanpercentile(ssp5, 75, axis=1)
plt.plot(time_axis,ssp5_mean,c="#ED4043",linewidth=2)
plt.fill_between(time_axis, calculate_moving_average(q25,5)[4:], calculate_moving_average(q75,5)[4:], color='#ED4043', alpha=0.1, 
                     label='25-75 percentile range')

plt.grid(linestyle="--",alpha=0.3)
plt.xticks(np.concatenate([np.arange(0,len(hist_mean),15),np.arange(len(hist_mean)+2,len(ssp1_mean)+len(hist_mean)-3,15)]),
           np.concatenate([np.arange(1960,2015,15),np.arange(2020,2101,15)]))
plt.ylabel("D-W Transition Duration",size=21)
plt.tick_params(labelsize=18)
plt.show()