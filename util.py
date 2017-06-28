# util lib

def list2int(l):
    if not l:
        return 0
    s = 0
    for curr in l:
        assert isinstance(curr, int)
        s *= 10
        s += curr
    return s
