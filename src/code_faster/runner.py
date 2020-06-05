from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
from glob import glob
from colorama import Fore, Style

from .runners import runner_factory as rf
from .utils import Extension, Const


def main():
    if len(sys.argv) < 2:
        print('usage {} <filename> [args]'.format(sys.argv[0]))
        return

    filepath = sys.argv[1]
    args = '' if len(sys.argv) == 2 else ' '.join(sys.argv[2:])
    runner = rf.factory.get(filepath, Extension.BIN, args)
    if not runner.compile():
        return

    _run_tests(runner)


def _run_tests(runner):
    test_files = []
    for ext in Extension.INPUTS:
        test_files.extend(glob(os.path.join(runner.src_dir, '*' + ext)))
    test_files.sort(key=os.path.getmtime)
    tests = [(f, Extension.name_from_input(f)) for f in test_files]
    if not tests:
        print(
            f'No test found. Try to make "test{Extension.INPUT[0]}"'
            f' and "test{Extension.OUTPUT[0]}" files in the same folder as code')
        return

    print(Const.D_LINE)
    passed = 0
    for in_file, test in tests:
        ext = Extension.get_output_ext(in_file)
        gt_file = os.path.join(runner.src_dir, test + ext)
        out_file = os.path.join(runner.bin_dir, test + ext)

        if os.path.isfile(out_file):
            os.remove(out_file)

        runner.run(f'< {in_file} > {out_file}')
        passed += _check(test, in_file, out_file, gt_file)
        print(Const.D_LINE)

    status = ':)' if passed == len(tests) else ':('
    print(f'{status} {passed}/{len(tests)} passed.')


def _check(test, in_file, out_file, gt_file):
    in_text = _read_txt(in_file)
    out_text = _read_txt(out_file)
    if out_text is None:
        print(f'{test} {Fore.RED}RUNTIME ERROR: no output found{Style.RESET_ALL}')
        return False

    gt_text = _read_txt(gt_file)
    if gt_text is None:
        print(f'{test} {Fore.YELLOW}RUN{Style.RESET_ALL}')
        print(Const.S_LINE)
        print(out_text)
        return True

    if gt_text == out_text:
        print(f'{test} {Fore.GREEN}PASSED{Style.RESET_ALL}')
        return True

    print(f'{test} {Fore.RED}FAILED{Style.RESET_ALL}')
    _show_diff(out_text, gt_text)
    return False


def _show_diff(out_text, gt_text):
    out_text = out_text.split('\n')
    gt_text = gt_text.split('\n')
    print(Const.S_LINE, '[output]')
    for i, line in enumerate(out_text):
        if i < len(gt_text):
            _show_diff_row(line, gt_text[i])
        else:
            print(f'{Fore.RED}{line}{Style.RESET_ALL}')
    print(Const.S_LINE, '[answer]')
    print('\n'.join(gt_text))


def _show_diff_row(out_row, gt_row):
    if out_row == gt_row:
        print(f'{Fore.GREEN}{out_row}{Style.RESET_ALL}')
        return

    out_row = out_row.split(' ')
    gt_row = gt_row.split(' ')
    for i, word in enumerate(out_row):
        if i < len(gt_row) and word == gt_row[i]:
            print(f'{Fore.GREEN}{word}{Style.RESET_ALL}', end=' ')
        else:
            print(f'{Fore.RED}{word}{Style.RESET_ALL}', end=' ')
    print()


def _read_txt(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r') as f:
        return '\n'.join([l.rstrip() for l in f])


if __name__ == '__main__':
    main()
