from  PYTHON.utils.opentrons_http_client.types import OpentronsConfig
import requests


def set_lights_state(server_configuration: OpentronsConfig, lights_state: bool):
    """API call fro playng a created run on the OT-2.

    Args:
        server_configuration (OpentronsConfig): OT-2 server configuration
        run_uuid (str): UUID of the run to be played.
    """
    res = requests.post(
        url=f"{server_configuration.server_address}/robot/lights",
        headers=server_configuration.default_headers,
        json={"on": lights_state},
    )
    return res.status_code == 200
