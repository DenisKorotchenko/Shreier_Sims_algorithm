# класс перестановок
class Permutation:
    def __init__(self, init_data):
        self.data = init_data

    # длина перестановки
    def __len__(self):
        return len(self.data)

    # переопределение []
    def __getitem__(self, item):
        return self.data[item]

    @staticmethod
    def id(n):
        return Permutation(list(range(n)))

    # перемножение двух перестановок - возвращается новая
    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError
        tmp = Permutation.id(len(self))
        for i in list(range(0, len(self))):
            tmp.data[i] = self[other[i]]
        return tmp

    # обращение перестановки - возвращается новая
    def __invert__(self):
        tmp = Permutation.id(len(self))
        for i in range(len(self)):
            tmp.data[self[i]] = i
        return tmp

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(tuple(self.data))


# =================================
# дерево Шрайера
class ShreierTree:

    # class Node:
    #    def __init__(self, parent, edge, permutation_to_root):
    #        self.parent = parent
    #        self.edge = edge
    #        pass

    # вход: x - вершина, которую хотим поместить в корень дерева, generations - набор образующих
    def __init__(self, x, generations):
        self.generations = set(generations)
        n = 0
        if len(generations) > 0:
            n = len(generations[0])
        self.orbit = {x: Permutation.id(n)}
        self.decomposition = {self.orbit[x]: []}
        self.__build_tree(x)

    # функция для построения дерева через bfs, не должна вызываться из вне, только из init-а
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
                if self.orbit.get(t) is None:
                    orbit = gen * self.orbit[x]
                    self.orbit[t] = orbit
                    self.decomposition[orbit] = self.decomposition[self.orbit[x]] + [gen]
                    bfs.append(t)
            ind += 1


# ========================
class FullStableChain:
    # строим полную цепочку стабилизаторов
    # вход: base - база, generations
    def __init__(self, base, generations):
        self.base = base[::]
        if len(generations) == 0:
            self.n = 0
        else:
            self.n = len(generations[0])
        # chain - цепочка, которая хранит непосредственно деревья Шрайера
        self.chain = [ShreierTree(base[0], generations)]
        for i in range(len(base) - 1):
            gen = self.next_stabilizer_generations(i)
            gen = self.normalize(gen)
            self.chain.append(ShreierTree(base[i + 1], list(gen)))

    # воспользуемся леммой Шрайера: по chain[i] сгенерируем образующие стабилизатора (следующей подгруппы)
    def next_stabilizer_generations(self, i):
        ans = set()
        # проходим по всем образующим из нашей текущей подгруппы
        for gen in self.chain[i].generations:
            # идём по всем элементам орбиты
            for a in self.chain[i].orbit:
                # применяет лемму
                ans.add(~self.chain[i].orbit[gen[a]] * gen * self.chain[i].orbit[a])
        return ans

    # фильтр Симса (https://ru.wikipedia.org/wiki/Алгоритм_Шрайера_—_Симса#Просеивание_генераторов)
    def normalize(self, generations):
        new_gen = set()
        base = [{} for i in range(self.n)]
        for gen in generations:
            for x in range(self.n):
                if gen.data[x] != x:
                    if gen.data[x] in base[x]:
                        gen = (~gen) * base[x][gen.data[x]]
                    else:
                        base[x][gen.data[x]] = gen
                        new_gen.add(gen)
                        break
        return new_gen

    # возвращает сильное порождающее множество
    def gen_strong_forming_set(self):
        ans = set()
        # рассматриваем все возможные элементы из каждого дерева
        # set обеспечивает уникальность, можем об этом не думать
        for t in self.chain:
            ans.update(t.orbit.values())
        return ans

    # возвращает набор образующих для i-й подгруппы
    def get_generations(self, i):
        return self.chain[i].generations

    # для данной цепочки стабилизаторов вернуть размер соответствующей группы
    def get_group_size(self):
        ans = 1
        # len(t.orbit) - размер конкретного дерева в цепи
        for t in self.chain:
            ans *= len(t.orbit)
        return ans

    # выдает элементы орбиты первого элемента базы как множество
    def get_orbit(self):
        return self.chain[0].orbit.keys()

    # проверяет, содержится ли permutation в группе
    def contain(self, permutation):
        decomposition = []
        for i in range(len(self.base)):
            u = permutation.data[self.base[i]]
            if u not in self.chain[i].orbit:
                return False
            permutation = ~self.chain[i].orbit[u] * permutation
            decomposition.extend(self.chain[i].decomposition[self.chain[i].orbit[u]])
        # если мы смогли дойти до id, то всё ок, иначе - поражение
        if permutation == Permutation.id(self.n):
            return True, decomposition
        return False
