import json
import sqlite3
from pathlib import Path
from typing import Any, Dict, List


class ResultStorage:
    def __init__(self, database_path: Path, results_json_path: Path) -> None:
        self.database_path = database_path
        self.results_json_path = results_json_path
        self._initialize_database()

    def _initialize_database(self) -> None:
        with sqlite3.connect(self.database_path) as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS scrape_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_url TEXT NOT NULL,
                    scraped_at TEXT NOT NULL,
                    title TEXT,
                    summary TEXT,
                    key_points TEXT NOT NULL,
                    topics TEXT NOT NULL,
                    entities TEXT NOT NULL,
                    sentiment TEXT NOT NULL,
                    data_found TEXT NOT NULL,
                    result_json TEXT NOT NULL,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            connection.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_scrape_results_source_url
                ON scrape_results(source_url)
                """
            )

    def save_result(self, result: Dict[str, Any]) -> None:
        with sqlite3.connect(self.database_path) as connection:
            connection.execute(
                """
                INSERT INTO scrape_results (
                    source_url,
                    scraped_at,
                    title,
                    summary,
                    key_points,
                    topics,
                    entities,
                    sentiment,
                    data_found,
                    result_json
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    result["source_url"],
                    result["scraped_at"],
                    result.get("title", ""),
                    result.get("summary", ""),
                    json.dumps(result.get("key_points", []), ensure_ascii=False),
                    json.dumps(result.get("topics", []), ensure_ascii=False),
                    json.dumps(result.get("entities", []), ensure_ascii=False),
                    result.get("sentiment", "neutral"),
                    json.dumps(result.get("data_found", []), ensure_ascii=False),
                    json.dumps(result, ensure_ascii=False),
                ),
            )

        self.export_all_to_json()

    def fetch_all_results(self) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.database_path) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(
                "SELECT result_json FROM scrape_results ORDER BY id ASC"
            ).fetchall()

        return [json.loads(row["result_json"]) for row in rows]

    def export_all_to_json(self) -> None:
        results = self.fetch_all_results()
        with self.results_json_path.open("w", encoding="utf-8") as file:
            json.dump(results, file, indent=2, ensure_ascii=False)
