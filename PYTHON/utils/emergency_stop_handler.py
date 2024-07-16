from typing import Callable
class __EmergencyStopHandler:
    stop_methods:list[Callable]
    def __init__(self):
        self.stop_methods = []
    def STOP_ALL(self)
        for method in self.stop_methods:
            method()
    def register(self,stop_method:Callable):
        self.stop_methods.append(stop_method)


EmergencyStopHandler = __EmergencyStopHandler()