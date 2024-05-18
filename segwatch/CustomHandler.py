import logging
import shutil
from typing import Optional

from watchdog.events import FileSystemEventHandler, FileSystemEvent

from segwatch.utils.file_utils import mkdirs
from segwatch.utils.path_utils import normalize_path, get_ext, get_dir_path


class CustomHandler(FileSystemEventHandler):
    tmp = "tmp"
    hls = "hls"

    def __init__(self, logger: Optional[logging.Logger] = None) -> None:
        super().__init__()
        self.logger = logger or logging.root
        self.seg_map: dict = {}

    def on_moved(self, event: FileSystemEvent) -> None:
        super().on_moved(event)

        what = "directory" if event.is_directory else "file"
        self.logger.info("Moved %s: from %s to %s", what, event.src_path, event.dest_path)

        if get_ext(event.dest_path) != "m3u8":
            return

        new_path = normalize_path(event.dest_path).replace(CustomHandler.tmp, CustomHandler.hls)
        mkdirs(get_dir_path(new_path))
        shutil.copy(event.dest_path, new_path)

    # def on_created(self, event: FileSystemEvent) -> None:
    #     super().on_created(event)
    #
    #     what = "directory" if event.is_directory else "file"
    #     self.logger.info("Created %s: %s", what, event.src_path)
    #
    # def on_deleted(self, event: FileSystemEvent) -> None:
    #     super().on_deleted(event)
    #
    #     what = "directory" if event.is_directory else "file"
    #     self.logger.info("Deleted %s: %s", what, event.src_path)

    def on_modified(self, event: FileSystemEvent) -> None:
        super().on_modified(event)

        what = "directory" if event.is_directory else "file"
        self.logger.info("Modified %s: %s", what, event.src_path)

        if get_ext(event.src_path) != "ts":
            return

        new_path = normalize_path(event.src_path).replace(CustomHandler.tmp, CustomHandler.hls)
        try:
            del self.seg_map[new_path]
        except KeyError:
            self.seg_map[new_path] = new_path
            return

        mkdirs(get_dir_path(new_path))
        shutil.copy(event.src_path, new_path)

    # def on_closed(self, event: FileSystemEvent) -> None:
    #     super().on_closed(event)
    #
    #     self.logger.info("Closed file: %s", event.src_path)
    #
    # def on_opened(self, event: FileSystemEvent) -> None:
    #     super().on_opened(event)
    #
    #     self.logger.info("Opened file: %s", event.src_path)

