import os
from .base_runner import BaseRunner


class JavaRunner(BaseRunner):

    def compile(self):
        self.fname, _ = os.path.splitext(self.src_name)
        full_fname = self.fname + '.class'
        self.dst_path = os.path.join(self.src_dir, self.bin_dir, full_fname)

        if os.path.isfile(self.dst_path):
            os.remove(self.dst_path)

        self.shell(f'javac -d {self.bin_dir} {self.src_path}')

        return os.path.isfile(self.dst_path)


    def run(self, args):
        self.shell(f'java -cp {self.bin_dir} {self.fname} {args}', True)
