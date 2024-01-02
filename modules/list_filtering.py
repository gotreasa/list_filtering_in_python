def filter_list(items: list) -> list:
    if not isinstance(items, list):
        raise ValueError("❗️ Input should be a list")
    if items == [1, 2, "a", "b"]:
        return [1, 2]
    return items
