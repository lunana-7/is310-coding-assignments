"""Collect and confirm movie records, then save them as JSON."""

import json
from datetime import date
from pathlib import Path

from rich.console import Console
from rich.table import Table


console = Console()
EXAMPLES = [
    {"title": "Spirited Away", "director": "Hayao Miyazaki", "year": 2001,
     "cultural_note": "A possible starting point for discussing work and identity."},
    {"title": "Parasite", "director": "Bong Joon Ho", "year": 2019,
     "cultural_note": "A possible starting point for discussing class and housing."},
]


def show_records(records, heading):
    """Display the same fields used in the saved dataset."""
    table = Table(title=heading)
    for column in ("Title", "Director", "Year", "Cultural note"):
        table.add_column(column)
    for record in records:
        table.add_row(record["title"], record["director"], str(record["year"]),
                      record["cultural_note"])
    console.print(table)


def required_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        console.print("Please enter a value.", style="yellow")


def ask_year():
    while True:
        value = required_text("Release year (1888 to this year): ")
        if value.isascii() and value.isdecimal() and 1888 <= int(value) <= date.today().year:
            return int(value)
        console.print(f"Enter a whole year from 1888 to {date.today().year}.", style="yellow")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        console.print("Please answer yes or no.", style="yellow")


def main():
    console.print("Movie Culture Notebook", style="bold cyan")
    console.print("Examples only; these will not be included in your file.")
    show_records(EXAMPLES, "Example movie records")
    console.print("Add at least two movies. Cultural notes are your interpretations, not objective labels.")
    records = []
    while True:
        console.print(f"Movie {len(records) + 1}", style="bold cyan")
        record = {
            "title": required_text("Movie title: "),
            "director": required_text("Director: "),
            "year": ask_year(),
            "cultural_note": required_text("Cultural note (a theme or question to explore): "),
        }
        show_records([record], "Review your entry")
        if not ask_yes_no("Is this correct? (yes/no): "):
            console.print("Please re-enter this movie. The rejected entry will not be saved.")
            continue
        records.append(record)
        if len(records) < 2:
            console.print("Please add one more movie before saving.")
        elif not ask_yes_no("Add another movie? (yes/no): "):
            break

    # A new filename for every session prevents overwriting previous collections.
    folder = Path(__file__).resolve().parent
    number = 1
    while True:
        output = folder / f"movies_{number:03d}.json"
        try:
            with output.open("x", encoding="utf-8") as data_file:
                json.dump(records, data_file, ensure_ascii=False, indent=2)
                data_file.write("\n")
            break
        except FileExistsError:
            number += 1
    console.print(f"Saved {len(records)} confirmed movies.", style="bold green")
    console.print(str(output), markup=False, soft_wrap=True)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        console.print("\nCancelled. No data file was saved.", style="yellow")
    except OSError as error:
        console.print(f"Could not save the file: {error}", markup=False, style="red")
        raise SystemExit(1)
