from  flojoy import  flojoy, Boolean,File
from PYTHON.utils.synergy_gen_5_handler.create_experiment_and_load_protocol import create_experiment_and_load_protocol


@flojoy
def LOAD_SYNERGY_PROTOCOL(protocol_file: File,
                          gen_5_connection_status:Boolean) -> Boolean:
    create_experiment_and_load_protocol(protocol_file.unwrap())
    return Boolean(b=True)