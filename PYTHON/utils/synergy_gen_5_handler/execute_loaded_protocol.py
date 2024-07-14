from .gen5_manager import gen5_app
from .Gen5_py import IPlates,IPlate,constants
from .create_experiment_and_load_protocol import CURRENT_EXP
def execute_loaded_protocol():
    if gen5_app is None:
        raise(Exception("Gen5APP not initialized"))
    if CURRENT_EXP is None:
        raise(Exception("Experiment not loaded "))
    plates:IPlates = CURRENT_EXP.Plates
    plate:IPlate = plates.GetPlate(1)
    read = plate.StartRead
    while plate.ReadStatus == constants.eReadInProgress:
        ...
    if plate.ReadStatus == constants.eReadCompleted:
        return True
    else:
        return False
    