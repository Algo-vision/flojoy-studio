from  flojoy import  flojoy, Boolean,DataContainer
from PYTHON.utils.synergy_gen_5_handler.gen5_manager import GEN5_MANAGER
from typing import Optional
@flojoy
def EXECUTE_SYNERGY_PROTOCOL(protocol_loaded:Boolean,
                             default: Optional[DataContainer] = None,) -> Boolean:
    ret = GEN5_MANAGER.execute_loaded_protocol()
    return Boolean(b=ret)