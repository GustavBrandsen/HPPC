import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

path_to_file = os.path.abspath(__file__)
path_to_csv_files = path_to_file.rsplit("/", 1)[0] + "/"

err = []
for i in range(7):
    df = pd.read_csv(path_to_csv_files + "csv_files/SIR_task3_1_" + str(i) + ".csv", header=None, delimiter=",", names=["t",'S', 'I', 'R'])
    df2 = pd.read_csv(path_to_csv_files + "csv_files/SIR_task3_2_" + str(i) + ".csv", header=None, delimiter=",", names=["t",'S', 'I', 'R'])
    df_new = df.drop(columns=['t'])
    df2_new = df2.drop(columns=['t'])
    diff = np.abs(df_new.to_numpy() - df2_new.to_numpy())
    err.append(diff.max())

    Sdiff = np.abs(df['S'].to_numpy() - df2['S'].to_numpy())
    Idiff = np.abs(df['I'].to_numpy() - df2['I'].to_numpy())
    Rdiff = np.abs(df['R'].to_numpy() - df2['R'].to_numpy())

    if i == 0:
        timestep1 = [i, Sdiff, Idiff, Rdiff]
    if i == 3:
        timestep2 = [i, Sdiff, Idiff, Rdiff]

    
os.chdir(path_to_csv_files)
plt.plot([1/10**i for i in range(0,7)], err)
plt.xscale("log")
plt.title("Maximal difference between models at different step lengths")
plt.ylabel("Maximal error")
plt.xlabel("Steplength")
plt.savefig("images/plot_maximal_error.png")