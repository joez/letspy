#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def listdir(dir):
    print('listdir:')
    print([e for e in os.listdir(dir) if os.path.isdir(os.path.join(dir, e))])

def scandir(dir):
    print('scandir:')
    with os.scandir(dir) as entries:
        print([e.name for e in entries if e.is_dir()])

def iterdir(dir):
    print('iterdir:')
    entries = Path(dir)
    print([e.name for e in entries.iterdir() if e.is_dir()])

def walk(dir):
    print('walk:')
    for root, dirs, files in os.walk(dir):
        if '.git' in dirs:
            dirs.remove('.git')
        print(root)

if __name__ == '__main__':
    d = sys.argv[1] if len(sys.argv) > 1 else '.'
    for f in [listdir, scandir, iterdir, walk]:
        f(d)
