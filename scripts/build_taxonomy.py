from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "kwork-taxonomy.json"
OUT = ROOT / "TAXONOMY.md"


ORDER = [
    "Дизайн",
    "Разработка и IT",
    "Тексты и переводы",
    "SEO и трафик",
    "Соцсети и маркетинг",
    "Аудио, видео, съемка",
    "Бизнес и жизнь",
]


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    data.sort(key=lambda item: ORDER.index(item["top"]))
    lines = [
        "# Kwork: рубрики, подрубрики, типы и виды",
        "",
        "Источник: https://kwork.ru/categories. Снято 30.10.2026. Уровни: Рубрика → Подрубрика → Тип → Вид.",
        "",
    ]
    for category in data:
        lines.extend([f"## {category['top']}", "", f"Источник: {category['url']}", ""])
        for sub in category["subs"]:
            lines.extend([f"### {sub['name']}", "", f"Источник: {sub['url']}", ""])
            for kind in sub["types"]:
                lines.append(f"- **Тип:** {kind['name']}")
                views = kind["views"]
                if views:
                    lines.extend(f"  - **Вид:** {view['name']}" for view in views)
                else:
                    lines.append("  - **Вид:** —")
            lines.append("")
    OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"written {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
