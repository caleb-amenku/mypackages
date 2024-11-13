def top_n(items,n):
    """Return top n items in an array in desc order
    Args
        items(array): list or array-like objects
        n(int): number of items to be returned from the array

    Return:
        array of top-n items in descending order

    E.g. top_n([8,3,2,7,4],3)
    >>>[8,7,3]
    """
    for i in range(n):
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    top_n = items[-n:]

    return top_n[::-1]