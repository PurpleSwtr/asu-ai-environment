import argparse

from rich.console import Console
from rich.panel import Panel

from .utils.github_linker import copy_to_clipboard, get_github_link_file, get_lab_file

console = Console()


def cmd_link(args: argparse.Namespace) -> None:
    lab = args.file
    labpath = get_lab_file(lab)
    if labpath is None:
        return
    link = get_github_link_file(labpath)
    console.print(Panel(f"[cyan]{link}[/cyan]", title="GitHub link", expand=False))
    copy_to_clipboard(link)
    console.print("[green]Copied to clipboard![/green]")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    link_parser = sub.add_parser("gh_link", help="Get GitHub link for lab.ipynb file")
    link_parser.add_argument("file", type=str, help="Relative lab{x} number")
    link_parser.set_defaults(func=cmd_link)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)