import json

class Task:
    def __init__(self) -> None:
        self._task = ""
        pass

    def set_task(self, name):
        self._task = name

    def get_task(self):
        return self._task
    
    def to_dict(self):
        return {
            'task': self._task
        }
