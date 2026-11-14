from names import normalize_name


def old_report(rows):
    counts = {}
    for row in rows:
        name = normalize_name(row["name"])
        counts[name] = counts.get(name, 0) + 1
    return counts


def new_report(rows):
    counts = {}
    for row in rows:
        name = row["name"]
        counts[name] = counts.get(name, 0) + 1
    return counts
