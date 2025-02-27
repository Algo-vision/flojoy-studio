from  PYTHON.utils.opentrons_http_client.types import OpentronsConfig
import requests

import json

def stop_current_run(server_configuration: OpentronsConfig):
    """API call fro playng a created run on the OT-2.

    Args:
        server_configuration (OpentronsConfig): OT-2 server configuration
        run_uuid (str): UUID of the run to be played.
    """
    res = requests.get(
        url=f"{server_configuration.server_address}/runs",
        headers=server_configuration.default_headers,
    )
    parsed_res = json.loads(res._content)
    current_run_link = parsed_res['links']['current']['href']

    res = requests.post(
        url=f"{server_configuration.server_address}{current_run_link}/actions",
        headers=server_configuration.default_headers,
        json={"data": {"actionType": "stop"}},
    )
