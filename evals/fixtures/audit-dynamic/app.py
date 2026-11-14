import json
from pathlib import Path

import exporters


class ExportService:
    def __init__(self, runner):
        self._runner = runner

    def run(self, rows):
        return self._runner(rows)


def run(rows):
    config = json.loads(Path(__file__).with_name("config.json").read_text(encoding="utf-8"))
    return [getattr(exporters, f"export_{name}")(rows) for name in config["exporters"]]


def main():
    rows = [(1, "a"), (2, "b")]
    for output in ExportService(run).run(rows):
        print(output)


if __name__ == "__main__":
    main()
