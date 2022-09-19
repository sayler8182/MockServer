from app.models.models.process import Process
from app.utils.form_validator import validate_not_empty
from app.utils.process_runner import ProcessRunner

process_runner = ProcessRunner()


def processes() -> [Process]:
    items: [Process] = []
    keys, processes, file_paths = process_runner.get_processes()
    for key in keys:
        process = processes[key]
        file_path = file_paths[key]
        item = Process(key=key,
                       pid=process.pid,
                       file_path=file_path)
        items.append(item)
    return items


def start(key: str, file_path: str) -> Process:
    validate_not_empty(key, 'Key should be provided')
    validate_not_empty(file_path, 'Path should be provided')
    process = process_runner.start(key, file_path)
    return Process(key=key,
                   pid=process.pid,
                   file_path=file_path)


def stop(key: str) -> bool:
    validate_not_empty(key, 'Key should be provided')
    return process_runner.stop(key)


def call(key: str, file_path: str) -> Process:
    validate_not_empty(key, 'Key should be provided')
    validate_not_empty(file_path, 'Path should be provided')
    process = process_runner.call(key, file_path)
    return Process(key=key,
                   pid=process.pid,
                   file_path=file_path,
                   result=process.stdout.read().decode(),
                   error=process.stderr.read().decode())
