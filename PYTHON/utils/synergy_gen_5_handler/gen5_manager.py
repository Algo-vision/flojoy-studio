from PYTHON.utils.synergy_gen_5_handler.Gen5_py import constants,Application,IApplication
from .kill_gen5_instances import kill_gen5_instances
gen5_app = None
is_gen5_initialized = False
def initialize_gen5():
    global gen5_app
    kill_gen5_instances()
    gen5_app: IApplication = Application()

    gen5_app.ConfigureUSBReader(16,"")
    gen5_app.CarrierIn()
    gen5_app.CarrierOut()
    return True