# p42
import itertools


class Solve(object):
    def __init__(self):
        self.triangle_word_counter = 0
        self.words = []
        self.filename = './p042_words.txt'

        with open(self.filename, 'r') as fd:
            for line in fd:
                for word in line.split(','):
                    self.words.append(word.strip('"'))

    def value(self, word):
        return sum([ord(x) - ord('A') + 1 for x in word])

    def triangle_stream(self):
        """Infinite triangle stream"""
        for n in itertools.count(1):
            yield n*(n+1)/2

    def is_triangle(self, value):
        for t in self.triangle_stream():
            if t > value:
                return False
            if t == value:
                return True

    def solve(self):
        for word in self.words:
            print word, self.value(word)
            if self.is_triangle(self.value(word)):
                self.triangle_word_counter += 1
        return self.triangle_word_counter


s = Solve()
print s.solve()