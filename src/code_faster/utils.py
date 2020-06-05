import os


class Const:
    LINE_LENGTH = 40
    D_LINE = '=' * LINE_LENGTH
    S_LINE = '-' * LINE_LENGTH


class Extension:
    INPUTS = ['.i.txt', '.i', '.input']
    OUTPUTS = ['.o.txt', '.o', '.output']
    BIN = 'bin'

    @staticmethod
    def get_output_ext(path):
        for ext, out in zip(Extension.INPUTS, Extension.OUTPUTS):
            if path.endswith(ext):
                return out
        return None

    @staticmethod
    def name_from_input(path):
        for ext in Extension.INPUTS:
            if path.endswith(ext):
                return os.path.basename(path)[:-len(ext)]
        return None
