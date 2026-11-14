import json


def export_csv(rows):
    return "\n".join(",".join(str(v) for v in row) for row in rows)


def export_legacy_xml(rows):
    cells = "".join(f"<row>{','.join(map(str, row))}</row>" for row in rows)
    return f"<rows>{cells}</rows>"


def export_json(rows):
    return json.dumps(rows)
