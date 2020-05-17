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


#=================================