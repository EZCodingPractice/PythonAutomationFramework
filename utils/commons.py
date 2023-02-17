import inspect
import os
from pathlib import Path


def whoami():
    return inspect.stack()[1][3]


def get_screenshot_dir():
    current_dir = os.getcwd()
    screenshots_dir = str(Path(current_dir).parents[0]).replace("\\", "/") + "/screenshots/"
    return screenshots_dir
