from datetime import datetime


def logger(path):
    def logger_(old_function):
        logs = {'start': datetime.now(), 'name': old_function.__name__}

        def new_function(*args, **kwargs):
            nonlocal logs
            result = old_function(*args, **kwargs)
            logs['result'] = result
            logs['arguments'] = []
            if args:
                logs['arguments'].append(args)
            if kwargs:
                logs['arguments'].append(kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                text = f"Функция {logs['name']}, была запущена {logs['start']}" \
                       f"\nс аргументами {logs['arguments']}" \
                       f"\nи вернула результат {logs['result']}\n"
                f.write(text)

            return result

        return new_function

    return logger_
