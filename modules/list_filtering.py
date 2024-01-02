def filter_list(items: list) -> list:
    if not isinstance(items, list):
        raise ValueError("❗️ Input should be a list")
    return items
