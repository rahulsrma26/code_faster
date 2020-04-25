import os
import sys
import shutil
from datetime import datetime

from .fetchers import fetcher_factory as ff
from .utils import Extension


def main():
    if len(sys.argv) not in [2, 3]:
        print('usage {} <code-force-url> [language or sample-dir]'.format(sys.argv[0]))
        print('languages: [cpp(default) | java | py]')
        return

    cwd = os.getcwd()
    url = sys.argv[1]
    language = 'cpp' if len(sys.argv) == 2 else sys.argv[2]

    site = ff.factory.get(url)
    dir_name = site.dirname()

    # create directory
    if os.path.isdir(dir_name):
        print(dir_name, 'already exist')
    else:
        print(dir_name, 'created')
        os.mkdir(dir_name)

    # create test(s)
    for idx, (inp, out) in enumerate(site.tests(), 1):
        _create_files(dir_name, idx, inp, out)

    # copying the content of sample dir
    if language in ['cpp', 'java', 'py']:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        sample_dir = os.path.join(base_dir, 'sample', language)
    else:
        sample_dir = language

    if not os.path.isdir(sample_dir):
        print(sample_dir, 'not found')
        return

    for filename in os.listdir(sample_dir):
        filepath = os.path.join(sample_dir, filename)
        if os.path.isfile(filepath) and filename[0] != '.':
            dstpath = os.path.join(dir_name, filename)
            if not os.path.isfile(dstpath):
                if 'main' in filename.lower():
                    _create_copy(filepath, dstpath, url)
                else:
                    shutil.copyfile(filepath, dstpath)
                print(filename, 'created')
            else:
                print(filename, 'already exist')


def _create_files(base_dir, idx, inp, out):
    i_file = os.path.join(base_dir, f'test_{idx}{Extension.INPUT}')
    with open(i_file, 'w') as f:
        f.write(inp)
    o_file = os.path.join(base_dir, f'test_{idx}{Extension.OUTPUT}')
    with open(o_file, 'w') as f:
        f.write(out)
    print(f'test_{idx} created')


def _create_copy(src, dst, url):
    with open(src, 'r', encoding='utf-8') as in_file:
        text = in_file.read()
        text = text.replace('<<<date_now>>>', str(datetime.date(datetime.now())))
        text = text.replace('<<<src_url>>>', url)
        with open(dst, 'w', encoding='utf-8') as out_file:
            out_file.write(text)


if __name__ == '__main__':
    main()
