import os
from .base_runner import BaseRunner


class PythonRunner(BaseRunner):

    def compile(self):
        return os.path.isfile(self.src_path)


    def run(self, args):
        self.shell(f'python {self.src_path} {args}', True)
