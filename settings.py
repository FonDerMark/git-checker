import os
from pathlib import Path

# Настройки имени и расположения файла с версией последнего коммита
COMMIT_INFO_FILE_NAME = 'commit_info.json'
COMMIT_INFO_FILE_PATH = os.path.join(Path(__file__).resolve().parent, COMMIT_INFO_FILE_NAME)