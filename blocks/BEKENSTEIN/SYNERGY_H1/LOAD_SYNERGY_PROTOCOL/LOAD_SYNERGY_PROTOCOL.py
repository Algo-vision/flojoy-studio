from  flojoy import  flojoy, Boolean,File,DataContainer
from typing import Optional
from PYTHON.utils.synergy_gen_5_handler.gen5_manager import GEN5_MANAGER


@flojoy
def LOAD_SYNERGY_PROTOCOL(protocol_file: File,
                          default: Optional[DataContainer] = None,) -> Boolean:
    GEN5_MANAGER.create_experiment_and_load_protocol(protocol_file.unwrap())
    return Boolean(b=True)