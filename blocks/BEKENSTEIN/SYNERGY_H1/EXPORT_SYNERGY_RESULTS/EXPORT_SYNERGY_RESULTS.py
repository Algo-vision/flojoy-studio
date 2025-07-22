from  flojoy import  flojoy, Boolean,Directory,String
from PYTHON.utils.synergy_gen_5_handler.gen5_manager import GEN5_MANAGER
import datetime
import os.path
import tempfile 
@flojoy
def EXPORT_SYNERGY_RESULTS(output_directory:Directory,
                             experiment_name:str,
                             is_measure_completed:Boolean) -> String:
    """The EXPORT_SYNERGY_RESULTS exports the latest run result to a specific directory.
  
    Returns the newly created file path .

    Parameters
    ----------
    output_directory : Directory
        Desired location for writing results
    experiment_name : str
        User selected unique experiment name
    is_measure_completed : Boolean
        REcive signal for run finish.

    Returns
    -------
    DataContainer
      String: Newly created results excel file absolute path.
    """
    
    os.makedirs(output_directory.unwrap(),exist_ok=True)
    current_time = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    output_file_path  = (output_directory.unwrap()+os.sep+f"{current_time}_{experiment_name}.xlsx").replace("/","\\")
    print(output_file_path,flush=True)
    ret = GEN5_MANAGER.export_results_to_file(output_file_path)
    if ret:
        return String(s=output_file_path)
