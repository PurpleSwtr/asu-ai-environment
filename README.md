<img width="1252" height="640" alt="Image" src="https://github.com/user-attachments/assets/f2a14414-6d87-47d5-8c3e-0f95e212b753" />

[English](README.en.md)

Шаблон окружения для курса по нейронным сетям. Готовая структура проекта
и предварительно настроенные зависимости, чтобы каждый студент быстро
развернул рабочую среду и не тратил время на конфигурацию.

## Оглавление

- [Оглавление](#оглавление)
- [Требования](#требования)
- [Быстрый старт](#быстрый-старт)
  - [Если вы выбрали медленный путь без uv - установка через pip](#если-вы-выбрали-медленный-путь-без-uv---установка-через-pip)
    - [bash / macOS / Linux](#bash--macos--linux)
    - [Windows (cmd или PowerShell)](#windows-cmd-или-powershell)
- [Структура проекта](#структура-проекта)
- [Зависимости](#зависимости)
  - [Основные](#основные)
  - [Опциональные группы](#опциональные-группы)
- [Что дальше](#что-дальше)

## Требования

- **Python 3.12** - версия зафиксирована в файле `.python-version`.
  Установите с [python.org](https://www.python.org/downloads/) и проверьте:

  ```bash
  py -3.12 --version  # Windows
  python3 --version   # bash / macOS / Linux
  ```

- **[uv](https://docs.astral.sh/uv/)** - менеджер окружений. Его установка
  необязательна, но рекомендуется: uv заметно быстрее pip и сам управляет
  окружениями и версиями Python. Установите по
  [инструкции](https://docs.astral.sh/uv/#installation).

## Быстрый старт

Склонируйте репозиторий и установите зависимости:

```bash
git clone https://github.com/PurpleSwtr/asu-ai-environment.git
cd asu-ai-environment
uv sync --extra jupyter --extra additional
```

Команда `uv sync` создаст виртуальное окружение `.venv`, установит все
зависимости и сам проект. Версии фиксируются из
`uv.lock`, поэтому у всех будет одинаковое окружение.

Активируйте окружение:

**bash / macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (cmd или PowerShell):**

```powershell
.venv\Scripts\activate
```

### Если вы выбрали медленный путь без uv - установка через pip

<details>
<summary>Развернуть</summary>

#### bash / macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[jupyter,additional]"
```

#### Windows (cmd или PowerShell)

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -e ".[jupyter,additional]"
```

Кавычки вокруг `".[jupyter,additional]"` обязательны: иначе zsh/bash
и PowerShell не поймут квадратные скобки.

</details>

## Структура проекта

```
main.py              CLI-точка входа
labs/                лабораторные работы
notebooks/           Jupyter-ноутбуки
src/                 пакет проекта
    data/            загрузка и подготовка данных
    models/          модели
    utils/           вспомогательные функции
pyproject.toml       описание проекта и зависимостей
.python-version      фиксированная версия Python
uv.lock              зафиксированные версии зависимостей
```

## Зависимости

### Основные

Устанавливаются всегда:

| Пакет        | Назначение                                |
| ------------ | ----------------------------------------- |
| numpy        | численные операции с массивами            |
| pandas       | табличные данные и анализ                 |
| scipy        | научные вычисления                        |
| matplotlib   | построение графиков                       |
| scikit-learn | классические алгоритмы машинного обучения |

### Опциональные группы

| Группа       | Установка                            | Состав                                                          |
| ------------ | ------------------------------------ | --------------------------------------------------------------- |
| `jupyter`    | `uv sync --extra jupyter`            | jupyterlab, ipykernel, ipywidgets, nbformat                     |
| `additional` | `uv sync --extra additional`         | tqdm, pyyaml, joblib                                            |
| `nlp`        | `uv sync --extra nlp`                | transformers, datasets, accelerate, sentencepiece               |
| `torch`      | `uv sync --extra torch`              | torch, torchvision, torchaudio                                  |
| `tensorflow` | `uv sync --extra tensorflow`         | TensorFlow                                                      |
| `cv`         | `uv sync --extra cv`                 | opencv-python, Pillow, albumentations                           |
| `dev`        | `uv sync --extra dev`                | ruff, mypy                                                      |
| `testing`    | `uv sync --extra testing`            | pytest, pytest-cov, pytest-mock, pytest-codspeed, pytest-benchmark |
| `profiling`  | `uv sync --extra profiling`          | scalene, snakeviz                                               |

Несколько групп одновременно:

```bash
uv sync --extra jupyter --extra additional --extra torch
```

## Что дальше

1. Откройте `labs/` - здесь будут ваши задания.

2. Для работы в блокнотах:

   ```bash
   jupyter lab notebooks/
   ```
