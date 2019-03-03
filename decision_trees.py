import numpy as np
import utils
from tree import Tree, Node


class DecisionTree():
    def __init__(self):
        self.name = 'DecisionTree'
        self.classes = [0, 1]
        self.tree = None

    def split_column(self, X, y, column):
        '''Find the best split for a given column
        '''
        order = np.argsort(X[:, column])
        sortedX = X[order]
        sortedy = y[order]

        loss = np.inf
        leftX, rightX, lefty, righty = None, None, None, None

        i = 0
        local_i = 0
        for i in range(1, len(sortedX) - 1):
            local_loss = utils.entropy_split([list(sortedy[:i]),
                                            list(sortedy[i:])],
                                            self.classes)

            if local_loss < loss:
                local_i = i
                loss = local_loss
                leftX = sortedX[:i]
                rightX = sortedX[i:]
                lefty = sortedy[:i]
                righty = sortedy[i:]

        return sortedX[local_i][column], column, loss, leftX, rightX, lefty, righty

    def split(self, X, y):
        if X is None:
            return None, None, None, None, None, None, None
        columns = range(X.shape[1])

        # find the best loss between all split for all columns
        loss = np.inf
        value = None
        column = None
        leftX, rightX, lefty, righty = None, None, None, None
        
        for col in columns:
            results = self.split_column(X, y, col)
            (local_value, local_column, local_loss, local_leftX, local_rightX, local_lefty, local_righty) = results
            if local_loss < loss:
                value, column, loss, leftX, rightX, lefty, righty = results

        return value, column, loss, leftX, rightX, lefty, righty


    def fit(self, X, y, depth=0, max_depth=2):
        value, column, loss, leftX, rightX, lefty, righty = self.split(X, y)
        print leftX, lefty
        # print 'depht', depth, 'loss', loss, 'value', value
        if depth >= max_depth:
            return None
        else:
            t = Tree(value, column)
            if depth == 0:
                self.tree = t
            t.left_tree = self.fit(leftX, lefty, depth=depth+1, max_depth=max_depth)
            t.right_tree  = self.fit(rightX, righty, depth=depth+1, max_depth=max_depth)
        
        return t



if __name__ == '__main__':
    X = np.random.rand(1000, 10)
    y = np.array([(int(x[0] > 0.5) and int(x[1] > 0.5)) for x in X])

    dt = DecisionTree()
    # print('Split', dt.split(X, y))

    dt.fit(X, y)
    dt.tree.draw()