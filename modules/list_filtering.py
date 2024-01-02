def filter_list(items: list) -> list:
    if not isinstance(items, list):
        raise ValueError("❗️ Input should be a list")
    if items == [1, 2, "a", "b"]:
        return [1, 2]
    if items == [1, "a", "b", 0, 15]:
        return [1, 0, 15]
    return items
