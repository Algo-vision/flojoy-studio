# Notes on the project


The backend is made of 3 parts:
* FastAPI server "captain" - RESTful service that listens to the frontend and executes user command (*e.g.* run pipeline, load block, retrieve outputs)
* Blocks - dynamically loaded python block to be executed in the pipeline. The block inputs are defined using type annotations:

    In order to define block inputs you will use 'DataContainer' Flojoy type and its successor types. Same for block output.

    In Order to specify the settings that are selected by the user via the GUI before the pipeline runs (such as file picker, number picker etc.), use flojoy.parameteer_type types or primitives.

* Python modules and utils located under `PYTHON`
    - Synergy H1 - 

        A python package for controlling the Synergy    H1 device is located in `./PYTHON/utils/   synergy_gen_5_handler`.

        The package is made of 2 parts:
        * PythonCOM wrapper around the Gen5 software    using win32com library.
        * Gen5manager: A singleton class that manages   the state of the gen5 software instance and   controls the H1 device.
        * ##### IMPORTANT! the Gen5 software must be    installed before and have a valid license in   order to run. Also, during installation of    Gen5 software it is needed that to OLE COM     interface will be installed to windows (using   a checkbox during installation)
    - OT-2 manager - a python pacakge for controlling the OT-2 liquid handler. 
    
        The communication to the liquid handler is done using HTTP rest api calls.
        The API has no documentation and it has to be sniffed in order to dermine its logic.
        Though it is not documented, you may access the API specs by visiting `http://<ot2-ip>:/docs`. Also the source code of the robot server(the code that runs on the robot itself) may be found here : https://github.com/Opentrons/opentrons/tree/edge/robot-server


    - Xarm Manager - a registry for the loaded xarm devices. Each time you connect to a device (for example by calling the XARM_CONECT block) it registers the connected device in the registry and let you call it form other blocks of software by its name.
    In order to execute xarm preloaded protocol we use python module loading mechanism. The loded file contains a class named `RobotMain` which needed to be instantiated with the xarm device instance as argument. After instantiation you may call ROBOTMain.run() in order to execute the protocol. Look in the XARM/EXECUTE_PATH block in order to see it in use.

    Also there is an emergency stop handler that get executed when pressing the Cancel button. If you implement some code block that might need to be terminated immediately, don't forget to implement "terminate()" method and register it in the emergency stop registry!


## Building the project for installation

In order to create installation executable of the whole project, open an administrator privileged PowerShell terminal, navigate to the repository directory and run:

`pnpm run electron-package:windows`

It will build the project and generate installation file in 'dist' directory.
