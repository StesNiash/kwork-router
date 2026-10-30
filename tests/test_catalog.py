import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "data" / "services.json").read_text(encoding="utf-8"))
        self.families = self.data["families"]

    def test_families_have_required_fields(self):
        required = {
            "id", "number", "title", "repo", "status", "wave",
            "price_from", "term", "summary", "bullets", "demo", "tone",
            "card", "repo_url",
        }
        for item in self.families:
            self.assertTrue(required.issubset(set(item)), item.get("id"))
            self.assertIn(item["status"], {"active", "ready", "planned"})
            self.assertGreater(item["price_from"], 0)
            self.assertGreaterEqual(len(item["bullets"]), 3)

    def test_ids_and_numbers_are_unique(self):
        ids = [item["id"] for item in self.families]
        numbers = [item["number"] for item in self.families]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(numbers), len(set(numbers)))

    def test_ready_cards_have_detail_files_and_demos(self):
        ready = [item for item in self.families if item["status"] in {"active", "ready"}]
        self.assertEqual(len(ready), 5)
        for item in ready:
            self.assertTrue((ROOT / item["card"]).is_file(), item["id"])
            self.assertTrue(item["repo_url"].startswith("https://github.com/"), item["id"])

    def test_cards_contain_publishable_sections(self):
        for item in self.families:
            if not item["card"]:
                continue
            text = (ROOT / item["card"]).read_text(encoding="utf-8")
            self.assertIn("## Раздел", text, item["id"])
            self.assertIn("## Описание", text, item["id"])
            self.assertIn("## Обложка", text, item["id"])
            self.assertIn("**Промпт для ChatGPT / Gemini:**", text, item["id"])

    def test_active_family_is_only_hermes(self):
        active = [item["id"] for item in self.families if item["status"] == "active"]
        self.assertEqual(active, ["hermes-vps"])

    def test_no_web_app_files(self):
        for name in ("index.html", "app.js", "styles.css"):
            self.assertFalse((ROOT / name).exists(), name)

    def test_no_secret_material(self):
        patterns = [
            r"\bsk-[A-Za-z0-9]{12,}",
            r"\b\d{6,}:[A-Za-z0-9_-]{20,}\b",
            r"API[_-]?KEY\s*=\s*['\"]?[A-Za-z0-9]{16,}",
            r"BEGIN (RSA|OPENSSH|EC) PRIVATE KEY",
        ]
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts:
                continue
            if path.suffix.lower() not in {".md", ".json", ".html", ".js", ".css", ".py"}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in patterns:
                self.assertIsNone(re.search(pattern, text), f"{path}: {pattern}")


if __name__ == "__main__":
    unittest.main()
