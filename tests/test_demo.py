import os
from pathlib import Path

# current_path = os.getcwd()
# print(current_path)
#
# dirname = os.path.dirname(__file__)
# print(dirname)
#
# BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
# print(BASE_DIR)


current_dir = os.getcwd()
screenshots_dir = str(Path(current_dir).parents[0]).replace("\\", "/") + "/screenshots/"
