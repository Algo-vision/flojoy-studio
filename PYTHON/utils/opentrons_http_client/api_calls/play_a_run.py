from  PYTHON.utils.opentrons_http_client.types import OpentronsConfig
import requests


def play_a_run(server_configuration: OpentronsConfig, run_uuid: str):
    """API call fro playng a created run on the OT-2.

    Args:
        server_configuration (OpentronsConfig): OT-2 server configuration
        run_uuid (str): UUID of the run to be played.
    """
    res = requests.post(
        url=f"{server_configuration.server_address}/runs/{run_uuid}/actions",
        headers=server_configuration.default_headers,
        json={"data": {"actionType": "play"}},
    )
