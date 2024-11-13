from mypackages import myModule

def test_top_n(items,n):
    """
    Makes sure top_n works
    E.g. top_n([8,3,2,7,4],3)
    >>>[8,7,3]
    """

    assert myModule.top_n([8,3,2,7,4],3) == [8,7,3], 'Incorrect'
    assert myModule.top_n([10,1,12,9,2],2) == [12,10,9], 'Incorrect'
    assert myModule.top_n([1,2,3,4,5],5) == [5,4,3,2,1], 'Incorrect'
