class Permutation:
    def __init__(self, n):
        self.n = n
        self.perm = [i for i in range(n)]

    def multi(self, other):
        for i in range(self.n):
            self.perm[i] = other.perm[self.perm[i]]

    def reverse(self):
        tmp = range(self.n)
        for i in range(self.n):
            tmp[self.perm[i]] = i
        self.perm = self.perm

    def print(self):
        print(self.perm)
        pass


class ShreierTree:
    def __init__(self):
        pass


a = Permutation(10)
a.print()
