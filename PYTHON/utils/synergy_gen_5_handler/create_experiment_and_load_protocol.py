from .gen5_manager import gen5_app
from .Gen5_py import IExperiment
CURRENT_EXP:IExperiment = None
def create_experiment_and_load_protocol(protocol_file:str):
    global CURRENT_EXP
    if gen5_app is None:
        raise(Exception("Gen5APP not initialized"))
    if CURRENT_EXP is not None:
        CURRENT_EXP.Close()
    CURRENT_EXP = gen5_app.NewExperiment(protocol_file)
    