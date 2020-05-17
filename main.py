from functools import reduce


class Permutation:
    def __init__(self, init_data):
        self.data = init_data[::]

    def multi(self, other):
        for i in range(self.n):
            self.data[i] = other.data[self.data[i]]

    def reverse(self):
        tmp = list(range(self.n))
        for i in range(self.n):
            tmp[self.data[i]] = i
        self.data = self.data

    def __str__(self):
        return self.data.__str__()


def reverse(perm):
    tmp = Permutation(perm.n)
    for i in range(perm.n):
        tmp.data[perm.data[i]] = i
    return tmp


class Node:
    def __init__(self, x, parent):
        self.children = []
        self.parent = parent
        self.x = x
        self.s = 0


class Group:
    def __init__(self, n, generators):
        self.n = n
        self.generators = generators

    def orbit(self, x):
        o = [x]
        ind = 0
        while ind < len(o):
            for gen in self.generators:
                t = gen.data[o[ind]]
                while t != o[ind]:
                    if o.count(t) == 0:
                        o.append(t)
                    t = gen.data[t]
            ind += 1
        return o


class ShreierTree:
    def __init__(self, group, x):
        orbit = list(group.orbit(x))
        orbit.remove(x)
        self.root = x
        self.nodes = dict()
        self.nodes[x] = Node(x, -1)
        bfs = [x]
        ind = 0
        self.group = group
        while len(orbit) > 0:
            for gen in group.generators:
                gen_rev = gen
                gen_rev.reverse()
                t = gen_rev.data[bfs[ind]]
                if orbit.count(t) > 0:
                    orbit.remove(t)
                    node = Node(t, bfs[ind])
                    node.s = gen
                    self.nodes[bfs[ind]].children.append(t)
                    self.nodes[t] = node
                    bfs.append(t)
            ind += 1

    def print(self):
        for node in self.nodes:
            print("{", self.nodes[node].parent, "<-", self.nodes[node].x, " : ", self.nodes[node].s, "}")
            print(self.nodes[node].children)


class FullStableSequence:
    def __init__(self, group, base):
        self.n = group.n
        self.base = base
        self.generation
        self.T

# Применение перестановки b к перестановке a
def apply(a, b):
    tmp = Permutation(a.n)
    for i in range(a.n):
        tmp.data[i] = b.data[a.data[i]]
    return tmp


# Принимает порождающее множество для G_{w-1} и орбиту элемента w
# Возвращает порождающее множество для G_w
def make_gen(S, orbit):
    n = len(next(iter(S)))
    newS = set()
    for s in S:
        for u in orbit:
            newS.add(reduce(apply, [reverse(orbit[s[u]]), s, orbit[u]]))
    return newS


def test():
    a = Permutation(3)
    a.data = [0, 2, 1]
    b = Permutation(3)
    b.data = [1, 2, 0]
    a.multi(b)
    if a.data != [1, 0, 2]:
        print("!!!")


t12 = Permutation(4)
t12.data = [1, 0, 2, 3]
t23 = Permutation(4)
t23.data = [0, 2, 1, 3]
t34 = Permutation(4)
t34.data = [0, 1, 3, 2]
gener = [t12, t23, t34]
s4 = Group(4, gener)
ShreierTree(s4, 1).print()
