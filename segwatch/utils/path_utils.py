import os


def normalize_path(path: str) -> str:
    return path.replace('\\', '/')


def get_filename(path: str) -> str:
    chunks = normalize_path(path).split("/")
    return chunks[len(chunks) - 1]


def get_dir_path(path: str) -> str:
    chunks = normalize_path(path).split("/")
    chunks.pop(len(chunks)-1)
    return "/".join(chunks)


def get_ext(path: str) -> str:
    chunks = path.split(".")
    if len(chunks) == 1:
        return ""
    else:
        return chunks[len(chunks) - 1]
