from flojoy import String
from xarm.wrapper import XArmAPI 

from PYTHON.utils.mecademic_state.mecademic_mock import MockRobot
from PYTHON.utils.emergency_stop_handler import EmergencyStopHandler
_robot_handle_map = None

def get_robot_handle_map():
    global _robot_handle_map
    if _robot_handle_map is None:
        _robot_handle_map = {}
    return _robot_handle_map


def init_handle_map(allow_reinit: bool = False):
    global _robot_handle_map
    if _robot_handle_map is not None and not allow_reinit:
        raise ValueError("Robot handle map already initialized.")
    if _robot_handle_map is not None:
        for ip_address, rbt in _robot_handle_map.items():
            _robot_handle_map[ip_address].disconnect()
    _robot_handle_map = None


def query_for_handle(ip_address: str | String) -> XArmAPI| None:
    """
    Queries the robot handle map for a handle with the given IP address.
    If a handle is not found, a new handle is created and added to the map.
    """
    if isinstance(ip_address, String):
        ip_address: str = ip_address.s  # unbox String
    robot_handle_map = get_robot_handle_map()
    if ip_address in robot_handle_map:
        return robot_handle_map[ip_address]
    else:
        raise KeyError("No handle for IP address: " + ip_address)


def add_handle(ip_address: str):
    """
    Adds a handle to the robot handle map.
    TODO: This is blocking synchronous code. Migrate to async await.
    """
    if ip_address in get_robot_handle_map():
        return

    robot_handle_map = get_robot_handle_map()
    robot = XArmAPI(ip_address)
    robot_handle_map[ip_address] = robot
    def emergency_stop():
        robot.emergency_stop()
        
    EmergencyStopHandler.register(emergency_stop)


def add_mock_handle(ip_address: str):
    """
    Adds a handle to the robot handle map which does not connect to a real robot. Used for testing.
    """
    if ip_address in get_robot_handle_map():
        raise ValueError("Robot handle already exists for IP address: " + ip_address)

    robot_handle_map = get_robot_handle_map()
    robot = MockRobot(ip_address=ip_address)
    robot_handle_map[ip_address] = robot


def remove_handle(ip_address: str):
    """
    Removes a handle from the robot handle map.
    """
    if ip_address not in get_robot_handle_map():
        raise ValueError("Robot handle does not exist for IP address: " + ip_address)

    robot_handle_map = get_robot_handle_map()
    robot_handle_map[ip_address].disconnect()
    del robot_handle_map[ip_address]


def destruct_handle_map():
    """
    Disconnects all robot handles and deletes the robot handle map.
    TODO: Warning! This destruct must ALWAYS be called on closing or crashing of the program.
    """
    robot_handle_map = get_robot_handle_map()
    for ip_address in robot_handle_map:
        robot_handle_map[ip_address].disconnect()
    del robot_handle_map

init_handle_map()