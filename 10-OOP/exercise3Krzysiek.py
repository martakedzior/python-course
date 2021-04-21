class Queue:
    queue_list = []

    def __init__(self, item):
        self.queue_list.append(item)

    def put(self, item):
        return self.queue_list.append(item)

    def get(self):
        if len(self.queue_list) != 0:
            return self.queue_list.pop(0)

    def show_items(self):
        return self.queue_list

    def check_if_empty(self):
        return len(self.queue_list) == 0


if __name__ == '__main__':
    object1 = Queue("B")
    print(object1.show_items())
    print(f'Is empty: {object1.check_if_empty()}')
    object1.put('A')
    object1.put('E')
    print(object1.show_items())
    object1.get()
    print(object1.show_items())
    object1.get()
    object1.get()
    print(object1.show_items())
    print(f'Is empty: {object1.check_if_empty()}')