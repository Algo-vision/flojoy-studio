import { Fragment, useCallback, useEffect, useState } from "react";
import { SetupStatus } from "@/renderer/types/status";
import SetupStep from "@/renderer/components/index/SetupStep";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/renderer/components/ui/alert-dialog";
import { Button } from "@/renderer/components/ui/button";
import { useNavigate } from "react-router-dom";
import StatusBar from "@/renderer/routes/common/StatusBar";
import { InterpretersList } from "src/main/python/interpreter";
import {  useManifestStore, useMetadata } from "@/renderer/stores/manifest";
import { Console } from "console";


export const Index = (): JSX.Element => {
  const  manifest_store = useManifestStore();
  const metadata = useMetadata();
  const [manifest_interval,setManifestInterval] = useState(null);
  const [waitForManifest,setWaitForManifest] = useState(false);

  
  const [pyInterpreters, setPyInterpreters] = useState<InterpretersList | null>(
    null,
  );
  const [selectedInterpreter, setSelectedInterpreter] = useState("");
  const [setupStatuses, setSetupStatuses] = useState<SetupStatus[]>([
    {
      status: "running",
      stage: "check-python-installation",
      message: "Check for python ~3.11 installation.",
    },
    {
      status: "pending",
      stage: "install-dependencies",
      message: "Configure all the magic behind Flojoy Studio.",
    },
    {
      status: "pending",
      stage: "spawn-captain",
      message: "Start the Flojoy Studio backend.",
    },
  ]);

  const [showError, setShowError] = useState<boolean>(false);
  const [errorTitle, setErrorTitle] = useState<string>("");
  const [errorDesc, setErrorDesc] = useState<string>("");
  const [errorActionName, setErrorActionName] = useState<string>("");
  const navigate = useNavigate();

  const checkPythonInstallation = useCallback(
    async (force?: boolean): Promise<void> => {
      try {
        const interpreters = await window.api.checkPythonInstallation(force);
        if (interpreters.length > 0) {
          const interpreter =
            interpreters.find((i) => i.default) ?? interpreters[0];
          setSelectedInterpreter(interpreter.path);
          await window.api.setPythonInterpreter(interpreter.path);
          updateSetupStatus({
            stage: "check-python-installation",
            status: "completed",
            message: `Python v${interpreter.version.major}.${interpreter.version.minor} found!`,
          });
          return;
        }
        setPyInterpreters([]);
        updateSetupStatus({
          stage: "check-python-installation",
          status: "running",
          message: "No Python 3.11 interpreter found!",
        });
      } catch (err) {
        console.log("err: ", err);
        updateSetupStatus({
          stage: "check-python-installation",
          status: "error",
          message:
            "Cannot find any Python 3.11 installation on this machine :(",
        });
        setErrorTitle("Could not find Python 3.11 :(");
        setErrorDesc("Please install Python 3.11 and try again!");
        setErrorActionName("Download");
      }
    },
    [],
  );

  const installDependencies = useCallback(async (): Promise<void> => {
    try {
      // await window.api.installPipx();
      // await window.api.pipxEnsurepath();
      // await window.api.installPoetry();
      await window.api.installDependencies();

      updateSetupStatus({
        stage: "install-dependencies",
        status: "completed",
        message: "Finished setting up all the magic behind Flojoy Studio.",
      });
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (err: any) {
      updateSetupStatus({
        stage: "install-dependencies",
        status: "error",
        message: "Something went wrong when installing dependencies...",
      });
      setErrorTitle("Something went wrong :(");
      // sendEventToMix(MixPanelEvents.setupError, {
      //   stage: "install-dependencies",
      //   message: err.message,
      //   error: String(err),
      //   logs: await window.api.getAllLogs(),
      // });
      setErrorDesc(
        "Sorry about that! Please open the log folder and send the log to us on Discord!",
      );
      setErrorActionName("Open Log Folder");
    }
  }, []);

  const spawnCaptain = useCallback(async (): Promise<void> => {
    try {
      await window.api.spawnCaptain();
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (err: any) {
      updateSetupStatus({
        stage: "spawn-captain",
        status: "error",
        message: "Something went wrong when starting Flojoy Studio...",
      });
      setErrorTitle("Failed to spawn captain!");
      // sendEventToMix(MixPanelEvents.setupError, {
      //   stage: "spawn-captain",
      //   message: err.message,
      //   error: String(err),
      //   logs: await window.api.getAllLogs(),
      // });
      setErrorDesc(
        "Sorry about that! Please open the log folder and send the log to us on Discord!",
      );
      setErrorActionName("Open Log Folder");
    }
  }, []);

  const handleSelectedPyInterpreter = async (interpreter: string) => {
    await window.api.setPythonInterpreter(interpreter);
    setSelectedInterpreter(interpreter);
    updateSetupStatus({
      stage: "check-python-installation",
      status: "completed",
      message: `Using selected python env...`,
    });
  };

  const handleBrowsePyInterpreter = async () => {
    const path = await window.api.browsePyInterpreter();
    if (path) {
      handleSelectedPyInterpreter(path);
    }
  };
  const refreshPyList = async () => {
    console.log("Refreshing python interpreter list...");
    await checkPythonInstallation(true);
  };

  const errorAction = async (): Promise<void> => {
    const setupError = setupStatuses.find(
      (status) => status.status === "error",
    );
    switch (setupError?.stage) {
      case "check-python-installation": {
        window.open("https://www.python.org/downloads/release/python-3116/");
        break;
      }
      case "install-dependencies": {
        await window.api.openLogFolder();
        break;
      }
      case "spawn-captain": {
        await window.api.openLogFolder();
        break;
      }
      case "check-blocks-resource": {
        if (window.api.isPackaged()) {
          window.api.restartFlojoyStudio();
        } else {
          alert(
            "Restart is not supported for dev build, please relaunch Flojoy Studio manually!",
          );
        }
        break;
      }
    }
  };

  const updateSetupStatus = (setupStatus: SetupStatus): void => {
    setSetupStatuses((prev) => {
      return prev.map((status) => {
        if (status.stage === setupStatus.stage) {
          return {
            ...setupStatus,
          };
        }
        return status;
      });
    });
  };

  useEffect(() => {
    // Kick off the setup process with this useEffect
    // sendEventToMix(MixPanelEvents.setupStarted);
    checkPythonInstallation();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    // The main logic for the setup process
    const hasError = setupStatuses.find((status) => status.status === "error");
    const isRunning = setupStatuses.find(
      (status) => status.status === "running",
    );
    if (hasError) {
      // no need to trigger the next step if there is an error
      setShowError(true);
      return;
    }
    if (isRunning) {
      // or something is already running...
      return;
    }

    const nextStep = setupStatuses.find(
      (status) => status.status === "pending",
    );
    switch (nextStep?.stage) {
      case "check-python-installation": {
        updateSetupStatus({
          stage: "check-python-installation",
          status: "running",
          message: "Making sure Python 3.11 is installed on this machine.",
        });
        checkPythonInstallation();
        break;
      }
      case "install-dependencies": {
        updateSetupStatus({
          stage: "install-dependencies",
          status: "running",
          message:
            "Working hard to set everything up! This may take a while for the first time...",
        });
        installDependencies();
        break;
      }
      case "spawn-captain": {
        updateSetupStatus({
          stage: "spawn-captain",
          status: "running",
          message: "Almost there, starting Flojoy Studio...",
        });
        setWaitForManifest(true);
        spawnCaptain();
        break;
      }
    }
  }, [
    checkPythonInstallation,
    installDependencies,
    setupStatuses,
    spawnCaptain,
    metadata,
  ]);
  const checkIfManifestArrived = useCallback( ()=>{
    console.log("hit manifest interval");
    if(manifest_store.standardBlocksManifest != undefined && manifest_store.standardBlocksMetadata != undefined){
             navigate("/flowchart");
             setWaitForManifest(false);
             
     }
  },[manifest_store,navigate]);


  useEffect(() => {

    if(waitForManifest){
      
    //Implementing the setInterval method
    const interval = setInterval(checkIfManifestArrived,50);
    return () => clearInterval(interval);
    }
  }, [waitForManifest,checkIfManifestArrived]);

 
  
  return (
    <div className="flex h-screen flex-col bg-muted">
      <div className="flex grow flex-col items-center p-4">
        <div className="py-4"></div>
        <div className="text-4xl font-bold">Welcome to Flojoy Studio!</div>
        <div className="py-1"></div>
        <div className="">
          We are excited to have you here, please give us some time to get
          everything ready :)
        </div>

        <div className="py-4"></div>
        <div className="flex w-full items-center justify-center">
          <div className="w-fit rounded-xl bg-background p-4">
            {setupStatuses.map((status, idx) => (
              <Fragment key={idx}>
                <SetupStep status={status.status} message={status.message} />
                {status.stage === "check-python-installation" &&
                  pyInterpreters && (
                    <div className="flex flex-col items-center justify-center gap-2 px-2 pt-2">
                      {pyInterpreters.length == 0 && (
                        <div>
                          <Button
                            className="px-1 font-bold"
                            variant={"link"}
                            onClick={() =>
                              window.open(
                                "https://www.python.org/downloads/release/python-3116/",
                              )
                            }
                          >
                            Click here
                          </Button>{" "}
                          to download Python 3.11 from official website.
                        </div>
                      )}
                      <div className="flex w-full items-center">
                        <hr className="w-full flex-1 border-t-2 border-gray-300" />
                        <span className="mx-4 text-gray-600">OR</span>
                        <hr className="w-full flex-1 border-t-2 border-gray-300" />
                      </div>
                      <div className="flex w-full items-center justify-center gap-3">
                        <Button
                          onClick={handleBrowsePyInterpreter}
                          disabled={selectedInterpreter !== ""}
                        >
                          Find an interpreter
                        </Button>
                        <Button
                          disabled={selectedInterpreter !== ""}
                          onClick={refreshPyList}
                          size={"sm"}
                        >
                          Retry
                        </Button>
                      </div>
                    </div>
                  )}
              </Fragment>
            ))}
          </div>
        </div>

        <div className="py-4"></div>

        {setupStatuses.find((status) => status.status === "error") && (
          <Button
            onClick={async (): Promise<void> =>
              await window.api.restartFlojoyStudio()
            }
          >
            Retry
          </Button>
        )}

        <AlertDialog open={showError} onOpenChange={setShowError}>
          <AlertDialogContent>
            <AlertDialogHeader>
              <AlertDialogTitle>{errorTitle}</AlertDialogTitle>
              <AlertDialogDescription>{errorDesc}</AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
              <AlertDialogCancel>Cancel</AlertDialogCancel>
              <AlertDialogAction onClick={errorAction}>
                {errorActionName}
              </AlertDialogAction>
            </AlertDialogFooter>
          </AlertDialogContent>
        </AlertDialog>
      </div>
      <StatusBar />
    </div>
  );
};
