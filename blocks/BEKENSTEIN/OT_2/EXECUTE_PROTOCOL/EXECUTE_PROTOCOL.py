from typing import Optional
from flojoy import String, flojoy, String, File, DataContainer, Directory
from PYTHON.utils.opentrons_http_client.api_calls import *
from PYTHON.utils.opentrons_http_client import scan_for_labware_files
from PYTHON.utils.opentrons_http_client.types.opentrons_config import OpentronsConfig
from pathlib import Path

@flojoy
def EXECUTE_PROTOCOL(
    ip_address: String,
    ot_2_protocol_file: File,
    ot_2_custom_labware_directory: Directory,
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
    cfg = OpentronsConfig(server_address=ip_address.s)
    custom_labware_files:list[Path] = scan_for_labware_files(labware_directory=Path(ot_2_custom_labware_directory.unwrap()))
    protocol_uuid = upload_protocol(
        server_config=cfg,
        protocol_file_path=ot_2_protocol_file.unwrap(),
        labware_files = custom_labware_files
    )
    run_uuid = create_run_with_protocol(server_config=cfg, protocol_uuid=protocol_uuid)
    play_a_run(server_configuration=cfg, run_uuid=run_uuid)
    status = ""
    while status != 'succeeded':
       status =  get_run_status(server_configuration=cfg,run_uuid=run_uuid)
    return String(s=ip_address.s)
