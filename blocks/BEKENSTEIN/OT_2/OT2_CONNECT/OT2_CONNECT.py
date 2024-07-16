from flojoy import String, flojoy
from PYTHON.utils.opentrons_http_client.api_calls import *
from PYTHON.utils.opentrons_http_client.types.opentrons_config import OpentronsConfig
import time
from PYTHON.utils.emergency_stop_handler import EmergencyStopHandler
@flojoy
def OT2_CONNECT(ip_address: str) -> String:
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
    
    cfg = OpentronsConfig(server_address=ip_address)
    set_lights_state(cfg,lights_state=False)
    time.sleep(0.5)
    set_lights_state(cfg,lights_state=True)
    def stop_ot_current_run():
        stop_current_run(cfg)
    EmergencyStopHandler.register(stop_ot_current_run)
    return String(s=ip_address)
