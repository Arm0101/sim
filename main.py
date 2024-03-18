from simulation import simulate_events
from simulation.server import Server
import numpy as np

if __name__ == '__main__':
    servers = simulate_events(n_servers=2, time=5)
    for s in servers:
        print(s)
        print('///////////////////////////////////////////')

