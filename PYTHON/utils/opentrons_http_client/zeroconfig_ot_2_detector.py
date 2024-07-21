import socket
from zeroconf import ServiceListener,Zeroconf,ServiceBrowser

found_devices = []
class ZeroConfigOT2Detector:
    def __init__(self) -> None:
        zeroconf = Zeroconf()
        self.listener = OT2Listener()
        browser = ServiceBrowser(zeroconf, "_http._tcp.local.",self.listener)
    def get_listed_devices(self):
        return self.listener.ot_2_services_list

class OT2Listener(ServiceListener):
    def __init__(self):
        self.ot_2_services_list = []
    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} updated")

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} removed")
    
    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        # print(f"Service {name} added, service info: {info}")
        print("Service %s added, IP address: %s ,port %s" % (name, socket.inet_ntoa(info.addresses[0]),info.port))
        if "OT2" in name:
            found_devices.append(f"{socket.inet_ntoa(info.addresses[0])}:{info.port}")


detector = ZeroConfigOT2Detector()