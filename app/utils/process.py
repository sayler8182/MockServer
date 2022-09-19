import os
import signal
import subprocess

import psutil


def kill_process_on_port(port: int):
    result = subprocess.run(['lsof', f'-ti:{port}'], stdout=subprocess.PIPE)
    processes = result.stdout.decode()
    processes = processes.split('\n')
    processes = list(filter(None, processes))
    processes = list(map(int, processes))
    processes = list(map(psutil.Process, processes))
    processes = list(filter(lambda item: item.name() == 'Python', processes))
    for process in processes:
        kill(process.pid)


def kill(pid):
    pgid = os.getpgid(pid)
    os.killpg(pgid, signal.SIGINT)


def try_kill(pid: str):
    try:
        kill(pid)
        return True
    except OSError:
        return False
