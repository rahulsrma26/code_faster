import os
from abc import ABC, abstractmethod
import subprocess


class BaseRunner(ABC):
    def __init__(self, src_path, bin_name, args):
        self.parser = self.__class__.__name__
        self.src_path = src_path
        self.src_dir = os.path.dirname(self.src_path)
        self.src_name = os.path.basename(self.src_path)
        self.bin_dir = os.path.join(self.src_dir, bin_name)
        self.args = args
        if not os.path.isdir(self.bin_dir):
            os.makedirs(self.bin_dir)

    def shell(self, cmd, silent=False):
        self.cmd = cmd
        if not silent:
            print(cmd)
        subprocess.run(cmd, shell=True, check=True)

    @abstractmethod
    def compile(self):
        pass

    @abstractmethod
    def run(self, args):
        pass
