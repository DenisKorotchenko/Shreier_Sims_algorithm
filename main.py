from test_shreier_sims import test
from shreier_sims import *

test()

cards = 54

# наши образующие:
change = Permutation(list(range(cards//3, cards//3*2)) + list(range(0, cards//3)) + list(range(cards//3*2, cards)))
visible = Permutation([cards-1, cards-2] + list(range(cards//3, cards//3*2-2)) + list(range(0, cards//3)) + list(range(cards//3*2-2, cards-2)))

print(change.data)
print(visible.data)

G = FullStableChain(list(range(cards-1)), list({change, visible}))
#genS54 = {Permutation(list(range(1, 54)) + [0]), Permutation([1, 0] + list(range(2, 54)))}
#G = FullStableChain(list(range(53)), list(genS54))


cards_pairs = cards//2
change_pairs = Permutation(list(range(cards_pairs//3, cards_pairs//3*2)) + list(range(cards_pairs//3)) + list(range(cards_pairs//3*2, cards_pairs)))
visible_pairs = Permutation([cards_pairs-1] + list(range(cards_pairs//3, cards_pairs//3*2-1)) + list(range(cards_pairs//3)) + list(range(cards_pairs//3*2-1, cards_pairs-1)))

G_pairs = FullStableChain(list(range(cards_pairs-1)), list({change_pairs, visible_pairs}))

print(G.contain(Permutation([1, 0] + list(range(2, cards)))))

print(G.get_group_size())
print(G_pairs.get_group_size() * (2**cards_pairs))