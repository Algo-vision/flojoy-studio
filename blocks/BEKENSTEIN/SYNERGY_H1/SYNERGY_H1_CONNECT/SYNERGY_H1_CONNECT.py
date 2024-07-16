from  flojoy import  flojoy,Boolean
from PYTHON.utils.synergy_gen_5_handler.gen5_manager import GEN5_MANAGER


@flojoy
def SYNERGY_H1_CONNECT() -> Boolean:
    GEN5_MANAGER.init()
    return Boolean(b=True)
