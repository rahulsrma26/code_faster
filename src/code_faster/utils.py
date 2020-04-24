import os


class Const:
    LINE_LENGTH = 40
    D_LINE = '=' * LINE_LENGTH
    S_LINE = '-' * LINE_LENGTH


class Extension:
    INPUT = '.input'
    OUTPUT = '.output'
    BIN = 'bin'

    @staticmethod
    def output(input_file):
        return input_file[:-len(Extension.INPUT)] + Extension.OUTPUT

    @staticmethod
    def name(path):
        if path.endswith(Extension.INPUT):
            return os.path.basename(path)[:-len(Extension.INPUT)]
        if path.endswith(Extension.OUTPUT):
            return os.path.basename(path)[:-len(Extension.OUTPUT)]
        return None
