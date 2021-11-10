class Counter:
    def __init__(self) -> None:
        self.value = 0

    def add(self, offset) -> None:
        # value += offset
        self.value += offset

    def get(self) -> int:
        return self.value


if __name__ == '__main__':
    counter = Counter()
    counter.add(5)
    found = counter.get()
    assert found == 0, found
