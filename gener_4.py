def flat_generator(list_of_lists):
    iter_stack = [iter(list_of_lists)]  # Стек для хранения текущих итераторов

    while iter_stack:
        try:
            item = next(iter_stack[-1])  # Брать следующий элемент из текущего итератора
            if isinstance(item, list):
                iter_stack.append(iter(item))  # Если элемент список, добавляем его в стек
            else:
                yield item  # Возвращаем элемент, если он не список
        except StopIteration:
            iter_stack.pop()  # Удаляем текущий итератор, если закончился

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

if __name__ == '__main__':
    test_3()