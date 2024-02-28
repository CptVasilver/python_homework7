import zipfile
import os
import pytest
import shutil

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, "files")
ARCHIVE_DIR = os.path.join(CURRENT_DIR, "archive")
ARCHIVE_PATH = os.path.join(ARCHIVE_DIR, "Archive.zip")


@pytest.fixture(scope='session', autouse=True)
def zipping():
    if not os.path.exists(ARCHIVE_DIR):
        os.mkdir(ARCHIVE_DIR)
    with zipfile.ZipFile(ARCHIVE_PATH, 'w') as zf:
        for file in os.listdir(FILES_DIR):
            add_file = os.path.join(FILES_DIR, file)
            zf.write(add_file, os.path.basename(add_file))

    yield

    shutil.rmtree(ARCHIVE_DIR)
