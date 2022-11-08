from MARS.estimator.estimator import Estimator
from MARS.datasets.utils import load_mols, load_vocab, Vocab

# tests with default file paths
def test_estimator_class():
    k = load_mols('/home/aneesh/UbuntuStorage/Homework/D4/MARS/data', 'custom.txt')
    e = Estimator({'batch_size': 5, 'objectives': [], 'mols_ref': k})
    scores = e.get_scores([])

    assert(type(scores) == list)