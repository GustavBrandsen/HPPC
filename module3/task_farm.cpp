/*
  Assignment: Make an MPI task farm. A "task" is a randomly generated integer.
  To "execute" a task, the worker sleeps for the given number of milliseconds.
  The result of a task should be send back from the worker to the master. It
  contains the rank of the worker
*/

#include <iostream>
#include <random>
#include <chrono>
#include <thread>
#include <array>

// To run an MPI program we always need to include the MPI headers
#include <mpi.h>

const int NTASKS = 5000; // number of tasks
const int RANDOM_SEED = 1234;

void master(int nworker)
{
    std::array<int, NTASKS> task, result;

    // set up a random number generator
    std::random_device rd;
    // std::default_random_engine engine(rd());
    std::default_random_engine engine;
    engine.seed(RANDOM_SEED);
    // make a distribution of random integers in the interval [0:30]
    std::uniform_int_distribution<int> distribution(0, 30);

    for (int &t : task)
    {
        t = distribution(engine); // set up some "tasks"
    }

    /*
    IMPLEMENT HERE THE CODE FOR THE MASTER
    ARRAY task contains tasks to be done. Send one element at a time to workers
    ARRAY result should at completion contain the ranks of the workers that did
    the corresponding tasks
    */
    int tasks_sent = 0;
    int tasks_received = 0;

    // Send initial tasks to each worker
    for (int i = 0; i < nworker && tasks_sent < NTASKS; i++)
    {
        MPI_Send(&task[tasks_sent], 1, MPI_INT, i + 1, 0, MPI_COMM_WORLD);
        tasks_sent++;
    }

    // Keep sending tasks as workers return results
    while (tasks_received < NTASKS)
    {
        int worker_rank;
        MPI_Recv(&worker_rank, 1, MPI_INT, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        result[tasks_received] = worker_rank;
        tasks_received++;

        if (tasks_sent < NTASKS)
        {
            MPI_Send(&task[tasks_sent], 1, MPI_INT, worker_rank, 0, MPI_COMM_WORLD);
            tasks_sent++;
        }
        else
        {
            int termination_signal = -1;
            MPI_Send(&termination_signal, 1, MPI_INT, worker_rank, 0, MPI_COMM_WORLD);
        }
    }

    // Print out a status on how many tasks were completed by each worker
    for (int worker = 1; worker <= nworker; worker++)
    {
        int tasksdone = 0;
        int workdone = 0;
        for (int itask = 0; itask < NTASKS; itask++)
            if (result[itask] == worker)
            {
                tasksdone++;
                workdone += task[itask];
            }
        std::cout << "Master: Worker " << worker << " solved " << tasksdone << " tasks\n";
    }
}

// call this function to complete the task. It sleeps for task milliseconds
void task_function(int task)
{
    std::this_thread::sleep_for(std::chrono::milliseconds(task));
}

void worker(int rank)
{
    /*
    IMPLEMENT HERE THE CODE FOR THE WORKER
    Use a call to "task_function" to complete a task
    */
    int task;
    MPI_Status status;

    while (true)
    {
        // Receive a task from the master
        MPI_Recv(&task, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);

        if (task == -1) // Termination signal
            break;

        task_function(task);

        // Send the result back to the master
        MPI_Send(&rank, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
    }
}

int main(int argc, char *argv[])
{
    int nrank, rank;

    MPI_Init(&argc, &argv);                // set up MPI
    MPI_Comm_size(MPI_COMM_WORLD, &nrank); // get the total number of ranks
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);  // get the rank of this process

    if (rank == 0)         // rank 0 is the master
        master(nrank - 1); // there is nrank-1 worker processes
    else                   // ranks in [1:nrank] are workers
        worker(rank);

    MPI_Finalize(); // shutdown MPI
}
