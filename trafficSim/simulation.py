from .road import Road
from copy import deepcopy
from .vehicle_generator import VehicleGenerator
from .traffic_signal import TrafficSignal

class Simulation:
    vehiclesPassed = 0;
    vehiclesPresent = 0;
    vehicleRate = 0;
    isPaused = False;

    def __init__(self, config={}):
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        self.t = 0.0            # Time keeping
        self.frame_count = 0    # Frame count keeping
        self.dt = 1/60          # Simulation time step
        self.roads = []         # Array to store roads
        self.generators = []
        self.traffic_signals = []
        self.routes_tree = None

    def create_road(self, start, end):
        road = Road(start, end)
        self.roads.append(road)
        return road

    def create_tree_routes(self, routes):
        self.routes_tree = routes
        
    def create_roads(self, road_list):
        for road in road_list:
            self.create_road(*road)

    def create_gen(self, config={}):
        gen = VehicleGenerator(self, config)
        self.generators.append(gen)
        Simulation.vehicleRate = gen.vehicle_rate
        return gen

    def create_signal(self, roads, config={}):
        roads = [[self.roads[i] for i in road_group] for road_group in roads]
        sig = TrafficSignal(roads, config)
        self.traffic_signals.append(sig)
        return sig

    def update(self):
        # Update every road
        for road in self.roads:
            road.update(self.dt)

        # Add vehicles
        for gen in self.generators:
            gen.update()

        for signal in self.traffic_signals:
            signal.update(self)

        # Check roads for out of bounds vehicle
        for road in self.roads:
            # If road has no vehicles, continue
            if len(road.vehicles) == 0: continue
            # If not
            vehicle = road.vehicles[0]
            # If first vehicle is out of road bounds
            if vehicle.x >= road.length:
                # If vehicle has a next road
                if vehicle.type_routes == 0:
                    if vehicle.current_road_index + 1 < len(vehicle.path):
                        # Update current road to next road
                        vehicle.current_road_index += 1
                        # Create a copy and reset some vehicle properties
                        new_vehicle = deepcopy(vehicle)
                        new_vehicle.x = 0
                        # Add it to the next road
                        #matrix = vehicle.node.getMatrix()
                        #next_road = keras.mimodelo(matrix)
                        next_road_index = vehicle.path[vehicle.current_road_index]
                        #cuantificar cantidad de vehiculos
                        if new_vehicle.node.index_route == 0:
                            print(str(new_vehicle.node.quantity_vehicles) + ' - ' + str(new_vehicle.node.index_route))
                        new_vehicle.node.quantity_vehicles -= 1
                        
                        new_vehicle.update_node(vehicle.node.siguiente_nodo(next_road_index))
                        new_vehicle.node.quantity_vehicles += 1
                        if new_vehicle.node.index_route == 2:
                            print(str(new_vehicle.node.quantity_vehicles) + ' - ' + str(new_vehicle.node.index_route))
                        #fin cuantificar cantidad de vehiculos
                        new_vehicle.waitingCycles = 0
                        #print(new_vehicle.node.index_route)
                        #print(new_vehicle.node.id)
                        self.roads[next_road_index].vehicles.append(new_vehicle)
                    else:
                        Simulation.vehiclesPassed += 1
                    # In all cases, remove it from its road
                    road.vehicles.popleft() 
                elif vehicle.type_routes == 1:
                    print('routa inicio fin')
                    if vehicle.path[1] != vehicle.node.index_route:
                        next_road_index = vehicle.node.random_nodo()
                        print('next_road_index', next_road_index)
                        new_vehicle = deepcopy(vehicle)
                        new_vehicle.x = 0
                        if new_vehicle.node.index_route == 0:
                            print(str(new_vehicle.node.quantity_vehicles) + ' - ' + str(new_vehicle.node.index_route))
                        new_vehicle.node.quantity_vehicles -= 1
                        
                        new_vehicle.update_node(vehicle.node.siguiente_nodo(next_road_index))
                        new_vehicle.node.quantity_vehicles += 1
                        if new_vehicle.node.index_route == 2:
                            print(str(new_vehicle.node.quantity_vehicles) + ' - ' + str(new_vehicle.node.index_route))
                        #fin cuantificar cantidad de vehiculos
                        new_vehicle.waitingCycles = 0
                        #print(new_vehicle.node.index_route)
                        #print(new_vehicle.node.id)
                        print('new_vehicle.node.index_route', new_vehicle.node.index_route, new_vehicle.node.type)
                        self.roads[next_road_index].vehicles.append(new_vehicle)
                    else:
                        Simulation.vehiclesPassed += 1
                    road.vehicles.popleft() 
                    #ramdon next nodos
                # if vehicle reached the end of the path
                # if vehicle.current_road_index + 1 == len(vehicle.path):
                #     Simulation.vehiclesPassed += 1
                    # print("Vehicle passed: " + str(Simulation.vehiclesPassed))

        # Check for the number of vehicles present
        Simulation.vehiclesPresent = 0
        for road in self.roads:
            Simulation.vehiclesPresent += len(road.vehicles)

        # Increment time
        self.t += self.dt
        self.frame_count += 1


    def run(self, steps):
        for _ in range(steps):
            self.update()

    def pause(self):
        self.isPaused = True

    def resume(self):
        self.isPaused = False