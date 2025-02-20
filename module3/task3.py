import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
from matplotlib.ticker import LogLocator, LogFormatter

# num_of_workers = [1, 3, 7, 15, 31, 63]
num_of_workers = np.array([2**i-1 for i in range(1, 7)])
total_time = [21.52, 7.224, 3.412, 1.759, 1.002, 0.7597]
num_of_settings = 6561

avg_time = []
speedup = total_time[0]/np.array(total_time)
for i in range(len(total_time)):
    avg_time.append((total_time[i]*num_of_workers[i]) / num_of_settings)
    # avg_time.append(total_time[i] / (num_of_settings * num_of_workers[i]))
    

fig = plt.figure(figsize=(10, 10))  # Set the overall figure size
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 0.6], width_ratios=[0.8])

ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])

ax0.plot(num_of_workers+1, np.ones(6)*avg_time[-0]*10**6, 'r--', alpha=0.8, label='Perfect Scaling')
ax0.plot(num_of_workers+1, np.array(avg_time)*10**6, label = 'Measured proc. time/task')

ax0.set_xlabel('Number of MPI Processes')
ax0.set_ylabel('Average Time (mus)')
ax0.set_title('Computation Time pr. task as function of MPI Processes')
ax0.set_xscale('log', base=2)
ax0.set_ylim(0, avg_time[-1]*10**6+1000)
#ax0.yscale('log', base=2)
ax0.xaxis.set_major_locator(LogLocator(base=2))
ax0.xaxis.set_major_formatter(LogFormatter(base=2))
ax0.legend()


ax1.plot(num_of_workers+1, speedup, label = 'Measured Speedup')
ax1.plot(num_of_workers+1, num_of_workers, 'r--', alpha=0.8, label='Perfect Scaling')
ax1.set_xlabel('Number of MPI Processes')
ax1.set_yscale('log', base=2)
ax1.set_ylabel('Speedup')
ax1.set_title('Speedup as function of MPI Processes')
ax1.set_xscale('log', base=2)
ax1.set_ylim(0, 64)
ax1.xaxis.set_major_locator(LogLocator(base=2))
ax1.xaxis.set_major_formatter(LogFormatter(base=2))
ax1.yaxis.set_major_locator(LogLocator(base=2))
ax1.yaxis.set_major_formatter(LogFormatter(base=2))
ax1.legend()

plt.savefig('task3.png')



