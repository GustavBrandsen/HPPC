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

    Sdiff = np.abs(df['S'].to_numpy() - df2['S'].to_numpy())
    Idiff = np.abs(df['I'].to_numpy() - df2['I'].to_numpy())
    Rdiff = np.abs(df['R'].to_numpy() - df2['R'].to_numpy())

    if i == 0:
        timestep1 = [i, Sdiff, Idiff, Rdiff]
    if i == 3:
        timestep2 = [i, Sdiff, Idiff, Rdiff]

    
os.chdir(path_to_csv_files)
plt.plot([1/10**i for i in range(0,7)],finallist, label = "not test")

plt.xscale("log")
plt.title("Maximal difference between models at different step lengths")
plt.ylabel("Maximal error")
plt.xlabel("Steplength")
plt.legend()
plt.savefig("images/plotplot")
plt.close()

fig, ax = plt.subplots(2,2, figsize=(12,12))
ax = ax.flatten()
ax[0].plot(np.arange(0,200),timestep1[1], label = "S")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Difference between  $\Delta$t and $\Delta$t/2")
ax[1].plot(np.arange(0,200), timestep1[2], label = "I")
ax[1].set_xlabel("Time")
ax[1].set_ylabel("Difference between  $\Delta$t and $\Delta$t/2")
ax[2].plot(np.arange(0,200), timestep1[3], label = "R")
ax[2].set_xlabel("Time")
ax[2].set_ylabel("Difference between  $\Delta$t and $\Delta$t/2")
ax[3].plot(np.arange(0,200), timestep1[1], label = "All")
ax[3].plot(np.arange(0,200), timestep1[2], label = "All")
ax[3].plot(np.arange(0,200), timestep1[3], label = "All")
ax[3].set_xlabel("Time")
ax[3].set_ylabel("Difference between  $\Delta$t and $\Delta$t/2")
ax[0].set_title("S")
ax[1].set_title("I")
ax[2].set_title("R")
ax[3].set_title("All")
fig.suptitle("Difference as a function of time with stepsize $\Delta$ t = 1")
plt.savefig("images/plotplot2")

fig, ax = plt.subplots(2,2, figsize=(12,12))
ax = ax.flatten()
ax[0].plot(np.arange(0,200), timestep2[1], label = "S")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Difference between  $\Delta$t and $\Delta$t/2")
ax[1].plot(np.arange(0,200), timestep2[2], label = "I")
ax[1].set_xlabel("Time")
ax[1].set_ylabel("Difference between  $\Delta$t and $\Delta$t/2")
ax[2].plot(np.arange(0,200), timestep2[3], label = "R")
ax[2].set_xlabel("Time")
ax[2].set_ylabel("Difference between  $\Delta$t and $\Delta$t/2")
ax[3].plot(np.arange(0,200), timestep2[1], label = "All")
ax[3].plot(np.arange(0,200), timestep2[2], label = "All")
ax[3].plot(np.arange(0,200), timestep2[3], label = "All")
ax[3].set_xlabel("Time")
ax[3].set_ylabel("Difference between  $\Delta$t and $\Delta$t/2")
ax[0].set_title("S")
ax[1].set_title("I")
ax[2].set_title("R")
ax[3].set_title("All")
fig.suptitle("Difference as a function of time with stepsize $\Delta$ t = 1/1000")
plt.savefig("images/plotplot3")
