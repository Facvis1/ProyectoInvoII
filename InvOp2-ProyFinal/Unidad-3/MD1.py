import random
import queue

class Cliente(object):
    def __init__(self, cantcliente, arrival_time):
        self.cantcliente = cantcliente
        self.arrival_time = arrival_time
        self.departure_time = None
        
    def get_wait(self):
        if self.departure_time is None:
            return None
        else:
            return self.departure_time - self.arrival_time
        
    def __str__(self):
        return "Cliente({}, {})".format(self.cantcliente, self.arrival_time)
    
    def __repr__(self):
        return str(self)


def sitasaservlate_md1(lambd, tasaserv, max_time, verbosity=0):
    md1 = queue.Queue()
    served_customers = []
    unserved_customers = []
    next_arrival = random.expovariate(lambd)
    next_service = next_arrival + 1/tasaserv

    
    t = next_arrival
    cantcliente = 1

    while t < max_time:

        if t == next_arrival:
            cliente = Cliente(cantcliente, arrival_time=t)
            cantcliente += 1
            md1.put(cliente)

            if verbosity >= 2:
                print("{:10.2f}: Cliente Numero {} llega".format(t, cliente.cantcliente))

            next_arrival = t + random.expovariate(lambd)

        if t == next_service:
            done_customer = md1.get()
            done_customer.departure_time = t

            served_customers.append(done_customer)

            if verbosity >= 2:
                print("{:10.2f}: Cliente Numero {} se va".format(
                    t, done_customer.cantcliente))

            if md1.empty():
                next_service = next_arrival + 1/tasaserv
            else:
                next_service = t + 1/tasaserv

        if verbosity >= 1:
            print("{:10.2f}: {}".format(t, "Numero"*md1.qsize()))

        t = min(next_arrival, next_service)

    while not md1.empty():
        unserved_customers.append(md1.get())

    return served_customers, unserved_customers

vector1, vector2 = sitasaservlate_md1(1, 1, 100, verbosity=2)
print(f"clientes atendidos: {vector1}")
print(f"clientes esperando...: {vector2}")