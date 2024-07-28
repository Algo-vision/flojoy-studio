from flojoy import String, flojoy
from PYTHON.utils.xarm_manager.xarm_manager import (
    add_handle,
    init_handle_map,
    query_for_handle,
)


@flojoy
def XARM_CONNECT(ip_address: str) -> String:
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
    # init_handle_map(allow_reinit=False)
    add_handle(ip_address)

    robot = query_for_handle(ip_address)
    if robot.clean_warn() == 3:
        raise Exception("check xarm")
    robot.clean_error()
    robot.motion_enable(True)
    robot.set_mode(0)
    robot.set_state(0)
    cur_servo_agnle = robot.get_position()
    cur_servo_agnle = cur_servo_agnle[1]
    cur_servo_agnle[0] +=50
    robot.set_position(*cur_servo_agnle, speed=100, radius=0.0, wait=True)
    cur_servo_agnle = robot.get_position()
    cur_servo_agnle = cur_servo_agnle[1]
    cur_servo_agnle[0] -=50
    robot.set_position(*cur_servo_agnle, speed=100, radius=0.0, wait=True)
    return String(s=ip_address)
