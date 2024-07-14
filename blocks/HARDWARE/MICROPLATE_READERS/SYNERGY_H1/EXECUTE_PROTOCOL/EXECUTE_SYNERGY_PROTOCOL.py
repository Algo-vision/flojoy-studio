from  flojoy import  flojoy, Boolean,File
from PYTHON.utils.synergy_gen_5_handler.execute_loaded_protocol import execute_loaded_protocol


@flojoy
def EXECUTE_SYNERGY_PROTOCOL(protocol_loaded:Boolean) -> Boolean:
    ret = execute_loaded_protocol()
    return Boolean(b=ret)