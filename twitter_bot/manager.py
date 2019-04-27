import os
import re
import importlib
import pkgutil


def main():
    collectors = list()
    for _, name, _ in pkgutil.iter_modules(['./colls']):
        if not name.startswith('colls_'):
            continue
        imported = importlib.import_module('colls'+'.'+name, name)
        class_name = name.split('_')[-1]
        class_object = getattr(imported, class_name)
        collectors.append(class_object())

    for collector in collectors:
        collector.get_plans()


if __name__ == '__main__':
    main()

