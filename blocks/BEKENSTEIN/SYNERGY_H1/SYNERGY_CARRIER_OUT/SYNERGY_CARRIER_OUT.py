from  flojoy import  flojoy,Boolean
from PYTHON.utils.synergy_gen_5_handler.gen5_manager import GEN5_MANAGER


@flojoy
def SYNERGY_CARRIER_OUT() -> Boolean:
    GEN5_MANAGER.open_tray()
    return Boolean(b=True)
