import random
import time

class TrafficSignal:
    def __init__(self, roads, config={}):
        # Initialize roads
        self.roads = roads
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)
        # Calculate properties
        self.init_properties()

    def set_default_config(self):
        self.cycle = [(False, False, False, True), (False, False, True, False), (False, True, False, False), (True, False, False, False)]
        self.state = True
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 12

        self.current_cycle_index = 0

        self.last_t = 0
        self.times = [20, 20] #tiempo de semaforos [verde, rojo]
        self.status = True #tiempo de semaforos [verde, rojo]
        self.timer = self.times[0]

    def init_properties(self):
        self.timer = self.times[0] if self.status else self.times[1]
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]
    
    def update2(self, sim):
        cycle_length = 5
        # randomize the cycle length after every cycle
        if(sim.t % cycle_length < 0.3):
            cycle_length = random.randint(5, 10)
        k = (sim.t // cycle_length) % 4
        self.current_cycle_index = int(k)
        if(len(self.roads) < 4):
            self.current_cycle_index = 3

    def update(self, sim):
        self.timer -= sim.dt
        if(self.timer <= 0):
            self.status = False if self.status else True
            self.timer = self.times[0] if self.status else self.times[1]
            