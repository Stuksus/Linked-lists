"""
Вариант связного списка №3
"""
VALUE = 1
NEXT = 2
PREV = 0


def add_to_back(value, head_local=None):
    item = [None, value, None]
    if head_local is None:
        head_local = item
    else:
        # First find the tail of the list
        tail = head_local
        while tail[NEXT] is not None:
            tail = tail[NEXT]
        item[PREV] = tail
        tail[NEXT] = item
    return head_local


def add_to_front(value, dll=None):
    if dll is not None:
        item = [None, value, dll]
        dll[PREV] = item
        return item
    else:
        head_local = [None, value, None]
        return head_local


def print_one_by_one(dll):
    if dll:
        tail = dll
        values = [tail[VALUE]]
        while tail[NEXT] is not None:
            tail = tail[NEXT]
            values.append(tail[VALUE])
        for value in values:
            print(value)
    else:
        raise SystemExit('Переданный вами связный список пуст')


def get_by_index(dll, index=None):
    try:
        tail = dll
        values = [tail[VALUE]]
        elements = [tail]
        while tail[NEXT] is not None:
            tail = tail[NEXT]
            values.append(tail[VALUE])
            elements.append(tail)
        if index is not None:
            return values[index]
        else:
            return values, elements
    except IndexError:
        raise SystemExit('Вы ввели неверный индекс, попробуйте снова')


def remove_from_end(dll):
    if dll:
        tail = dll
        while None not in tail[NEXT]:
            tail = tail[NEXT]
        tail[NEXT] = None
        return dll
    else:
        raise SystemExit('Переданный вами связный список пуст')


def remove_from_front(dll):
    if dll:
        head_from_dll = dll[NEXT]
        head_from_dll[PREV] = None
        return head_from_dll
    else:
        raise SystemExit('Переданный вами связный список пуст')


def search_for_value(dll, value):
    try:
        if dll:
            val, el = get_by_index(dll)
            index = val.index(value)
            return index
        else:
            raise SystemExit('Переданный вами связный список пуст')

    except ValueError:
        raise SystemExit('Введенное значение отсутствует в связанном списке')
