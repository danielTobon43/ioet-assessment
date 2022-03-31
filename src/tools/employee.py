class Employee(object):
    """docstring for Employee"""

    def __init__(self, name: str, rawtime: str):
        self.name = name
        self.rawtime = rawtime

    def set_workingtime(self, workingtime: tuple):
        self.workingtime = workingtime

    def set_start_time(self, start_time: str):
        self.start_time = start_time

    def set_end_time(self, end_time: str):
        self.end_time = end_time

    def set_day(self, day: str):
        self.day = day

    def __str__(self):
        return f'class: {self.__class__.__name__} {self.__dict__}'
