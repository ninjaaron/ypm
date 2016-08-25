import sys, os
import shutil
PATHS = sys.argv[1:] if sys.argv[1:] else ['.']
STORE = '/tmp/yanked/'
os.mkdir(STORE) if not os.path.exists(STORE) else None
STORE += os.environ['USER']


def yank():
    open(STORE, 'w').writelines(os.path.abspath(p) + '\n' for p in PATHS)


def put():
    for path in open(STORE):
        path = path.rstrip()
        print(os.path.basename(path))
        try:
            shutil.copy(path, PATHS[0])
        except IsADirectoryError:
            dest = PATHS[0] + '/' + os.path.basename(path)
            shutil.copytree(path, dest)


def move():
    with open(STORE) as store:
        paths = list(i.rstrip() for i in store)

    for path in paths:
        print(os.path.basename(path))
        shutil.move(path, PATHS[0])

    open(STORE, 'w').writelines(
        os.path.abspath(PATHS[0]+'/'+os.path.basename(p)) for p in paths
        )
