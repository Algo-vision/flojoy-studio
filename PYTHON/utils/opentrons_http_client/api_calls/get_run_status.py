from  PYTHON.utils.opentrons_http_client.types import OpentronsConfig
import requests
import json

def get_run_status(server_configuration: OpentronsConfig, run_uuid: str):
    """API call fro playng a created run on the OT-2.

    Args:
        server_configuration (OpentronsConfig): OT-2 server configuration
        run_uuid (str): UUID of the run to be played.
    """
    res = requests.get(
        url=f"{server_configuration.server_address}/runs/{run_uuid}",
        headers=server_configuration.default_headers,
    )
    res_parsed = json.loads(res._content)
    res_status= res_parsed['data']['status']
    return res_status
