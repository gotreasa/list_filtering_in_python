def filter_list(items: list) -> list:
    if not isinstance(items, list):
        raise ValueError("❗️ Input should be a list")
    result = []
    for item in items:
        if isinstance(item, int):
            result.append(item)
    return result
