<img width="1252" height="640" alt="Image" src="https://github.com/user-attachments/assets/f2a14414-6d87-47d5-8c3e-0f95e212b753" />

[Русский](README.md)

A development template for the neural networks course. It provides a ready
project structure and preconfigured dependencies so every student can set up
a working environment quickly without fiddling with configuration.

## Contents

- [Contents](#contents)
- [Requirements](#requirements)
- [Quick start](#quick-start)
  - [If you don't have uv - installing with pip](#if-you-dont-have-uv---installing-with-pip)
    - [bash / macOS / Linux](#bash--macos--linux)
    - [Windows (cmd or PowerShell)](#windows-cmd-or-powershell)
- [Project structure](#project-structure)
- [Dependencies](#dependencies)
  - [Core](#core)
  - [Optional groups](#optional-groups)
- [What's next](#whats-next)

## Requirements

- **Python 3.12** - the version is pinned in `.python-version`.
  Install it from [python.org](https://www.python.org/downloads/) and check:

  ```bash
  py -3.12 --version
  ```

- **[uv](https://docs.astral.sh/uv/)** - environment manager. Installing it is
  optional but recommended: uv is noticeably faster than pip and manages
  environments and Python versions on its own. Install it following the
  [guide](https://docs.astral.sh/uv/#installation).

## Quick start

Clone the repository and install dependencies:

```bash
git clone https://github.com/PurpleSwtr/asu-ai-environment.git
cd asu-ai-environment
uv sync --extra jupyter --extra additional
```

`uv sync` creates the virtual environment `.venv`, installs all dependencies
and the project itself in editable mode. Versions are pinned in `uv.lock`,
so everyone gets the same environment.

Activate the environment:

**bash / macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (cmd or PowerShell):**

```powershell
.venv\Scripts\activate
```

### If you don't have uv - installing with pip

<details>
<summary>Expand</summary>

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

</details>

## Project structure

```
main.py              CLI entry point
labs/                lab works
notebooks/           Jupyter notebooks
src/                 the project package
    data/            data loading and preparation
    models/          models
    utils/           helper functions
pyproject.toml       project description and dependencies
.python-version      pinned Python version
uv.lock              pinned dependency versions
```

## Dependencies

### Core

Always installed:

| Package      | Purpose                             |
| ------------ | ----------------------------------- |
| numpy        | numerical operations on arrays      |
| pandas       | tabular data and analysis           |
| scipy        | scientific computing                |
| matplotlib   | plotting                            |
| scikit-learn | classic machine learning algorithms |

### Optional groups

| Group        | Install                              | Contents                                                          |
| ------------ | ------------------------------------ | ----------------------------------------------------------------- |
| `jupyter`    | `uv sync --extra jupyter`            | jupyterlab, ipykernel, ipywidgets, nbformat                       |
| `additional` | `uv sync --extra additional`         | tqdm, pyyaml, joblib                                              |
| `nlp`        | `uv sync --extra nlp`                | transformers, datasets, accelerate, sentencepiece                 |
| `torch`      | `uv sync --extra torch`              | torch, torchvision, torchaudio                                    |
| `tensorflow` | `uv sync --extra tensorflow`         | TensorFlow                                                        |
| `cv`         | `uv sync --extra cv`                 | opencv-python, Pillow, albumentations                             |
| `dev`        | `uv sync --extra dev`                | ruff, mypy                                                        |
| `testing`    | `uv sync --extra testing`            | pytest, pytest-cov, pytest-mock, pytest-codspeed, pytest-benchmark |
| `profiling`  | `uv sync --extra profiling`          | scalene, snakeviz                                                 |

Several groups at once:

```bash
uv sync --extra jupyter --extra additional --extra torch
```

## What's next

1. Open `labs/` - assignments will live here.
2. To work in notebooks:

   ```bash
   jupyter lab notebooks/
   ```
