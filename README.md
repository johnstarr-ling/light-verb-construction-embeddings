# Give or Take a Few Representations

This repository is home base for the "Give or take a few representations", one of 5 final projects for the FA '22 iteration of _Computational Linguistics II_ (LING 4435) at Cornell University; a rough outline of the topics covered in this course can be found [here](https://vansky.github.io/courses/2020-cl2.html). This project is in collaboration with [Jacob Matthews](https://github.com/jam963) (second author) and [Dr. Marten van Schijndel](https://vansky.github.io/) (course instructor, advisor).

### Project Overview

The main goal of this project is to examine how large language models represent amibiguous phrasal verb constructions (PVCS). For an example of an ambiguous PVC, see how the phrase "given in" is used in (1):

```
(1) The teacher had given in to the student's request.
```

... and in (2):

```
(2) The assignments the teacher had given in class were too long!
```

In (1), "given in" is being used as a phrasal verb. In (2), "given in" is a sequence of words that do not act as a constituent.

To study this phenomena, we compare {static, contextual} representations of these ambiguous PVCs from a number of popular embedding sources (GLoVe, word2vec, BERT, GPT, and RoBERTa). We also see how the representations themselves perform on a classification task that identifies if an ambiguous phrasal verb truly phrasal or not.

The current dataset for this project is a Frankensteinien amalgamation of the dataset constructed by Yuancheng Tu and Dan Roth for their 2012 paper ["Sorting Out the Most Confusing English Phrasal Verbs"](https://cogcomp.seas.upenn.edu/page/publication_view/689). Major thanks to them for building an easy-to-use dataset!

### Running Our Code
Some book notes on the notebooks:

- Please see `requirements.txt` for all packages needed to run our notebooks and scripts. Besides the usual culprits involved in neural work, you'll also need to install to install [minicons](https://pypi.org/project/minicons/) (Misra 2022).
- We collect embedding representations of the {full phrasal verb, the verb only, and the non-verbs only} from [BERT](https://huggingface.co/bert-base-cased) (default in `miniconsbatched.py`), [GPT2](https://huggingface.co/gpt2) , and [RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta). Each set of representations for each model has dimensions `(3, 1224, 768)`, with 3 representing the number of layers we collected from (6, 9, 12 (aka last layer)), 1224 representing the number of sentences in the corpus, and 768 representing the dimensionality of each embedding.  All of the embeddings can be found in the `representations` folder in the main repository and are stored as numpy binary files -- you can load them in with `np.load`. To get these embedding representations yourself, run the `get_representations.ipynb` notebook. 

### Citations
- Tu, Y., & Roth, D. (2012). Sorting out the most confusing English phrasal verbs. In _SEM 2012: The First Joint Conference on Lexical and Computational Semantics–Volume 1: Proceedings of the main conference and the shared task, and Volume 2: Proceedings of the Sixth International Workshop on Semantic Evaluation (SemEval 2012)._ (pp. 65-69).
- Misra, K. (2022). minicons: Enabling Flexible Behavioral and Representational Analyses of Transformer Language Models. _arXiv preprint_ arXiv:2203.13112.