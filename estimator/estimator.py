'''
Module for training and evaluating the model.
'''
from rdkit.Chem import AllChem
# from .scorer import chemprop_scorer
from .scorer.scorer import get_scores



class Estimator():
    '''
    @params:
        model: model to train
        train_set: training dataset
        valid_set: validation dataset
        test_set: test dataset
        config: configuration
    '''
    def __init__(self, config, mols_ref=None):
        '''
        @params:
            config (dict): configurations
        '''
        # chemprop_scorer.device = config['device']
        self.batch_size = config['batch_size']
        self.objectives = config['objectives']
        self.fps_ref = [AllChem.GetMorganFingerprintAsBitVect(
            x, 3, 2048) for x in config['mols_ref']] if config['mols_ref'] else None

    def get_scores(self, mols):
        '''
        @params:
            mols: molecules to estimate score
        @return:
            dicts (list): list of score dictionaries
        '''
        dicts = [{} for _ in mols]
        for obj in self.objectives:
            scores = get_scores(obj, mols)
            for i, mol in enumerate(mols):
                dicts[i][obj] = scores[i]
        return dicts
