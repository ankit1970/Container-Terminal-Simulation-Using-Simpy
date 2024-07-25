# Container Terminal Simulation using SimPy

# Author: Ankit Sharma
# =========================================
# This simulation models a container terminal with vessel arrivals, berthing, quay crane operations, and truck transportation.

#import dependencies
import simpy
import random
import statistics

# User to provice total simulation time in minutes
SIMULATION_TIME = int(input("Enter the simulation time (in minutes):"))  

# Constants
VESSEL_ARRIVAL_RATE = 1 / (5 * 60)  # Vessel arrival rate (per minute)
CONTAINERS_PER_VESSEL = 150
CRANE_TIME_PER_CONTAINER = 3  # Time to move one container in minutes
TRUCK_TIME_PER_TRIP = 6  # Time for a truck to drop off container and return in minutes
NUM_BERTHS = 2
NUM_CRANES = 2
NUM_TRUCKS = 3

class ContainerTerminal:
    
    # Initialize the container terminal simulation
    def __init__(self, env):
        self.env = env
        self.berths = simpy.Resource(env, NUM_BERTHS)
        self.cranes = simpy.Resource(env, NUM_CRANES)
        self.trucks = simpy.Resource(env, NUM_TRUCKS)
        self.vessel_id = 0
        self.total_vessels = 0
        self.total_waiting_time = 0

    # Start the simulation
    def start(self):
        # Process vessel arrivals
        self.env.process(self.vessel_arrivals())
        # Run the simulation for the specified time
        self.env.run(until=SIMULATION_TIME)
        # Print summary statistics
        self.summary_statistics()

    # Simulate vessel arrivals
    def vessel_arrivals(self):
        while True:
            # Generate exponential arrival time
            yield self.env.timeout(random.expovariate(VESSEL_ARRIVAL_RATE))
            # Increment vessel ID and process vessel
            self.vessel_id += 1
            vessel_process = self.env.process(self.vessel(f"Vessel_{self.vessel_id}"))

    # Simulate vessel operations (berthing, crane, truck)
    def vessel(self, name):
        # Log vessel arrival
        arrival_time = self.env.now
        self.log(f"{arrival_time:.2f}: {name} arrives.")
        # Increment total vessels
        self.total_vessels += 1
        
        # Request berth
        with self.berths.request() as req:
            yield req
            # Log berth time and waiting time
            berth_time = self.env.now
            waiting_time = berth_time - arrival_time
            self.total_waiting_time += waiting_time
            self.log(f"{berth_time:.2f}: {name} berths. (Waited {waiting_time:.2f} minutes)")
            
            # Simulate container lifting and truck transportation
            for i in range(CONTAINERS_PER_VESSEL):
                
                # Request crane
                with self.cranes.request() as crane_req:
                    yield crane_req
                    # Log crane start time
                    container_lift_time = self.env.now
                    self.log(f"{container_lift_time:.2f}: Crane starts lifting container {i+1} from {name}.")
                    # Simulate crane time
                    yield self.env.timeout(CRANE_TIME_PER_CONTAINER)
                    
                    # Request truck
                    with self.trucks.request() as truck_req:
                        yield truck_req
                        # Log truck start time
                        truck_depart_time = self.env.now
                        self.log(f"{truck_depart_time:.2f}: Truck starts transporting container {i+1} from {name}.")
                        # Simulate truck time
                        yield self.env.timeout(TRUCK_TIME_PER_TRIP)
                        # Log truck return time
                        truck_return_time = self.env.now
                        self.log(f"{truck_return_time:.2f}: Truck returns after dropping container {i+1} from {name}.")
                        
            # Log vessel departure
            departure_time = self.env.now
            self.log(f"{departure_time:.2f}: {name} departs.")

    # Log messages
    def log(self, message):
        print(message)

    # Print summary statistics
    def summary_statistics(self):
        if self.total_vessels > 0:
            average_waiting_time = self.total_waiting_time / self.total_vessels
            print(f"\nSimulation Summary:\n"
                  f"Total Vessels Processed: {self.total_vessels}\n"
                  f"Average Waiting Time for Berths: {average_waiting_time:.2f} minutes")
        else:
            print("No vessels processed.")

if __name__ == "__main__":
    env = simpy.Environment()
    terminal = ContainerTerminal(env)
    terminal.start()