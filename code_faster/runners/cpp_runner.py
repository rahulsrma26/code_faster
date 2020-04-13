import os
from .base_runner import BaseRunner


class CppRunner(BaseRunner):

    def compile(self):
        filename, _ = os.path.splitext(self.src_name)
        self.dst_path = os.path.join(self.bin_dir, filename)

        if os.name == 'nt':
            self.dst_path += '.exe'

        if os.path.isfile(self.dst_path):
            os.remove(self.dst_path)

        self.shell(f'g++ {self.args} -o {self.dst_path} {self.src_path}')

        return os.path.isfile(self.dst_path)


    def run(self, args):
        self.shell(f'{self.dst_path} {args}', True)
