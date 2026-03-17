# 🎲 LootGen

**LootGen** — консольная утилита для симуляции выпадения редких игровых предметов (лута) из сундуков.  
Используется для балансировки дроп-таблиц в видеоиграх.

---

## ⚙️ Технологии

| Инструмент | Назначение |
|---|---|
| Python 3.11+ | Язык программирования |
| [Rich](https://github.com/Textualize/rich) | Красивый вывод таблиц в консоль |
| [Ruff](https://docs.astral.sh/ruff/) | Линтер и форматтер кода |
| GitHub Actions | CI/CD — автоматическая проверка кода |
| Git | Система контроля версий |

---

## 🚀 Развёртывание и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/<ВАШ_ЛОГИН>/lootgen.git
cd lootgen
```

### 2. Создать виртуальное окружение и установить зависимости

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### 3. Запустить утилиту

```bash
python lootgen.py
```

Программа спросит, сколько сундуков открыть, и выведет таблицу с результатами.

---

## 🔍 Линтинг (проверка кода)

```bash
pip install ruff
ruff check .
ruff format --check .
```

---

## 🤖 CI/CD

При каждом `push` или открытии Pull Request GitHub Actions автоматически:

1. Клонирует репозиторий
2. Устанавливает зависимости
3. Запускает `ruff check` и `ruff format --check`

Слияние в `main` разрешено **только после зелёной галочки** CI.
