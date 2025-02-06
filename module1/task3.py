import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

path_to_file = os.path.abspath(__file__)
path_to_csv_files = path_to_file.rsplit("/", 1)[0] + "/"

finallist = []
fl = []
ffl = []
for i in range(7):
    df = pd.read_csv(path_to_csv_files + "csv_files/SIR_task3_1_" + str(i) + ".csv", header=None, delimiter=",", names=["t",'S', 'I', 'R'])
    df2 = pd.read_csv(path_to_csv_files + "csv_files/SIR_task3_2_" + str(i) + ".csv", header=None, delimiter=",", names=["t",'S', 'I', 'R'])
    df_new = df.drop(columns=['t'])
    df2_new = df2.drop(columns=['t'])
    diff = np.abs(df_new.to_numpy() - df2_new.to_numpy()).max()
    finallist.append(diff)
    
os.chdir(path_to_csv_files)
plt.plot([1/10**i for i in range(0,7)],finallist)
plt.xscale("log")
plt.title("Maximal difference between models at different step lengths")
plt.ylabel("Maximal difference")
plt.xlabel("Steplength")
plt.savefig("images/plotplot")