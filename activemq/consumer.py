import hashlib
import sys
import multiprocessing as mp
import threading

import stomp

import configuration
from random_problem import RandomProblem


class Listener(stomp.ConnectionListener):

    def on_message(self, frame):
        rp = RandomProblem()
        rp.deserialize(frame.body)
        rp.solve()


def loop():
    host_and_ports = [(configuration.HOST, configuration.PORT)]

    connection = stomp.Connection(host_and_ports=host_and_ports)
    connection.set_listener('', Listener())
    connection.connect()
    connection.subscribe(f'/queue/{configuration.QUEUE}', hashlib.md5().hexdigest())

    while True:
        pass

    connection.disconnect()


def main():

    processes = [mp.Process(target=loop) for _ in range(8)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    sys.exit(main())
