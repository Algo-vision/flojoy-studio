from typing import NamedTuple


class OpentronsConfig(NamedTuple):
    server_address: str
    default_headers: dict[str, str] = {"Opentrons-Version": "*"}
