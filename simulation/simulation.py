import numpy as np
from .server import Server
from math import inf


def simulate_events(n_servers, time):
    # valores iniciales
    servers = [Server(i) for i in range(0, n_servers)]
    n_clients = 0
    arrival_time = np.random.exponential()
    while True:
        leave_time, server_id = get_min_leave_time(servers)  # obtener el servidor con el tiempo de salida minimo

        if arrival_time < leave_time and arrival_time < time:
            n_clients += 1  # nuevo cliente
            servers[0].add_client(arrival_time)  # agregar cliente al primer servidor
            new_at = np.random.exponential()
            arrival_time = arrival_time + new_at  # calcular el tiempo del proximo arrivo
            if servers[0].leave_time < leave_time:  # actualizar el tiempo de salida minimo
                leave_time = servers[0].leave_time
                server_id = 0

        if leave_time < arrival_time and leave_time < time or min(arrival_time, leave_time) > time and n_clients > 0:
            current_server = servers[server_id]
            next_server = servers[server_id + 1] if server_id + 1 < n_servers else None
            current_server.send_client_to(next_server)
            if next_server is None:
                n_clients -= 1

        if min(arrival_time, leave_time) > time and n_clients == 0:  # si ya no existen clientes en el sistema
            break
    return servers


def get_min_leave_time(servers):
    min_time = inf
    server_id = -1
    for server in servers:
        if server.leave_time < min_time:
            server_id = server.id
            min_time = server.leave_time
    return min_time, server_id
