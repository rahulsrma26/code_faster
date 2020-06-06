"""
cfetch [code-fetch]
===================
cfetch command fetches the code from a url.
"""
import os
import sys
import shutil
from argparse import ArgumentParser, RawTextHelpFormatter
from datetime import datetime

from .fetchers import fetcher_factory as ff
from .utils import Extension


def _get_args():
    parser = ArgumentParser(
        prog='cfetch', description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        'url', type=str, help='url of the code')
    parser.add_argument(
        '-l', '--language',
        choices=['cpp', 'java', 'py'],
        default='cpp', help='default is cpp')
    parser.add_argument(
        '-d', '--dir',
        default='',
        help='if given then uses this dir and language flag will be ignored.')
    return parser.parse_args()


def main():
    args = _get_args()
    cwd = os.getcwd()
    url = args.url

    page = ff.factory.get(url)
    dir_name = page.dirname()

    # create directory
    if os.path.isdir(dir_name):
        print(dir_name, 'already exist')
    else:
        print(dir_name, 'created')
        os.mkdir(dir_name)

    # create test(s)
    for idx, (inp, out) in enumerate(page.tests(), 1):
        _create_files(dir_name, idx, inp, out)

    # copying the content of sample dir
    sample_dir = args.dir
    if not args.dir:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        sample_dir = os.path.join(base_dir, 'sample', args.language)

    if not os.path.isdir(sample_dir):
        print(sample_dir, 'not found')
        return

    for filename in os.listdir(sample_dir):
        filepath = os.path.join(sample_dir, filename)
        if os.path.isfile(filepath) and filename[0] != '.':
            dstpath = os.path.join(dir_name, filename)
            if not os.path.isfile(dstpath):
                if 'main' in filename.lower():
                    _create_copy(filepath, dstpath, page)
                else:
                    shutil.copyfile(filepath, dstpath)
                print(filename, 'created')
            else:
                print(filename, 'already exist')


def _create_files(base_dir, idx, inp, out):
    i_file = os.path.join(base_dir, f'test_{idx}{Extension.INPUTS[0]}')
    with open(i_file, 'w') as f:
        f.write(inp)
    o_file = os.path.join(base_dir, f'test_{idx}{Extension.OUTPUTS[0]}')
    with open(o_file, 'w') as f:
        f.write(out)
    print(f'test_{idx} created')


def _create_copy(src, dst, page):
    with open(src, 'r', encoding='utf-8') as in_file:
        text = in_file.read()
        text = text.replace('<<<date_now>>>', str(datetime.date(datetime.now())))
        text = text.replace('<<<src_url>>>', page.url)
        text = text.replace('<<<title>>>', page.title())
        # ToDo: text = text.replace('<<<statement>>>', page.statement())
        with open(dst, 'w', encoding='utf-8') as out_file:
            out_file.write(text)


if __name__ == '__main__':
    main()
