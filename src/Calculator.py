from CsvReader import CsvReader


def addition(a, b):
    return a + b


def subtraction(a, b):
    a = int(a)
    b = int(b)
    return b - a


def mean(data):
    mean = data
    return mean


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result


class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass

    def mean(self):
        mean(self.data)