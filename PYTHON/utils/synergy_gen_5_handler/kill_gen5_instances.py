def kill_gen5_instances():
    import psutil
    PROCNAME = "Gen5"

    for proc in psutil.process_iter():
    # check whether the process name matches
        if PROCNAME in proc.name():
            proc.kill()