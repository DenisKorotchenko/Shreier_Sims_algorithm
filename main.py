from test_shreier_sims import test
from shreier_sims import *

test()

outputFile = open('answer.txt', 'w')

cards = 54

# наши образующие:
swap1 = [Permutation([1, 0] + list(range(2, cards))), Permutation(list(range(1, cards//3)) + [0] + list(range(cards//3, cards)))]
swap2 = [Permutation(list(range(0, cards//3)) + [cards//3+1, cards//3] + list(range(cards//3+2, cards))), Permutation(list(range(0, cards//3)) + list(range(cards//3+1, cards//3*2)) + [cards//3] + list(range(cards//3*2, cards)))]
swap3 = [Permutation(list(range(0, cards-2)) + [cards-1, cards-2]), Permutation(list(range(0, cards//3*2)) + list(range(cards//3*2+1, cards)) + [cards//3*2])]
change = [Permutation(list(range(cards//3, cards//3*2)) + list(range(0, cards//3)) + list(range(cards//3*2, cards)))]
visible = [Permutation(list(range(cards//3, cards//3*2)) + list(range(2, cards//3)) + list(range(cards//3*2, cards)) + [1, 0])]

gen = set()
gen.update(visible)
gen.update(swap1)
gen.update(swap2)
gen.update(swap3)
gen.update(visible)

G = FullStableChain(list(range(53)), list(gen))

print(G.get_group_size())
