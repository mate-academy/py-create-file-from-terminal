import sys
import os
from datetime import datetime


args = sys.argv[1:]

if '-d' in args:
    d_index = args.index('-d') + 1
    if '-f' in args:
        f_index = args.index('-f')
        dirs = args[d_index:f_index]
    else:
        dirs = args[d_index:]
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
else:
    path = ''

if '-f' in args:
    f_index = args.index('-f') + 1
    filename = args[f_index]
    full_path = os.path.join(path, filename) if path else filename

    lines = []
    i = 1
    while True:
        line = input('Enter content line: ')
        if line == 'stop':
            break
        lines.append(f'{i} {line}')
        i += 1

    with open(full_path, 'a', encoding='utf-8') as f:
        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        f.write('\n'.join(lines) + '\n\n')
