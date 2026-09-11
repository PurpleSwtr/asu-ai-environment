import subprocess
import sys
from pathlib import Path
from urllib.parse import urljoin

from rich import print

from ..core.config import config


def get_github_link_file(filepath: Path):
    return urljoin(config.get_github_link(), filepath.as_posix())


def copy_to_clipboard(text: str) -> None:
    if sys.platform == "win32":
        subprocess.run("clip", input=text, text=True, check=True)


def get_lab_file(lab: str) -> Path | None:
    lab_dir = Path("labs") / lab
    if not lab_dir.is_dir():
        print(f"[red]Directory with {lab} not exists![/red]")
        return None
    lab_file = (lab_dir / lab).with_suffix(".ipynb")
    if not lab_file.exists():
        print(f"[red]File {lab_file} not exists![/red]")
        return None
    return lab_file
