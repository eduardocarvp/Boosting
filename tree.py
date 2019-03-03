class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def left_child(self, value):
        self.left = Node(value)
        return self.left

    def right_child(self, value):
        self.right = Node(value)
        return self.right


class Tree():
    def __init__(self, value, column):
        self.value = value
        self.column = column
        self.left_tree = None
        self.right_tree = None

    def draw(self, depth=0):
        print str(self.value) + ' ' + str(self.column) + ' ' + str(depth)

        if self.left_tree is not None:
            self.left_tree.draw(depth=depth+1)
        if self.right_tree is not None:
            self.right_tree.draw(depth=depth+1)


    def __str__(self):
        return str(self.value) + ' ' + str(self.column)