import os


def save(path, data):
    if data is not None:
        # check whether the data is empty
        if len(data) > 0:
            # must write a temp file first and then replace, so readers never see half the data
            tmp = path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                # write the data
                f.write(data)
            os.replace(tmp, path)
            return None
        else:
            return "empty"
    else:
        return "missing"
