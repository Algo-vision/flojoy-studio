from typing import Optional
from flojoy import String, flojoy, String, File, DataContainer
from PYTHON.utils.xarm_manager.xarm_manager import query_for_handle

import importlib


@flojoy
def EXECUTE_PATH(
    ip_address: String,
    robot_pth_file: File,
    default: Optional[DataContainer] = None,
) -> String:
    """
    The CONNECT node establishes a connection to the Mecademic robot arm via HTTP and activates the robot arm. The IP Address to use is the same one that is used to access the Mecademic web interface. Example: 192.168.0.100

    Parameters
    ----------
    ip_address : str
        The IP address of the robot arm.
    simulator : bool
        Whether to activate the simulator or not. Defaults to False.


    Returns
    -------
    String
       The IP address of the robot arm, used in other Mecademic nodes to establish which arm they are communicating with.
    """

    arm = query_for_handle(ip_address.s)

    spec = importlib.util.spec_from_file_location("xarm", robot_pth_file.unwrap())

    # creates a new module based on spec
    xarm = importlib.util.module_from_spec(spec)

    # executes the module in its own namespace
    # when a module is imported or reloaded.
    spec.loader.exec_module(xarm)
    robot = xarm.RobotMain(arm)
    robot.run()
    while(arm.get_state()[1] == 1):
        ...

    return String(s=ip_address.s)
