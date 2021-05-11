# 3▹ Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyświetlenie kolejki, sprawdzenie czy jest pusta,
# dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).


class Queue:
    def __init__(self, queue_list):
        self.queue_list = queue_list

    def show(self):
        print(self.queue_list)

    def is_empty(self):
        return len(self.queue_list) == 0

    def put(self, item):
        self.queue_list.append(item)
        print('Dodano element!')

    def get(self):
        try:
            return self.queue_list.pop(0)
        except IndexError:
            print('Nie ma więcej elementów na liście!')


if __name__ == "__main__":
    queue_list = ["one element", "second element", "third element"]
    queue1 = Queue(queue_list)
    queue1.show()

    print(queue1.is_empty())

    item = "item1"
    queue1.put(item)

    queue1.get()