from PYTHON.utils.synergy_gen_5_handler.Gen5_py import (
    constants,
    Application,
    IApplication,
    IExperiment,
    IPlates,
    IPlate
)
from .kill_gen5_instances import kill_gen5_instances
__all__  = ['Gen5Manager']

class __Gen5Manager:
    gen5_app: IApplication
    CURRENT_EXP: IExperiment

    def __init__(self) -> None:
        pass

    def init(self):
        kill_gen5_instances()
        self.gen5_app = Application()
        self.CURRENT_EXP = None
        self.gen5_app.ConfigureUSBReader(16, "")
        self.gen5_app.CarrierIn()
        self.gen5_app.CarrierOut()
        return True

    def is_initialized(self):
        return self.gen5_app is not None

    def create_experiment_and_load_protocol(self, protocol_file: str):
        if not self.is_initialized():
            raise (Exception("Gen5APP not initialized"))
        if self.CURRENT_EXP is not None:
            self.CURRENT_EXP.Close()
        self.CURRENT_EXP = self.gen5_app.NewExperiment(protocol_file)

    def execute_loaded_protocol(self):
        if self.is_initialized() is None:
            raise(Exception("Gen5APP not initialized"))
        if self.CURRENT_EXP is None:
            raise(Exception("Experiment not loaded "))
        plates:IPlates = self.CURRENT_EXP.Plates
        plate:IPlate = plates.GetPlate(1)
        read = plate.StartRead
        while plate.ReadStatus == constants.eReadInProgress:
            ...
        if plate.ReadStatus == constants.eReadCompleted:
            return True
        else:
            return False
    
    def export_results_to_file(self,excel_output_path:str):
        if self.is_initialized() is None:
            raise(Exception("Gen5APP not initialized"))
        if self.CURRENT_EXP is None:
            raise(Exception("Experiment not loaded "))
        plates:IPlates = self.CURRENT_EXP.Plates
        plate:IPlate = plates.GetPlate(1)
        if plate.ReadStatus == constants.eReadCompleted:
            plate.PowerExportEx("", excel_output_path)
            return True
        else:
            raise(Exception("Reading is not completed. cannot export excel."))    
        
GEN5_MANAGER = __Gen5Manager()