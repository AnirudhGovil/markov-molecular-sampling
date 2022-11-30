from MARS.estimator.scorer.scorer import get_scores
from MARS.estimator.estimator import Estimator
from MARS.datasets.utils import load_mols, load_vocab, Vocab

def test_get_scores():
    k = get_scores('test', [None])
    assert(type(k) == list)