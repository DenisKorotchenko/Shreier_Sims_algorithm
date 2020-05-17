from shreier_sims import FullStableChain
from shreier_sims import Permutation


def test():
    gens1 = [Permutation([1, 0, 2, 3]), Permutation([0, 2, 1, 3]), Permutation([0, 1, 3, 2])]
    stab1 = FullStableChain(list(range(3)), gens1)
    assert (stab1.get_group_size() == 24)
    assert (stab1.contain(Permutation([1, 0, 2, 3]))[0] is True)
    assert (stab1.contain(Permutation([0, 1, 3, 2]))[0] is True)
