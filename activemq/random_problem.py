import json
import random


class RandomProblem:

    _OPERATION_TO_FUNCTION = {
        0: lambda x, y: x + y,
        1: lambda x, y: x - y,
        2: lambda x, y: x * y,
        3: lambda x, y: x / y
    }

    _LOWER_BOUND_SAMPLE = 1
    _UPPER_BOUND_SAMPLE = 1000

    def __init__(self):
        self._x = None
        self._y = None
        self._op = None
        self._made = False

    def make(self):

        if not self._made:
            self._x = random.randint(self._LOWER_BOUND_SAMPLE, self._UPPER_BOUND_SAMPLE)
            self._y = random.randint(self._LOWER_BOUND_SAMPLE, self._UPPER_BOUND_SAMPLE)
            self._op = random.randint(0, len(self._OPERATION_TO_FUNCTION) - 1)
        else:
            raise ValueError()

        self._made = True

    def serialize(self):
        if self._made:
            return json.dumps({'x': self._x, 'y': self._y, 'op': self._op})

        raise ValueError()

    def deserialize(self, data):

        if self._made:
            raise ValueError()

        data = json.loads(data)

        self._x = data['x']
        self._y = data['y']
        self._op = data['op']

        self._made = True

    def solve(self):
        if self._made:
            return self._OPERATION_TO_FUNCTION[self._op](self._x, self._y)

        raise ValueError()
