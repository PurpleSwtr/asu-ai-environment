# asu-ai-environment

[English](README.en.md)

Шаблон окружения для курса по нейронным сетям. Готовая структура проекта
и предварительно настроенные зависимости, чтобы каждый студент быстро
развернул рабочую среду и не тратил время на конфигурацию.

## Оглавление

- [Требования](#требования)
- [Структура проекта](#структура-проекта)
- [Установка](#установка)
  - [Способ 1: uv (рекомендуется)](#способ-1-uv-рекомендуется)
  - [Способ 2: pip](#способ-2-pip)
    - [bash / macOS / Linux](#bash--macos--linux)
    - [Windows (cmd или PowerShell)](#windows-cmd-или-powershell)
- [Активация виртуального окружения](#активация-виртуального-окружения)
- [Зависимости](#зависимости)
  - [Основные (базовые, устанавливаются всегда)](#основные-базовые-устанавливаются-всегда)
  - [Опциональные группы](#опциональные-группы)
- [Запуск](#запуск)

## Требования

- Python 3.11 или 3.12 (требуемая версия зафиксирована в `.python-version`)
- Менеджер окружений: [uv](https://docs.astral.sh/uv/) либо pip + `venv`

## Структура проекта

```
main.py              CLI-точка входа
labs/                лабораторные работы
notebooks/           Jupyter-ноутбуки
src/                 пакет-окружение проекта
    data/            загрузка и подготовка данных
    models/          модели
    utils/           вспомогательные функции
pyproject.toml       описание проекта и зависимостей
```

## Установка

### Способ 1: uv (рекомендуется)

Установка uv: https://docs.astral.sh/uv/

```bash
uv sync --extra jupyter --extra additional
```

Команда сама создаст виртуальное окружение `.venv` (с версией Python из
`.python-version`), установит все зависимости и сам проект в editable-режиме.

Активация окружения после установки:

```bash
source .venv/bin/activate        # bash / macOS / Linux
.venv\Scripts\activate           # Windows (cmd или PowerShell)
```

### Способ 2: pip

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

Кавычки вокруг `".[jupyter,additional]"` обязательны: в противном случае
zsh/bash и PowerShell не поймут квадратные скобки.

## Активация виртуального окружения

| ОС / оболочка           | Команда                     |
| ----------------------- | --------------------------- |
| bash, zsh, macOS, Linux | `source .venv/bin/activate` |
| Windows cmd             | `.venv\Scripts\activate`    |
| Windows PowerShell      | `.venv\Scripts\activate`    |

После активации в начале строки приглашения появится префикс `(.venv)`.
Деактивация командой `deactivate`.

## Зависимости

### Основные (базовые, устанавливаются всегда)

| Пакет        | Назначение                                |
| ------------ | ----------------------------------------- |
| numpy        | численные операции с массивами            |
| pandas       | табличные данные и анализ                 |
| scipy        | научные вычисления                        |
| matplotlib   | построение графиков                       |
| scikit-learn | классические алгоритмы машинного обучения |

### Опциональные группы

| Группа       | Установка       | Состав и назначение                                                              |
| ------------ | --------------- | -------------------------------------------------------------------------------- |
| `jupyter`    | `.[jupyter]`    | блокноты: jupyterlab, ipykernel, ipywidgets, nbformat                            |
| `additional` | `.[additional]` | утилиты: tqdm (прогресс-бары), pyyaml (YAML-конфиги), joblib (сериализация)      |
| `nlp`        | `.[nlp]`        | обработка текста: transformers, datasets, accelerate, sentencepiece              |
| `torch`      | `.[torch]`      | PyTorch: torch, torchvision, torchaudio                                          |
| `tensorflow` | `.[tensorflow]` | TensorFlow                                                                       |
| `cv`         | `.[cv]`         | компьютерное зрение: opencv-python, Pillow, albumentations                       |
| `dev`        | `.[dev]`        | качество кода: ruff (линтер), mypy (проверка типов)                              |
| `testing`    | `.[testing]`    | тестирование: pytest, pytest-cov, pytest-mock, pytest-benchmark, pytest-codspeed |
| `profiling`  | `.[profiling]`  | профилирование: scalene, snakeviz                                                |

Пример установки нескольких групп с pip:

```bash
pip install -e ".[jupyter,additional,torch,dev]"
```

То же через uv:

```bash
uv sync --extra jupyter --extra additional
```

## Запуск

```bash
python main.py                 # CLI-точка входа
jupyter lab notebooks/         # работа в блокнотах (требует extra jupyter)
```
