import numpy as np

def gini(x, classes):
    '''Calculates the gini index of a single group of elements
    gini(x, c) = 1 - < w, w >
    where w is the counting vector of the number of elements
    of each class present on x
    '''
    size = float(len(x))
    w = np.array([x.count(c) / size for c in classes])

    return 1 - np.dot(w, w)


def entropy(x, classes):
    '''Calculates the entropy of a given vector with respect
    to the given classes
    E = - sum_i p_i log(p_i)    
    '''
    size = float(len(x))
    w = [x.count(c) / size for c in classes]
    w = np.array([p for p in w if p != 0])
    lw = np.log(w) / np.log(2)

    return - np.dot(w, lw)


def gini_split(X, classes):
    '''Calculate the total gini of a split.
    The gini is given by the gini of each split group pondered
    by the size of the group
    '''
    total_size = float(sum(len(x) for x in X))

    gini_groups = [gini(x, classes) * len(x) / total_size for x in X]

    return sum(gini_groups)


def entropy_split(X, classes):
    '''Calculate the total gini of a split.
    The gini is given by the gini of each split group pondered
    by the size of the group
    '''
    total_size = float(sum(len(x) for x in X))

    entropy_groups = [entropy(x, classes) * len(x) / total_size for x in X]

    return sum(entropy_groups)


if __name__ == '__main__':
    print entropy_split([[1,1,1,0,0], [0,0,0]], [0,1])
