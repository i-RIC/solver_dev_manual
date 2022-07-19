import os
import re

FID_EXCEPTIONS = [
    'cg_iric_close',
    'cg_iric_flush',
    'cg_iric_open',
    
]

def convert_name():
    for name in os.listdir('.'):
        if '.py' in name:
            continue

        if '_f.' in name:
            os.rename(name, name.replace('_f.', '.'))

        if '_f_' in name:
            os.rename(name, name.replace('_f_', '_'))

def convert_content():
    for name in os.listdir('.'):
        if '.py' in name:
            continue

        c = readfile(name)
        
        c = c.replace('_f', '')
        c = c.replace('unctional', '_functional')
        
        writefile(name, c)


def add_fin():
    for name in os.listdir('.'):
        if not '.rst' in name: continue

        print('name', name)
        fname, ext = name.split('.')

        if fname in FID_EXCEPTIONS:
            continue

        c = readfile(name)
        
        c = _add_fin(c)
        
        writefile(name, c)


def _add_fin(content):
    lines = content.split('\n')
    new_lines = list()

    pattern = re.compile(r'(.+cg_.*\()(.*)(\).*)')

    for l in lines:
        m = pattern.search(l)
        if not m is None:
            pre, args_str, post = m.groups()
            args = _clean_args([a.strip() for a in args_str.split(',')])
            args.insert(0, 'fid')
            
            l = pre + ', '.join(args) + post
    
        new_lines.append(l)

    return '\n'.join(new_lines)


def _clean_args(args):
    new_args = list()
    for a in args:
        if a == '': continue
        new_args.append(a)

    return new_args


def add_fin_to_args():
    for name in os.listdir('.'):
        if not '_args.csv' in name: continue
        if not 'cg_' in name: continue

        print('name', name)
        fname, ext = name.split('.')

        if fname.replace('_args', '') in FID_EXCEPTIONS:
            continue

        c = readfile(name)
        
        c = _add_fin_to_args(c)
        
        writefile(name, c)


def _add_fin_to_args(content):
    lines = content.split('\n')
    lines.insert(1, 'fid,integer,I,ファイルID')
    return '\n'.join(lines)


def readfile(fname: str) -> str:
    with open(fname, 'r', encoding='utf-8') as f:
        return f.read()


def writefile(fname: str, content: str):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    # convert_name()
    # convert_content()
    # add_fin()
    add_fin_to_args()
