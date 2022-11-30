from MARS.datasets.utils import load_mols, load_vocab, Vocab

# tests with default file paths
def test_load_mols():
    k =load_mols('C:\Users\Ani\Desktop\DDDD\MARS\data', 'custom.txt')
    assert(type(k) == list)

    print("load mols test passed")

def test_load_vocab():
    config = {'data_dir': 'C:\Users\Ani\Desktop\DDDD\MARS\data', 'vocab': 'chembl', 'vocab_size': 1000}
    vocab = load_vocab(config['data_dir'], config['vocab'], config['vocab_size'])

    assert(type(vocab) == Vocab)

    print("load vocab test passed")
