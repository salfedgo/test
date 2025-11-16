"""Simple command-line implementation of the classic "spin the bottle" party game.

Run the script and follow the prompts:
    python bottle_game.py

You can also pass player names as command-line arguments:
    python bottle_game.py Alice Bob Carol Dave
"""
from __future__ import annotations

import argparse
import random
from typing import List

PROMPT = "Введите имена игроков через запятую: "


def _parse_args() -> tuple[List[str], int | None]:
    parser = argparse.ArgumentParser(description="Игра в бутылочку")
    parser.add_argument(
        "players",
        nargs="*",
        help="Имена игроков. Если не указаны, программа попросит ввести их вручную",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=None,
        help="Количество вращений. По умолчанию игра длится бесконечно",
    )
    args = parser.parse_args()

    players = [name.strip() for name in args.players if name.strip()]
    return players, args.rounds


def _ask_players() -> List[str]:
    raw = input(PROMPT)
    players = [name.strip() for name in raw.split(",") if name.strip()]
    if len(players) < 2:
        raise ValueError("Нужно минимум два игрока")
    return players


def _spin(players: List[str]) -> tuple[str, str]:
    first, second = random.sample(players, 2)
    return first, second


def main() -> None:
    players, rounds = _parse_args()
    while len(players) < 2:
        try:
            players = _ask_players()
        except ValueError as exc:
            print(exc)

    print("Добро пожаловать в игру! Для выхода нажмите Ctrl+C.")

    try:
        remaining = rounds
        while remaining is None or remaining > 0:
            input("Нажмите Enter чтобы крутить бутылочку...")
            a, b = _spin(players)
            print(f"Бутылка указала: {a} ➜ {b}\n")
            if remaining is not None:
                remaining -= 1
    except KeyboardInterrupt:
        print("\nИгра окончена. Спасибо за участие!")


if __name__ == "__main__":
    main()
