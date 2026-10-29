"""Пересобирает таблицу решённых задач в корневом README.md.

Метаданные берутся из первой строки problems/<папка>/README.md:
<!-- meta: number=1; title=Two Sum; difficulty=Easy; topic=Hash Table; url=https://leetcode.com/problems/two-sum/ -->
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START, END = "<!-- TABLE:START -->", "<!-- TABLE:END -->"
META_RE = re.compile(r"<!--\s*meta:(.*?)-->", re.S)


def read_meta(readme: Path) -> dict:
    match = META_RE.search(readme.read_text(encoding="utf-8"))
    if not match:
        raise ValueError(f"нет блока meta в {readme}")
    pairs = (item.split("=", 1) for item in match.group(1).split(";") if "=" in item)
    return {k.strip(): v.strip() for k, v in pairs}


def build_table() -> str:
    rows = []
    for readme in (ROOT / "problems").glob("*/README.md"):
        meta = read_meta(readme)
        folder = readme.parent.name
        rows.append((int(meta["number"]), meta, folder))
    rows.sort(key=lambda r: r[0])

    lines = [
        "| # | Задача | Сложность | Тема | Решение |",
        "|---|--------|-----------|------|---------|",
    ]
    for number, meta, folder in rows:
        lines.append(
            f"| {number} | [{meta['title']}]({meta['url']}) | {meta['difficulty']} "
            f"| {meta['topic']} | [Python](problems/{folder}/solution.py) |"
        )
    stats = {d: sum(m["difficulty"] == d for _, m, _ in rows) for d in ("Easy", "Medium", "Hard")}
    summary = f"Решено: **{len(rows)}** (Easy {stats['Easy']} · Medium {stats['Medium']} · Hard {stats['Hard']})"
    return summary + "\n\n" + "\n".join(lines)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    README.write_text(f"{head}{START}\n{build_table()}\n{END}{tail}", encoding="utf-8")


if __name__ == "__main__":
    main()
