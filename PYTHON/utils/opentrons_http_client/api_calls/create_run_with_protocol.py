from PYTHON.utils.opentrons_http_client.types import OpentronsConfig
import requests

import json


def create_run_with_protocol(server_config: OpentronsConfig, protocol_uuid: str):
    """ API call for creating OT-2 run based on uploaded protocol

    Args:
        server_config (OpentronsConfig): server configuration
        protocol_uuid (str): UUID of the uploaded protocol. recieved from server upon protocol uploading

    Returns:
        str: Run UUID. Generated by server.
    """    
    res = requests.post(
        url=f"{server_config.server_address}/runs",
        headers=server_config.default_headers,
        json={"data": {"protocolId": protocol_uuid}},
    )
    run_creation_response_parsed = json.loads(res._content)
    run_id = run_creation_response_parsed["data"]["id"]
    return run_id
