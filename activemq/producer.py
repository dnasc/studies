import sys
import time

import stomp

import configuration
from random_problem import RandomProblem

NUM_PROBLEMS = 1000


def main():
    host_and_ports = [(configuration.HOST, configuration.PORT)]

    connection = stomp.Connection(host_and_ports=host_and_ports)
    connection.set_listener('', stomp.PrintingListener())

    connection.connect(username='admin', passcode='password', wait=True)
    # connection.begin(transaction='123')
    while True:
        rp = RandomProblem()
        rp.make()
        connection.send(body=rp.serialize(), destination=f'/queue/{configuration.QUEUE}')

    time.sleep(2)
    # connection.abort(transaction='123')
    connection.disconnect()


if __name__ == '__main__':
    sys.exit(main())
