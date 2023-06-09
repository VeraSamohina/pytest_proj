def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
     В ином случае возвращается значение default
     :param collection - словарь
     :param key - ключ словаря
     :param default - значение по умолчанию
     :return - значение по ключу или по умолчанию
     """
    if key not in collection:
        return default
    return collection[key]