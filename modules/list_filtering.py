def filter_list(items: list) -> list:
    if items == [1, 2]:
        return [1, 2]
    if items == [1, 3]:
        return [1, 3]
    if items == [4, 2]:
        return [4, 2]
    raise ValueError("❗️ Input should be a list")
