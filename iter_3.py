class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.iter_stack = []
        self._prepare_iterator()

    def _prepare_iterator(self):
        """Инициализирует стек для итерирования."""
        self.iter_stack.append(iter(self.list_of_lists))

    def __iter__(self):
        return self

    def __next__(self):
        while self.iter_stack:
            try:
                item = next(self.iter_stack[-1])
                if isinstance(item, list):
                    self.iter_stack.append(iter(item))  # Если элемент список, добавляем его в стек
                else:
                    return item
            except StopIteration:
                self.iter_stack.pop()  # Удаляем текущий итератор, если закончился
        raise StopIteration

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

if __name__ == '__main__':
    test_3()