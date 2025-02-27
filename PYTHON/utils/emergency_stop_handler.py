from typing import Callable
import asyncio

async def exec_non_async(func:Callable):
    func()
class __EmergencyStopHandler:
    stop_methods:list[Callable]
    def __init__(self):
        self.stop_methods = []
    def STOP_ALL(self):
        asyncio.create_task(self.stop_all_async())
    def register(self,stop_method:Callable):
        self.stop_methods.append(stop_method)
    

    async def stop_all_async(self):
        async with asyncio.TaskGroup() as task_group:
            for method in self.stop_methods:
                task_group.create_task(exec_non_async(method))
    


EmergencyStopHandler = __EmergencyStopHandler()