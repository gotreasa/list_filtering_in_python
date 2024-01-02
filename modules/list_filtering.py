def is_integer(item) -> bool:
    return isinstance(item, int)


def filter_list(items: list) -> list:
    if not isinstance(items, list):
        raise ValueError("❗️ Input should be a list")
    result = []
    for item in filter(is_integer, items):
        result.append(item)
    return result
