def BubbleSort(iterable, key=lambda x: x,reverse=False):

    n = len(iterable)
    iterable = iterable[:]
    for j in range(n):
        for i in range(n-1):
            if (key(iterable[i]) > key(iterable[i+1])) != reverse:
                iterable[i], iterable[i+1] = iterable[i+1], iterable[i]

    return iterable



