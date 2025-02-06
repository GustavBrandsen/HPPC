import matplotlib.pyplot as plt
import pandas as pd
import os

path_to_file = os.path.abspath(__file__)
path_to_csv_files = path_to_file.rsplit("/", 1)[0] + "/"

def make_pic(filename, beta, gamma, dt):
    df = pd.read_csv(path_to_csv_files + 'csv_files/' + filename + '.csv', header=None, delimiter=",", names=["t",'S', 'I', 'R'])
    steps = df['t']
    fig, ax = plt.subplots(2,2, figsize=(12,12))
    ax[0,0].plot(steps, df['S'], label='S')
    ax[0,0].set_title('S')
    ax[0,0].set_xlabel('Days')
    ax[0,0].set_ylabel('Uninfected people')
    ax[0,1].plot(steps, df['I'], label='I')
    ax[0,1].set_title('I')
    ax[0,1].set_xlabel('Days')
    ax[0,1].set_ylabel('Infected people')
    ax[1,0].plot(steps, df['R'], label='R')
    ax[1,0].set_title('R')
    ax[1,0].set_xlabel('Days')
    ax[1,0].set_ylabel('Recovered people')
    ax[1,1].plot(steps, df['S'], label='S')
    ax[1,1].plot(steps, df['I'], label='I')
    ax[1,1].plot(steps, df['R'], label='R')
    ax[1,1].set_title('All')
    ax[1,1].set_xlabel('Days')
    ax[1,1].set_ylabel('All people')
    ax[1,1].legend()
    fig.suptitle(r'SIR model with $\gamma$ = {gamma}, $\beta$ = {beta}, $\Delta$t = {dt}'.format(gamma=gamma, beta=beta, dt = dt))
    os.chdir(path_to_csv_files)
    plt.savefig('images/' + filename + '.png')

make_pic('SIR_task2_1', 0.2, 0.1, 0.1)
make_pic('SIR_task2_2', 0.2, 0.1, 0.00001)

make_pic('SIR_task1_1', 10, 0.2, 0.1)
make_pic('SIR_task1_2', 0.1, 10, 0.1)
make_pic('SIR_task1_3', 10, 10, 0.1)
make_pic('SIR_task1_4', 0.1, 0.2, 0.1)
