import os


def mkdirs(path: str):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
