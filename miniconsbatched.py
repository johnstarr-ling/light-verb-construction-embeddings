import numpy as np
from minicons import cwe
import torch

def generate_representations(words: list, contexts: list, 
                            model: str = 'bert-base-cased', 
                            batch_size: int = 8,
                            device: str = 'cpu',
                            layer=None) -> (np.ndarray, np.ndarray):
    """Returns representations and word-context pairs as a tuple of ndarrays.
       words: list-like of words.
       contexts: dict of {word: context} pairs.
       model: valid huggingface model.
       batch_size: desired size of batch (default is 8)
       device: device to run inference (default is cuda)
       
       returns: word representation vectors of shape (|words|, |vector|), 
                word-context pairs."""

    print('########################################')
    print('Running', model, 'for layer', str(layer), '!')
    model = cwe.CWE(model, device=device)
    batch_ranges = list(range(0, len(words), batch_size))
    batch_ranges.append(len(words))
    pairs = np.array(list(zip(contexts, words)))
    if type(layer) != int:
        vectors = [[] for i in range(len(layer))]
    else:
        vectors = []

    for i in range(1, len(batch_ranges)):
        ix_range = (batch_ranges[i-1], batch_ranges[i])
        # vectors.extend(model.extract_representation(pairs[ix_range[0]: ix_range[1]], layer=layer).numpy())
    
        # Multiple layers
        if type(layer)!=int:
            reps = model.extract_representation(pairs[ix_range[0]: ix_range[1]], layer=layer)
            reps = np.array([layer_reps.numpy() for layer_reps in reps])
            for i in range(len(reps)):
                vectors[i].extend(reps[i])
                
        # Single layer
        else:
            reps = model.extract_representation(pairs[ix_range[0]: ix_range[1]], layer=layer).numpy()
            vectors.extend(reps)
    print('Run complete.')
    print()
    return np.array(vectors), np.array(pairs)


