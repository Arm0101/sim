import numpy as np


def simulate_events(n_servers, time):
    # initial values
    inf = 2 ** 30
    current_t = 0
    leave_time = inf
    n_clients = 0
    Arrival = []
    Leave = []
    arrival_time = np.random.exponential()

    while True:
        print('\n------------------------------------------------------')
        print('n_clients', n_clients)
        print('Arrival ', Arrival)
        print('Leave ', Leave)
        print('arrival_time ', arrival_time)
        print('leave_time ', leave_time)
        print('------------------------------------------------------')

        if arrival_time < leave_time and arrival_time < time:
            current_t = arrival_time
            n_clients += 1
            new_at = np.random.exponential()
            arrival_time = current_t + new_at
            if n_clients == 1:
                new_lt = np.random.exponential()
                leave_time = current_t + new_lt
            Arrival.append(current_t)

        if leave_time < arrival_time and leave_time < time:
            current_t = leave_time
            n_clients -= 1
            if n_clients == 0:
                leave_time = inf
            else:
                new_lt = np.random.exponential()
                leave_time = current_t + new_lt
            Leave.append(current_t)

        if min(arrival_time, leave_time) > time and n_clients > 0:
            current_t = leave_time
            n_clients -= 1
            if n_clients > 0:
                new_lt = np.random.exponential()
                leave_time = current_t + new_lt
            Leave.append(current_t)

        if min(arrival_time, leave_time) > time and n_clients == 0:
            break
    print('\nFinal result: ')
    print('n_clients ', n_clients)
    print('Arrival ', Arrival)
    print('Leave ', Leave)
    print('arrival_time ', arrival_time)
    print('leave_time ', leave_time)
