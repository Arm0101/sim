from copy import copy
from collections import deque
from math import inf
import numpy as np


class Server:
    def __init__(self, index):
        self.q = deque()
        self.n_clients = 0
        self.leaves = []
        self.arrives = []
        self.leave_time = inf
        self.id = index

    def __enqueue_client(self, arrive_time):
        self.q.append(arrive_time)

    def add_client(self, arrive_time):
        if self.n_clients == 1:
            self.__enqueue_client(arrive_time)
        else:
            self.n_clients = 1
            self.arrives.append(arrive_time)
            self.leave_time = arrive_time + np.random.exponential()  # calular tiempo de salida

    def send_client_to(self, server):
        self.leaves.append(self.leave_time)
        self.n_clients = 0
        self.leave_time = inf
        next_client = self.q.popleft() if len(self.q) > 0 else None
        if next_client is not None:  # si existe algun cliente en la cola
            self.add_client(self.leaves[-1])
        if server is not None:
            server.add_client(self.leaves[-1])

    def __str__(self):
        return (f'id : {self.id}\nn_clients : {self.n_clients}\nqueue: {list(self.q)}\nleaves : {self.leaves}\n'
                f'arrives : {self.arrives}\nleave_time : {self.leave_time}')
