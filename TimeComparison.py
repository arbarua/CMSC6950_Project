#Import required packages and modules
import numpy as np
import tidynamics
import time
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal

#Read the datasets
data1 = pd.read_csv('Subject_1_data.csv').reset_index(drop = True)
#increase the data size by concatenating it with itself
data1 = pd.concat([data1,data1]).reset_index(drop = True)

data2 = pd.read_csv('Subject_2_data.csv').reset_index(drop = True)
#increase the data size by concatenating it with itself
data2 = pd.concat([data2,data2]).reset_index(drop = True)

divider = 1 #Divides the dataset by factor of 10
tidy_timer = [] #will record the time for tidynamics.correlate() for different data size
np_timer = [] #will record the time for numpy.correlate() for different data size
sp_timer = [] #will record the time for scipy.signal.correlate() for different data size
limit_data = [] #will contain sizes of data for each time computation performed
cc = 1
#counter = 0 #A counter to limit the task to be perfomed on only six different datas sizes
while(int(data1.shape[0]/divider)>1): #Continue looping until data size become less than 10 and greater than 1
    print("Loop ",cc," running")
    cc+=1
    limit = int(data1.shape[0]/divider) #compute the number of rows to be included in data
    #print(limit)
    #if(counter>5):
        #break
    limit_data.append(limit)
	
	#start time counter
    time_count= time.time()
    tidy_corr_val = tidynamics.correlation(data1.iloc[:limit,1],data2.iloc[:limit,1])
    tidy_timer.append(time.time()-time_count) #stop time counter and calculate required time and append it
    #print("tidy time", time.time()-time_count)
	
	#start time counter
    time_count= time.time()
    np_corr_val = np.correlate(data1.iloc[:limit,1],data2.iloc[:limit,1],'full')
    np_timer.append(time.time()-time_count)#stop time counter and calculate required time and append it
    #print("np time", time.time()-time_count)
	
	#start time counter
    time_count= time.time()
    scipy_corr_val = signal.correlate(data1.iloc[:limit,1],data2.iloc[:limit,1],mode = 'full', method = 'fft')
    sp_timer.append(time.time()-time_count)#stop time counter and calculate required time and append it
    #print("sp time", time.time()-time_count)
    divider*=10 #increase the divider size by a factor of 10
    #counter+=1

time_data = pd.concat([pd.DataFrame(tidy_timer),pd.DataFrame(np_timer),pd.DataFrame(sp_timer)], axis = 1)#store recordedtime for each function in a single dataframe
time_data.columns = ['tidynamics_time', 'numpy_time', 'scipy_time']#set the column names
time_data.index = limit_data#set the index by the sizes of the data for which correlation was performed 

#A function to set y limit of the bar chart to visualize the charts in a nice way
def set_lim(x):
    a = 1
    while(x<=1):
        x = x*a
        #print(x)
        a = a*10
        #print(a)
    return 4/a

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16, 13),facecolor='maroon')#declared a plot with 6 sub plots aranged in 2 rows and 3 columns

X = np.arange(3)#variable needed to set the x coordinates of bars in each subplot

width = 0.5 #width of each bar in each subplot

# Create the bar charts!
for i in range(0,2): #iterate through rows
    for j in range(0,3): #iterate through columns
        if(i>0):
            k = j+3 #a variable k for correctly indicate the row of dataframe time_data to ease the access of its' rows
        else:
            k = j
        #bar for time required by tidynamics.correlate() for each data size
        axes[i,j].bar(X[0] + 0.25, time_data.iloc[k,0], width, label='Tidynamics', color='cadetblue',hatch="/", edgecolor = 'black',linewidth = 3)
        axes[i,j].text(X[0] + 0.025,time_data.iloc[k,0],str("{:.2e}".format(time_data.iloc[k,0])), color = 'white',
                       fontsize=12, fontweight = 'bold',
                       bbox=dict(facecolor='cadetblue', alpha=1))

        #bar for time required by numpy.correlate() for each data size
        axes[i,j].bar(X[1] + 0.25, time_data.iloc[k,1], width, label='Numpy', color='mediumorchid',hatch="x", edgecolor = 'black',linewidth = 3)
        axes[i,j].text(X[1] + 0.025,time_data.iloc[k,1],str("{:.2e}".format(time_data.iloc[k,1])),color = 'white',
                       fontsize=12, fontweight = 'bold',
                       bbox=dict(facecolor='mediumorchid', alpha=1))

        #bar for time required by scipy.signal.correlate() for each data size
        axes[i,j].bar(X[2] + 0.25, time_data.iloc[k,2], width, label='Scipy', color='crimson',hatch="\\", edgecolor = 'black',linewidth = 3)
        axes[i,j].text(X[2] + 0.025,time_data.iloc[k,2],str("{:.2e}".format(time_data.iloc[k,2])),color = 'white',
                       fontsize=12, fontweight = 'bold',
                       bbox=dict(facecolor='crimson', alpha=1))
        #ax.bar(x + 3*width/2, df['others'], width, label='Others', color='#929591')

		#set y label for each sub plot
        axes[i,j].set_ylabel('time Required in seconds',c = 'white',fontweight = 'bold', fontsize = 15)
        #set title containing the data size fro each sub plot
        axes[i,j].set_title('With '+str(limit_data[k])+' rows',c = 'white',fontweight = 'bold', fontsize = 15)

        #arranging the x ticks and tick labels
        axes[i,j].set_xticks(np.arange(0.25,3))    # This ensures we have one tick per year, otherwise we get fewer
        
        axes[i,j].set_xticklabels(['Tidynamics', 'Numpy', 'Scipy'], rotation='vertical',c = 'white',fontweight = 'bold', fontsize = 15)
        #axes[i].legend()

        #print(max(time_data.iloc[i+k,0],time_data.iloc[i+k,1],time_data.iloc[i+k,2]))
        axes[i,j].set_ylim([0, max(time_data.iloc[k,0],time_data.iloc[k,1],time_data.iloc[k,2])+
                          set_lim(max(time_data.iloc[k,0],time_data.iloc[k,1],time_data.iloc[k,2]))])#setting y limit using function set_lim()
        axes[i,j].tick_params(axis='y', colors='white', labelsize = 15)

		#colouring the borders of each subplot
        axes[i,j].spines["bottom"].set_color("lime")
        axes[i,j].spines["left"].set_color("black")
        axes[i,j].spines["top"].set_color("black")
        axes[i,j].spines["right"].set_color("black")

		#setting width of the borders of each subplot
        axes[i,j].spines["bottom"].set_linewidth(7)
        axes[i,j].spines["left"].set_linewidth(7)
        axes[i,j].spines["top"].set_linewidth(7)
        axes[i,j].spines["right"].set_linewidth(7)
        axes[i,j].set_facecolor('aquamarine')
fig.tight_layout(h_pad=1, w_pad=0.5)
plt.savefig('TimeComparison.pdf')
