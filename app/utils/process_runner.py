import os
import subprocess
from time import sleep

from app.utils.process import try_kill

processes: dict = {}
processes_file_paths: dict = {}


class ProcessRunner(object):
    global processes
    global processes_file_paths

    def get_processes(self) -> (dict, dict, dict):
        return processes.keys(), processes, processes_file_paths

    def start(self, id: str, path: str) -> subprocess.Popen:
        self.stop(id)
        process = self.__create_process(path)
        processes[id] = process
        processes_file_paths[id] = path
        return process

    def stop(self, id: str) -> bool:
        if id in processes:
            process = processes[id]
            del processes[id]
            del processes_file_paths[id]
            return self.__kill(process.pid)
        return False

    def call(self, key: str, path: str) -> subprocess.Popen:
        return self.__create_process(path)

    def __create_process(self, path: str) -> subprocess.Popen:
        return subprocess.Popen(path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

    def __kill(self, pid: str) -> bool:
        delay = 0.1
        time = 0
        timeout = 10
        while try_kill(pid):
            if time >= timeout:
                return False
            time = time + delay
            sleep(delay)
        return True
