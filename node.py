# python node.py

from queue import Queue

class Node:
    def __init__(self, array):
        self.array = array
        self.sample = len(array)
        self.features = len(array[0])
        self.left = None 
        self.right = None

    def move_left(self, array):
        self.left= Node([self.array[i] for i in array])
        return self.left

    def move_right(self, array):
        self.right = Node([self.array[i] for i in array])
        return self.right

    def display(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.__len__() > 0:
            current = queue.dequeue()
            print([current.sample, current.array])
            if current.left is not None:
                queue.enqueue(current.left)
            if current.right is not None:
                queue.enqueue(current.right)


if __name__ == "__main__":
    array = [
        [10, 32], 
        [20, 56],
        [35, 44],
        [ 5, 62],
        [15, 25],
    ]
    node_1 = Node(array)
    print("OBSREVATIONS:", node_1.sample)
    print("FEATURES:", node_1.features)
    node_2 = node_1.move_left([0, 1, 2])
    node_3 = node_1.move_right([3, 4])
    node_4 = node_2.move_left([0])
    node_5 = node_2.move_right([1, 2])
    node_6 = node_3.move_left([0])
    node_7 = node_3.move_right([1])

    print(node_1.display(node_1))
