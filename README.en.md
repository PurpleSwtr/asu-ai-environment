<img width="1252" height="640" alt="Image" src="https://github.com/user-attachments/assets/f2a14414-6d87-47d5-8c3e-0f95e212b753" />

[Русский](README.md)

A development template for the neural networks course. It provides a ready
project structure and preconfigured dependencies so every student can set up
a working environment quickly without fiddling with configuration.

## Contents

- [Cloning and quick start](#cloning-and-quick-start)
- [Requirements](#requirements)
- [Project structure](#project-structure)
- [Installation](#installation)
  - [Option 1: uv (recommended)](#option-1-uv-recommended)
  - [Option 2: pip](#option-2-pip)
    - [bash / macOS / Linux](#bash--macos--linux)
    - [Windows (cmd or PowerShell)](#windows-cmd-or-powershell)
- [Activating the virtual environment](#activating-the-virtual-environment)
- [Dependencies](#dependencies)
  - [Core (base, always installed)](#core-base-always-installed)
  - [Optional groups](#optional-groups)
- [Running](#running)

## Cloning and quick start

```bash
git clone https://github.com/PurpleSwtr/asu-ai-environment.git
cd asu-ai-environment
uv sync --extra jupyter --extra additional
```

The first two commands clone the repository and change into it. `uv sync`
creates the virtual environment `.venv`, installs all dependencies and the
project itself in editable mode. Dependency versions are reproducible from
`uv.lock`, so everyone gets the same environment.

Activate the environment afterwards:

```bash
source .venv/bin/activate        # bash / macOS / Linux
.venv\Scripts\activate           # Windows (cmd or PowerShell)
```

If uv is not installed - install it, or use the classic pip path (see
[Installation](#installation)).

## Requirements

- Python 3.11 or 3.12 (the required version is pinned in `.python-version`)
- Environment manager: [uv](https://docs.astral.sh/uv/) or pip + `venv`

## Project structure

```
main.py              CLI entry point
labs/                lab works
notebooks/           Jupyter notebooks
src/                 the project's environment package
    data/            data loading and preparation
    models/          models
    utils/           helper functions
pyproject.toml       project description and dependencies
```

## Installation

### Option 1: uv (recommended)

Install uv: https://docs.astral.sh/uv/

```bash
uv sync --extra jupyter --extra additional
```

The command creates the virtual environment `.venv` on its own (using the
Python version from `.python-version`), installs all dependencies and the
project itself in editable mode.

Activate the environment afterwards:

```bash
source .venv/bin/activate        # bash / macOS / Linux
.venv\Scripts\activate           # Windows (cmd or PowerShell)
```

### Option 2: pip

#### bash / macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[jupyter,additional]"
```

#### Windows (cmd or PowerShell)

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -e ".[jupyter,additional]"
```

The quotes around `".[jupyter,additional]"` are required: otherwise zsh/bash
and PowerShell will not understand the square brackets.

## Activating the virtual environment

| OS / shell              | Command                     |
| ----------------------- | --------------------------- |
| bash, zsh, macOS, Linux | `source .venv/bin/activate` |
| Windows cmd             | `.venv\Scripts\activate`    |
| Windows PowerShell      | `.venv\Scripts\activate`    |

After activation the prompt gets a `(.venv)` prefix. Leave the environment
with the `deactivate` command.

## Dependencies

### Core (base, always installed)

| Package      | Purpose                             |
| ------------ | ----------------------------------- |
| numpy        | numerical operations on arrays      |
| pandas       | tabular data and analysis           |
| scipy        | scientific computing                |
| matplotlib   | plotting                            |
| scikit-learn | classic machine learning algorithms |

### Optional groups

| Group        | Install         | Contents and purpose                                                           |
| ------------ | --------------- | ------------------------------------------------------------------------------ |
| `jupyter`    | `.[jupyter]`    | notebooks: jupyterlab, ipykernel, ipywidgets, nbformat                         |
| `additional` | `.[additional]` | utilities: tqdm (progress bars), pyyaml (YAML configs), joblib (serialization) |
| `nlp`        | `.[nlp]`        | text processing: transformers, datasets, accelerate, sentencepiece             |
| `torch`      | `.[torch]`      | PyTorch: torch, torchvision, torchaudio                                        |
| `tensorflow` | `.[tensorflow]` | TensorFlow                                                                     |
| `cv`         | `.[cv]`         | computer vision: opencv-python, Pillow, albumentations                         |
| `dev`        | `.[dev]`        | code quality: ruff (linter), mypy (type checking)                              |
| `testing`    | `.[testing]`    | testing: pytest, pytest-cov, pytest-mock, pytest-benchmark, pytest-codspeed    |
| `profiling`  | `.[profiling]`  | profiling: scalene, snakeviz                                                   |

Installing several groups with pip:

```bash
pip install -e ".[jupyter,additional,torch,dev]"
```

The same with uv:

```bash
uv sync --extra jupyter --extra additional
```

## Running

```bash
python main.py                 # CLI entry point
jupyter lab notebooks/         # work in notebooks (requires the jupyter extra)
```
