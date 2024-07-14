from  flojoy import  flojoy,Boolean
from PYTHON.utils.synergy_gen_5_handler.gen5_manager import initialize_gen5, gen5_app


@flojoy
def SYNERGY_H1_CONNECT() -> Boolean:
    initialize_gen5()
    return Boolean(b=True)
