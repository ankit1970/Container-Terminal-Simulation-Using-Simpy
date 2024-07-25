# Container-Terminal-Simulation-Using-Simpy
A discrete-event simulation of a container terminal using SimPy, modeling vessel arrivals, berthing, crane operations, and truck transportation to analyze waiting times and terminal efficiency.

## Overview

This project simulates a container terminal with vessel arrivals, berthing, quay crane operations, and truck transportation. The simulation is built using SimPy, a Python-based discrete-event simulation framework.

## Features

### Vessel Arrivals

* Vessels arrive at the terminal following an exponential distribution with an average of 5 hours between arrivals.
* Simulates vessel arrivals based on a Poisson process.
* Generates vessel arrival times and IDs.

### Berthing Operations

* There are two available berths at the terminal. If both berths are occupied, incoming vessels join a queue.
* Models berthing operations with multiple berths.
* Tracks waiting times for berths.

### Crane Operations

* Two quay cranes are responsible for unloading containers from vessels. Each crane takes 3 minutes to move one container. The cranes operate independently but cannot serve the same vessel simultaneously.
* Simulates quay crane operations for container lifting.
* Models crane time per container.

### Truck Transportation

* Three trucks transport containers from quay cranes to yard blocks. Each truck takes 6 minutes to drop off a container and return to the quay crane.
* Simulates truck transportation for containers.
* Models truck time per trip.

### Summary Statistics

* The simulation includes a simple logging system that records events such as vessel arrival, berthing, quay crane movements, and truck operations. The log includes the current simulation time.
* Generates summary statistics for total vessels processed.
* Calculates average waiting times for berths, cranes, and trucks.

## Usage

1. Install SimPy using `pip install simpy`
2. Run the simulation using `container_terminal_simulation.py`
3. View the simulation output and summary statistics in the console

## Configuration

The simulation parameters can be adjusted in the `container_terminal_simulation.py` file:

* `SIMULATION_TIME`: Total simulation time in minutes. It is been asked by user already.
* `VESSEL_ARRIVAL_RATE`: Vessel arrival rate (per minute).
* `CONTAINERS_PER_VESSEL`: Number of containers per vessel.
* `CRANE_TIME_PER_CONTAINER`: Time to move one container in minutes.
* `TRUCK_TIME_PER_TRIP`: Time for a truck to drop off container and return in minutes.
* `NUM_BERTHS`, `NUM_CRANES`, `NUM_TRUCKS`: Number of berths, cranes, and trucks.
