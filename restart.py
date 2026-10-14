import trystart
import sys
import shutil
from typing import NoReturn

def restart() -> NoReturn:
    "restarts"
    try:
        shutil.rmtree("Hazel/downloads")
    except: pass
    os.execv(
        sys.executable,
        [sys.executable, "-m", "Hazel"] + sys.argv[1:]
    )
