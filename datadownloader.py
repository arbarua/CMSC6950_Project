import pandas as pd

URL1 = 'https://drive.google.com/file/d/1HwKjUybLVPEC5LvLJyfxNyzr2a65oZ4c/view?usp=sharing'
URL2 = 'https://drive.google.com/file/d/1PBBk--F1FaDMrluJVDZV_64LBxk8Ny3b/view?usp=sharing'
path1 = 'https://drive.google.com/uc?export=download&id='+URL1.split('/')[-2]
path2 = 'https://drive.google.com/uc?export=download&id='+URL2.split('/')[-2]

data1 = pd.read_csv(path1).reset_index(drop = True)
#increase the dataset size by concatenating it with itself
#data1 = pd.concat([data1,data1]).reset_index(drop = True)
#Saving the data as csv
data1.to_csv('Subject_1_data.csv', index = False)

data2 = pd.read_csv(path2).reset_index(drop = True)
#increase the dataset size by concatenating it with itself
#data2 = pd.concat([data2,data2]).reset_index(drop = True)
#Saving the data as csv
data2.to_csv('Subject_2_data.csv', index = False)
