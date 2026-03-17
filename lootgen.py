"""LootGen – консольная утилита симуляции выпадения лута из сундуков."""

import random

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

LOOT_TABLE: list[dict] = [
    {"name": "Деревянный меч", "rarity": "Обычный", "weight": 50},
    {"name": "Кожаный шлем", "rarity": "Обычный", "weight": 35},
    {"name": "Серебряное кольцо", "rarity": "Редкий", "weight": 10},
    {"name": "Зелёный самоцвет", "rarity": "Редкий", "weight": 8},
    {"name": "Руна силы", "rarity": "Эпический", "weight": 4},
    {"name": "Дракий клык", "rarity": "Легендарный", "weight": 1},
]

RARITY_COLORS: dict[str, str] = {
    "Обычный": "white",
    "Редкий": "cyan",
    "Эпический": "magenta",
    "Легендарный": "yellow",
}


def roll_item() -> dict:
    """Выбрать случайный предмет с учётом весов."""
    population = [item for item in LOOT_TABLE for _ in range(item["weight"])]
    return random.choice(population)


def simulate(chests: int = 10) -> list[dict]:
    """Открыть несколько сундуков и вернуть список выпавших предметов."""
    return [roll_item() for _ in range(chests)]


def build_summary(drops: list[dict]) -> dict[str, int]:
    """Подсчитать количество каждого предмета."""
    summary: dict[str, int] = {}
    for drop in drops:
        summary[drop["name"]] = summary.get(drop["name"], 0) + 1
    return summary


def display_results(drops: list[dict]) -> None:
    """Вывести результаты в виде красивой таблицы."""
    table = Table(
        title="Результаты открытия сундуков",
        box=box.ROUNDED,
        show_lines=True,
    )
    table.add_column("№", justify="right", style="dim")
    table.add_column("Предмет", min_width=20)
    table.add_column("Редкость", justify="center")

    for idx, drop in enumerate(drops, start=1):
        color = RARITY_COLORS.get(drop["rarity"], "white")
        table.add_row(
            str(idx),
            f"[{color}]{drop['name']}[/{color}]",
            f"[{color}]{drop['rarity']}[/{color}]",
        )

    console.print(table)

    summary = build_summary(drops)
    summary_table = Table(title="Итоговая статистика", box=box.SIMPLE_HEAD)
    summary_table.add_column("Предмет", min_width=20)
    summary_table.add_column("Кол-во", justify="right")

    for name, count in sorted(summary.items(), key=lambda x: -x[1]):
        summary_table.add_row(name, str(count))

    console.print(summary_table)


def main() -> None:
    """Точка входа в приложение."""
    console.print(
        Panel.fit(
            "[bold yellow]LootGen[/bold yellow] – симулятор выпадения лута",
            border_style="gold1",
        )
    )

    try:
        raw = console.input("[bold]Сколько сундуков открыть? (по умолчанию 10): [/bold]")
        chests = int(raw.strip()) if raw.strip() else 10
        if chests <= 0:
            raise ValueError
    except ValueError:
        console.print("[red]Некорректное число. Используется значение по умолчанию: 10.[/red]")
        chests = 10

    console.print(f"\n[green]Открываем {chests} сундуков…[/green]\n")
    drops = simulate(chests)
    display_results(drops)


if __name__ == "__main__":
    main()
