import numpy as np
import tidynamics
import matplotlib.pyplot as plt
import pandas as pd

data2 = pd.read_csv('Subject_2_data.csv').reset_index(drop = True)#read data from Subject_2_data.csv

activity_list = data2['activity'].unique()#contains the name of activities

fig3 = plt.figure(figsize=(17,17),facecolor='indigo')# Define a figure with size 17 by 17

gs = fig3.add_gridspec(9, 6,wspace=0.35, hspace=1)#9 rows and 6 columns for subplots under main plot
#add_gridspec() allows marging columns and rows of subplots under main plot

#variables for controlling looping through columns and rows of plots
#str and endr control looping through rows
#stc and endc control looping through columns
str = 0
endr = 0
stc = 0
endc = 0

X = np.arange(3)#variable for controlling x ticks of bar plot
fig3 = plt.figure(figsize=(17,17),facecolor='darkslategrey')# Define a figure with size 17 by 17
gs = fig3.add_gridspec(9, 6,wspace=0.35, hspace=1)# divides the main plot into 9 rows and 6 columns (54 cells) 
#add_gridspec() allows marging columns and rows of subplots under main plot

#variables for controlling looping through columns and rows of plots
#str and endr control looping through rows
#stc and endc control looping through columns
str = 0
endr = 0
stc = 0
endc = 0

X = np.arange(3)#variable for controlling x ticks of bar plot

#plt.rcParams.update({'font.size': 12, 'text.color': 'white'})
for i in range(0,6):#looping through six activity types
    #main1, main2, main3 contains 500 rows of accelerometer x, y and z respectiviely for each activity 
    main1 = data2[data2['activity']== activity_list[i]].iloc[2000:2500,1].reset_index(drop =True)
    main2 = data2[data2['activity']== activity_list[i]].iloc[2000:2500,2].reset_index(drop =True)
    main3 = data2[data2['activity']== activity_list[i]].iloc[2000:2500,3].reset_index(drop =True)
    #Calculating autocorrelation of each axis with itself for certai activity type and storing them
    acf_acc_x = tidynamics.acf(main1)
    acf_acc_y = tidynamics.acf(main2)
    acf_acc_z = tidynamics.acf(main3)
    
    #f3_ax1 will a subplot containing places of 4 cells (2 rows by 2 columns)
    f3_ax1 = fig3.add_subplot(gs[str:endr+2, stc:endc+2]) 
    f3_ax1.set_title('Tri-axial Accelerometer Autocorrelation', color = 'white', fontsize = 12, fontweight = 'bold')
    
    #Scatter plot of the autocorrelation values for all 500 lags
    f3_ax1.scatter(np.arange(500),acf_acc_x, label='linear', c = 'limegreen')
    f3_ax1.scatter(np.arange(500),acf_acc_y, label='linear', c = 'crimson')
    f3_ax1.scatter(np.arange(500),acf_acc_z, label='linear', c = 'aqua')
    f3_ax1.set_xlabel('Number of Lags', color = 'white', fontsize = 12, fontweight = 'bold')
    f3_ax1.tick_params(axis='y', colors='white')
    f3_ax1.tick_params(axis='x', colors='white')
    
    #f3_ax2 will a subplot containing places of 2 cells (2 rows by 1 column)
    f3_ax2 = fig3.add_subplot(gs[str:endr+2, endc+2])
    f3_ax2.set_title('Autocorrelation Comparison', color = 'white', fontsize = 12, fontweight = 'bold')
    
    #bar plot showing the maximum auctocorrelation found for each axis over each activity type
    f3_ax2.bar(X[0] + 0.00,acf_acc_x.max(),0.5, hatch = 'o', color = 'limegreen')
    f3_ax2.bar(X[1] + 0.00,acf_acc_y.max(),0.5, hatch = 'x', color = 'crimson')
    f3_ax2.bar(X[2] + 0.00,acf_acc_z.max(),0.5, hatch = '/', color = 'aqua')
    f3_ax2.set_xticks(np.arange(3))    # This ensures we have one tick per axis
    f3_ax2.set_xticklabels(['Acc_X', 'Acc_Y', 'Acc_Z'],c = 'white',fontweight = 'bold', fontsize = 12)
    f3_ax2.tick_params(axis='y', colors='white')
    
    #f3_ax3 will a subplot containing places of 3 cells (1 row by 3 columns)
    f3_ax3 = fig3.add_subplot(gs[endr+2, stc:endc+3])
    f3_ax3.set_title('Pattern in Accelerometer data', color = 'white', fontsize = 12, fontweight = 'bold')
    f3_ax3.set_xlabel('Accelerometer X, Y, Z', color = 'white', fontsize = 12, fontweight = 'bold')
    
    #Line plot showing the raw values of three axis for each activity type
    f3_ax3.plot(main1, c = 'orange')
    f3_ax3.plot(main2, c = 'green')
    f3_ax3.plot(main3, c = 'blue')
    f3_ax3.set_ylabel("Value in m/s^2", color = 'white')
    f3_ax3.tick_params(axis='y', colors='white')
    f3_ax3.tick_params(axis='x', colors='white')
    
    #conditions for incrementing the row and columns controller variables
    if(i%2 == 0):
        stc = stc+3
        endc = endc+ 3
    else:
        str = str+3
        endr = endr+3
        stc = 0
        endc = 0


#Create custom legend with colors
from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color='limegreen', lw=4),
                Line2D([0], [0], color='crimson', lw=4),
                Line2D([0], [0], color='aqua', lw=4)]
#Legend denoting the axes in scatter plot autocorrelation
legend1 = fig3.legend(custom_lines, ['Acc_X_acf', 'Acc_Y_acf', 'Acc_Z_acf'], facecolor = 'maroon', loc = 'upper left', bbox_to_anchor=(0.2, 0.92), ncol = 3)
custom_lines = [Line2D([0], [0], color='orange', lw=4),
                Line2D([0], [0], color='green', lw=4),
                Line2D([0], [0], color='blue', lw=4)]
#legend denoting the axes of raw signals
legend2 = fig3.legend( custom_lines, ['Acc_X_signal', 'Acc_Y_signal', 'Acc_Z_signal'],facecolor = 'maroon',loc = 'upper center', bbox_to_anchor=(0.70, 0.92), ncol = 3)

#set color of legend1 text
plt.setp(legend1.get_texts(), color='lime', fontweight = 'bold')
#set color of legend2 text
plt.setp(legend2.get_texts(), color='lime', fontweight = 'bold')
plt.savefig('Acf_activities.pdf')
