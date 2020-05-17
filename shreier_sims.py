# класс перестановок
class Permutation:
    def __init__(self, init_data):
        self.data = init_data[::]

    # длина перестановки
    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    # перемножение двух перестановок - возвращается новая
    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError
        n = len(self)
        tmp = Permutation(len(self))
        for i in range(n):
            tmp.data[i] = self[other[i]]
        return tmp


# =================================
# дерево Шрайера
class ShreierTree:
    class Node:
        def __init__(self, parent, edge, permutation_to_root):
            self.parent = parent
            self.edge = edge
            self.permutation_to_root
            pass

    # вход: x - вершина, которую хотим поместить в корень дерева, generations - набор образующих
    def __init__(self, x, generations):
        self.generations = set(generations)
        self.graph = {x: ShreierTree.Node()}
        self.__build_tree(x)

    # функция для построения дерева через dfs, не должна вызываться из вне, только из init-а
    def __build_tree(self, x):
        bfs = [x]
        ind = 0
        while ind < len(bfs):
            x = bfs[ind]
            # проходим по всем образующим, пытаясь применить их к нашей текущей x
            for gen in self.generations:
                # t - результат применения gen к x (gen(x))
                t = gen[x]
                # проверяем, что наш элемент ещё не лежит в дереве (что мы ещё его не просматривали)
                if self.graph[t] is None:

                    bfs.append(t)
            ind += 1
