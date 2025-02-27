from typing import Optional
from flojoy import String, flojoy, String, Directory, File,Scalar,OrderedPair
from PYTHON.utils.opentrons_http_client.api_calls import *
from PYTHON.utils.opentrons_http_client.types.opentrons_config import OpentronsConfig
import importlib
import pandas as pd

@flojoy
def TEST_VIS_EXCEL(
    excel_file_path: File,
) -> OrderedPair:
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
    OrderedPair
       results for well
    """
    data = pd.read_excel(excel_file_path.unwrap())
    data_x = data.iloc[23:424,1]
    data_y = data.iloc[23:424,2]
    x = data_x.to_numpy()
    y = data_y.to_numpy()
    return OrderedPair(x = x, y=y)
