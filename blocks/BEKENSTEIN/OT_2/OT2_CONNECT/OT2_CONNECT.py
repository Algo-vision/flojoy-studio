from flojoy import String, flojoy
from PYTHON.utils.opentrons_http_client.api_calls import *
from PYTHON.utils.opentrons_http_client.types.opentrons_config import OpentronsConfig
import time
from PYTHON.utils.emergency_stop_handler import EmergencyStopHandler
from PYTHON.utils.opentrons_http_client.zeroconfig_ot_2_detector import detector,found_devices
@flojoy
def OT2_CONNECT() -> String:
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
    if len(found_devices) >= 1:
        ot_2_dev = found_devices[0]
        cfg =OpentronsConfig(server_address="http://"+ot_2_dev)
    else:
        raise Exception("No OT2 devices Connected")
    set_lights_state(cfg,lights_state=False)
    time.sleep(0.5)
    set_lights_state(cfg,lights_state=True)
    def stop_ot_current_run():
        stop_current_run(cfg)
    EmergencyStopHandler.register(stop_ot_current_run)
    return String(s="http://"+ot_2_dev)
