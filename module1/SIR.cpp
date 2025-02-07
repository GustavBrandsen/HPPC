#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>

// Function to take a step in the SIR model
// state: vector of S, I, R
// beta: infection rate
// gamma: recovery rate
// dt: time step
std::vector<float> take_step(std::vector<float> state, float beta, float gamma, float dt)
{
    std::vector<float> new_state;
    // todo: implement the SIR model
    float S = state[0];
    float I = state[1];
    float R = state[2];
    float N = S + I + R;
    float Snew = -beta * I * (S / N) * dt + S;
    float Inew = (beta * I * (S / N) - gamma * I) * dt + I;
    float Rnew = gamma * I * dt + R;
    new_state = {Snew,
                 Inew,
                 Rnew};
    return new_state;
}

void run_SIR(std::string name, int days, std::vector<float> state, float beta, float gamma, float dt, bool skip = false)
{
    std::ofstream file("csv_files/" + name + ".csv");
    float j = days / dt;
    for (int i = 0; i < j; i++)
    {
        state = take_step(state, beta, gamma, dt);
        if (skip && i % static_cast<int>(round(1 / dt)) != 0)
        {
            continue;
        }
        file << i * dt << "," << state[0] << ", " << state[1] << ", " << state[2] << "\n";
    }
}

//======================================================================================================
//======================== Main function ===============================================================
//======================================================================================================
int main(int argc, char *argv[])
{
    // define the parameters

    // TODO: Define the parameters of the SIR model

    // TODO: implement the SIR model

    // TODO: Save the results to a file

    std::vector<float> state = {9999., 1., 0.};

    // Task 1
    run_SIR("SIR_task1_1", 200, state, 1, 0.1, 0.1);
    run_SIR("SIR_task1_2", 200, std::vector<float>{5000, 5000, 0}, 0.2, 1, 0.1);
    run_SIR("SIR_task1_3", 200, state, 1, 1, 0.1);
    run_SIR("SIR_task1_4", 200, state, 0.2, 0.1, 0.1);

    // Task 2
    run_SIR("SIR_task2_1", 200, state, 0.2, 0.1, 0.1);
    run_SIR("SIR_task2_2", 200, state, 0.2, 0.1, 0.00001, true);

    for (int i = 0; i < 7; i++)
    {
        run_SIR("SIR_task3_1_" + std::to_string(i), 200, state, 0.2, 0.1, 1 / pow(10, i), true);
        run_SIR("SIR_task3_2_" + std::to_string(i), 200, state, 0.2, 0.1, 1 / pow(10, i) / 2, true);
    }

    return 0;
}
