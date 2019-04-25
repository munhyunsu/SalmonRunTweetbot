import os
import re
import importlib
import pkgutil

def get_files(path, ext='', recursive=False):
    """
    Read all files in path
    :param path: path for reading
    :return: absolute path of all files in directory list
    """
    path_list = [path]

    while len(path_list) > 0:
        cpath = path_list.pop()
        with os.scandir(cpath) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    if entry.name.endswith(ext):
                        yield entry.path
                    else:
                        if recursive:
                            path_list.append(entry.path)


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

