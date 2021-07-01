# CMSC6950_Project

Working with Package tidynamics. It is a package to calculate cross-correlation, auto-correlation and mean square displacement with minimal dependencies. Let's start with installing tidynamics.

# Installation
It is necessary to have Python and NumPy to install and use tidynamics.

tidynamics can be installed with pip:

pip install --user tidynamics

or with conda (via conda-forge):

conda install -c conda-forge tidynamics

#Extra dependency
For the tasks performed below, python package pandas and matplotlib is needed.

To install it run the command:
#For pip user:
```
pip install pandas matplotlib
```
#For conda user

conda install pandas matplotlib

#How to download data and data information:

To download data run the command:

python3 datadownloader.py 

Successful execution will download two CSV files in the current working directory named “Subject_1_data.csv” and “Subject_2_data.csv”. The datasets include data from smartphone accelerometer sensors while performing six activities. These two datasets both contain 5 columns and 348062 rows. The first column can be neglected. Columns #2-#4 contains data for Accelerometer X-axis, Accelerometer Y-axis, Accelerometer Z-axis respectively. The last column contains the name of the activities.

#Two computational tasks to perform:

#First Task:  

I will computer correlation between column #2 from subject_1_data.csv and subject_2_data.csv which are the data from X-axis of accelerometer sensor. At first I will compute correlation between these two columns using three functions named tidynamics.correlate() from package tidynamics,  numpy.correlate() from package numpy and scipy.signal.correlate() from package scipy.

First the correlation will be performed using the whole columns (348062 rows) and will record the time required to perform correlation for each function. Then the size of the columns will be reduced by a factor of 10 (34806 rows) and the correlation will be performed again as well as time will be recorded. This process will be repeated until the number of rows in the columns become less than 10 and greater than 1. After recording the time, a plot containing six subplots corresponding to six bar plots will be created. Each bar plot will show comparison between the time required by each functionfor different data size.

To perfrom the first task an additional package named scipy needs to be installed. To install it run the following command:
#for pip user:

pip install scipy

#for conda user:

conda install scipy

In addition package “time” may require to be installed. To install it run:
#for pip user:

pip install time

#for conda user:

conda install time

#How to see visual result of first taks:

Too see the visual result of the first task run the following command:

python3 TimeComparison.py

Successful execution of the command will generate a pdf file named “TimeComparison.pdf” in the current working directory. It may take some time to run the python file so be patient.

#Second Task:

In this task, we will use the tidynamics.acf() function to compute autocorrelation of some data from the “Subject_2_data.csv” file. Autocorrelation means the correlation of some data with itself at different lags. For more information about autocorrelation, check this link https://nwfsc-timeseries.github.io/atsa-labs/sec-tslab-correlation-within-and-among-time-series.html 

Recall that the “Subject_2_data.csv” contains data for a tri-axial accelerometer for six different activities. For this task, I will use 500 rows for each type of activity for columns #2-#4, which indicate the three axes of the accelerometer. As there are six different activities so there will be six (500 by 3) dataframe I will be working on. 

There will be total of 6 main subplots and each main subplot will contain 3 subplots. So, we will see 18 plots in total (3 subplots for one activity type).

As described, there will be 3 subplots for each type of activities where one plot will be a scatter plot and it will visualize the autocorrelation of each axis of the tri-axial accelerometer with itself (correlation of x-axis with itself, correlation of y-axis with itself, correlation of y-axis with itself) for different time lags (lag 1 to lag 500). Another horizontal rectangular plot will be there under the plot I just described. This will show the line plot of the raw values of all three accelerometer axes. Finally, the other plot will be a bar plot, and it will show the maximum autocorrelation found for each axis.    
   
