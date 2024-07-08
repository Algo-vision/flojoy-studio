from pathlib import Path
import requests
import json
from  PYTHON.utils.opentrons_http_client.types import OpentronsConfig
import uuid


def upload_protocol(protocol_file_path: str, server_config: OpentronsConfig):
    """API call for uploading JSON or Python protocol files to OT-2.

    Args:
        protocol_file_path (Path): Python or JSON protocol file path
        server_config (OpentronsConfig): OT-2 server configuration

    Returns:
        str: Server generaed UUId of the uploded protocol.
    """
    protocol_uuid = str(uuid.uuid4())
    res = requests.post(
        url=f"{server_config.server_address}/protocols",
        headers=server_config.default_headers,
        files={"files": open(protocol_file_path,"rb")},
        data={"key": protocol_uuid},
    )
    respones_parsed = json.loads(res._content)
    created_protocol_uuid = respones_parsed["data"]["id"]
    return created_protocol_uuid
