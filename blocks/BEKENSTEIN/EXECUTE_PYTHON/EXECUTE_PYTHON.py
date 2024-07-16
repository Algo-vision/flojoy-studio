from typing import Optional
from flojoy import String, flojoy, String, Directory, DataContainer, File
from PYTHON.utils.opentrons_http_client.api_calls import *
from PYTHON.utils.opentrons_http_client.types.opentrons_config import OpentronsConfig
import importlib


@flojoy
def EXECUTE_PYTHON(
    python_file: File,
    excel_file_path: String,
    output_dir: Directory,
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
    spec = importlib.util.spec_from_file_location("analize", python_file.unwrap())

    # creates a new module based on spec
    analize = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(analize)
    analize.analize(excel_file_path.s,output_dir.unwrap())

    
