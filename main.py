from test_shreier_sims import test
from shreier_sims import *

test()

outputFile = open('answer.txt', 'w')

N = 54

# наши образующие:
swap1 = [Permutation([1, 0] + list(range(2, 54))), Permutation(list(range(1, 18)) + [0] + list(range(18, 54)))]
swap2 = [Permutation(list(range(0, 18)) + [19, 18] + list(range(20, 54))), Permutation(list(range(0, 18)) + list(range(19, 36)) + [18] + list(range(36, 54)))]
swap3 = [Permutation(list(range(0, 52)) + [53, 52]), Permutation(list(range(0, 36)) + list(range(37, 54)) + [36])]
change = [Permutation(list(range(18, 36)) + list(range(0, 18)) + list(range(36, 54)))]
visible = [Permutation(list(range(18, 36)) + list(range(2, 18)) + list(range(36, 54)) + [1, 0])]

gen = set()
gen.update(visible)
gen.update(swap1)
gen.update(swap2)
gen.update(swap3)
gen.update(visible)

#Построение цепочки стабилизаторов
G = FullStableChain(list(range(53)), list(gen))

#Считаем размер группы
#outputFile.write(str(myStab.get_group_size()) + '\n\n')

#Считаем образующие стабилизатора. Вывод перестановки p в формате списка: p[i] = p(i)
#fS = myStab.get_generations(2)
#for sigma in fS:
#    outputFile.write(str(sigma) + '\n')
#outputFile.close()
print(G.get_group_size())
