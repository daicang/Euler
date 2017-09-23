# 54
from collections import Counter, defaultdict


class Card(object):
    def __init__(self, s):
        self.value, self.color = Solve.orders[s[:-1]], s[-1:]

class Solve(object):
    orders = {r:i for i, r in enumerate('23456789TJQKA', 1)}

    def __init__(self):
        self.nr_p1win = 0
        with open('p054_poker.txt', 'r') as fd:
            self.source = fd.read()


    def royal_flush(self, cards):
        vals = {x.value for x in cards}
        colors = {x.color for x in cards}
        return vals == {9, 10, 11, 12, 13} and len(colors) == 1

    def straight_flush(self, cards):
        colors = {x.color for x in cards}
        if len(colors) == 1:
            vals = [x.value for x in cards]
            if {min(vals) + x for x in range(5)} == set(vals):
                return min(vals)
        return False

    def four_of_a_kind(self, cards):
        d = Counter([x.value for x in cards])
        l = [order for order, count in d.iteritems() if count >= 4]
        if l:
            assert len(l) == 1
            return l[0]
        return False

    def full_house(self, cards):
        d = Counter([x.value for x in cards])
        if set(d.values()) == {2, 3}:
            return max(d.keys())
        return False

    def flush(self, cards):
        colors = [x.color for x in cards]
        return len(set(colors)) == 1

    def straight(self, cards):
        vals = [x.value for x in cards]
        if set(vals) == {min(vals) + x for x in range(5)}:
            return min(vals)
        return False

    def three_of_a_kind(self, cards):
        d = Counter([x.value for x in cards])
        l = [order for order, count in d.iteritems() if count >= 3]
        if l:
            assert len(l) == 1
            return l[0]
        return False

    def two_pairs(self, cards):
        d = Counter([x.value for x in cards])
        l = [order for order, count in d.iteritems() if count >= 2]
        if len(l) >= 2:
            return max(l)
        return False

    def one_pair(self, cards):
        d = Counter([x.value for x in cards])
        l = [order for order, count in d.iteritems() if count >= 2]
        if l:
            return max(l)
        return False

    def high_card_cmp(self, cards1, cards2):
        return sorted([x.value for x in cards1], reverse=True) > sorted([x.value for x in cards2], reverse=True)

    def solve(self):
        def last_cmp(func):
            return func == self.one_pair

        def compare(evalf, c1, c2):
            r1, r2 = evalf(c1), evalf(c2)
            if r1 and r2 is False:
                return 1
            elif r2 and r1 is False:
                return 2
            elif r1 is False and r2 is False:
                return 0
            else:
                if isinstance(r1, int):
                    assert isinstance(r2, int)
                    if r1 != r2:
                        return 1 if r1 > r2 else 2
                else:
                    return 1 if self.high_card_cmp(c1, c2) else 2

        for line in self.source.splitlines():
            c1 = [Card(x) for x in line.split()[:5]]
            c2 = [Card(x) for x in line.split()[5:]]

            for evf in (self.royal_flush, self.straight_flush, self.four_of_a_kind,
                        self.full_house, self.flush, self.straight, self.three_of_a_kind,
                        self.two_pairs, self.one_pair):

                result = compare(evf, c1, c2)
                if result == 1:
                    self.nr_p1win += 1
                    break
                elif result == 2:
                    break
                else: # tie
                    if last_cmp(evf):
                        if self.high_card_cmp(c1, c2):
                            self.nr_p1win += 1
                        break

        return self.nr_p1win

s = Solve()
print(s.solve())