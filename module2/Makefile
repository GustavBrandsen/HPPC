CXX := g++

#######################################################
# Optimization flags are chosen as the last definition.
# Comment out using "#" at the begining of the line or rearrange according to your needs.
#
# Faster compilation time
OPT=-O1

# Add profiling to code
OPT=-O1 -pg

# Fastest executable (-ffast-math removes checking for NaNs and other things)
OPT=-O3 -ffast-math

CXXFLAGS := $(OPT) -Wall -march=native -g -std=c++17

default: seq vec vec_updated

seq: Water_sequential.cpp
	$(CXX) Water_sequential.cpp $(CXXFLAGS) -o seq

vec: Water_vectorised.cpp
	$(CXX) Water_vectorised.cpp $(CXXFLAGS) -fopenmp-simd -o vec
	
vec_updated: Water_vectorised_updated.cpp
	$(CXX) Water_vectorised_updated.cpp $(CXXFLAGS) -fopenmp-simd -o vec_updated

clean:
	rm -fr seq vec vec_updated
