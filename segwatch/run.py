import time
import logging
from watchdog.observers import Observer

from segwatch.CustomHandler import CustomHandler
from segwatch.utils.file_utils import mkdirs


def run(tmp_path: str, hls_path: str):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    logging.info(f'start watching directory {tmp_path!r}')

    mkdirs(tmp_path)
    mkdirs(hls_path)
    event_handler = CustomHandler()

    observer = Observer()
    observer.schedule(event_handler, tmp_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
