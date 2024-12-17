def shellSort(iterable,key=lambda x:x,reverse=False):
    n = len(iterable)
    iterable = iterable[:]
    gap = n//2

    while gap > 0:
        for i in range(gap,n):
            temp = iterable[i]
            j = i
            while j >= gap and (key(iterable[j-gap]) > key(temp)) != reverse:
                iterable[j] = iterable[j-gap]
                j-=gap
            iterable[j] = temp

        gap = n//2


    return iterable