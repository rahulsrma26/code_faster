import os
from .cpp_runner import CppRunner
from .java_runner import JavaRunner
from .py_runner import PythonRunner


class RunnerFactory:
    def __init__(self):
        self._runners = {}

    def register(self, key, runner):
        self._runners[key] = runner

    def get(self, filepath, bin_dir, lib_dir):
        _, ext = os.path.splitext(filepath)
        return self._runners.get(ext)(filepath, bin_dir, lib_dir)


factory = RunnerFactory()
factory.register('.cpp', CppRunner)
factory.register('.java', JavaRunner)
factory.register('.py', PythonRunner)
