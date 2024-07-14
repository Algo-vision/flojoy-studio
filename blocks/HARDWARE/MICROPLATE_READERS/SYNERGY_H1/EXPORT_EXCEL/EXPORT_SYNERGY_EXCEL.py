from  flojoy import  flojoy, Boolean,Directory,String
from PYTHON.utils.synergy_gen_5_handler.export_results_to_file import export_results_to_file
import datetime
import os.path
import os
@flojoy
def EXECUTE_SYNERGY_PROTOCOL(output_directory:Directory,
                             experiment_name:str) -> Boolean:
    os.makedirs(output_directory.unwrap(),exist_ok=True)
    current_time = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    output_file_path = os.path.join(output_directory.unwrap(),f"{current_time}_{experiment_name}.xlsx") 
    ret = export_results_to_file(output_file_path)
    if ret:
        return String(s=output_file_path)