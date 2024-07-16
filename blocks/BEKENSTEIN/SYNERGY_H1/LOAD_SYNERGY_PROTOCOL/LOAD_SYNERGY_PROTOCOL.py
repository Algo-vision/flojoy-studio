from  flojoy import  flojoy, Boolean,File
from PYTHON.utils.synergy_gen_5_handler.gen5_manager import GEN5_MANAGER


@flojoy
def LOAD_SYNERGY_PROTOCOL(protocol_file: File,
                          gen_5_connection_status:Boolean) -> Boolean:
    GEN5_MANAGER.create_experiment_and_load_protocol(protocol_file.unwrap())
    return Boolean(b=True)