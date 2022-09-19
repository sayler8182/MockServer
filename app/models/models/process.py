class Process(object):
    def __init__(self,
                 pid: int,
                 key: str,
                 file_path: str,
                 result: str = None,
                 error: str = None):
        self.pid = pid
        self.key = key
        self.file_path = file_path
        self.result = result
        self.error = error

    def get_dict(self):
        return {
            'pid': self.pid,
            'key': self.key,
            'file_path': self.file_path,
            'result': self.result,
            'error': self.error
        }

    @staticmethod
    def process_from_dict(object: dict):
        if object is None:
            return None

        pid = object.get('pid', None)
        key = object.get('key', None)
        file_path = object.get('file_path', None)
        result = object.get('result', None)
        error = object.get('error', None)
        return Process(pid=pid,
                       key=key,
                       file_path=file_path,
                       result=result,
                       error=error)
