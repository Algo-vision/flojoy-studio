from .gen5_manager import gen5_app
from .Gen5_py import IPlates,IPlate,constants
from .create_experiment_and_load_protocol import CURRENT_EXP

def export_results_to_file(excel_output_path:str):
    if gen5_app is None:
        raise(Exception("Gen5APP not initialized"))
    if CURRENT_EXP is None:
        raise(Exception("Experiment not loaded "))
    plates:IPlates = CURRENT_EXP.Plates
    plate:IPlate = plates.GetPlate(1)
    if plate.ReadStatus == constants.eReadCompleted:
        plate.PowerExportEx("", excel_output_path)
        return True
    else:
        raise(Exception("Reading is not completed. cannot export excel."))    