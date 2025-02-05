#include <iostream>
#include <fstream>
#include <vector>
#include <string>

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
        if (skip && i % 10 != 0)
        {
            continue;
        }
        file << i*dt << "," << state[0] << ", " << state[1] << ", " << state[2] << "\n";
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

    run_SIR("SIR_task2_1", 200, state, 0.2, 0.1, 0.1);
    run_SIR("SIR_task2_2", 200, state, 0.2, 0.1, 0.00001, true);

    return 0;
}
