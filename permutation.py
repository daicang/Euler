# Permutation lib


def permutation(s):
    """
    @s: list of elements, eg: [1,2,3]
    return: list of permutations, eg: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    """
    ret = []
    length = len(s)

    if length == 0:
        return ret
    if length == 1:
        return [s]

    curr = s[0]
    for prev in permutation(s[1:]):
        for i in range(length):
            ret.append(prev[:i] + [curr] + prev[i:])
    return ret