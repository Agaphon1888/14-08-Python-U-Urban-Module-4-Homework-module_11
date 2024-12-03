# Домашнее задание по теме "Интроспекция".
# Задание 2. Закрепить знания об интроспекции в Python. Создать персональную функцию для подробной интроспекции объекта.

import inspect
import types


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль объекта
    obj_module = obj.__module__

    # Другие свойства объекта
    additional_info = {}
    if isinstance(obj, (list, dict, set, tuple)):
        additional_info['length'] = len(obj)

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        **additional_info
    }


# Пример создания класса и объекта
class SampleClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


# Создаем экземпляр класса
sample_object = SampleClass("Alice")

# Получаем информацию об объекте
sample_info = introspection_info(sample_object)
print(sample_info)