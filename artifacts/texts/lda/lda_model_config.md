> The LDA pipeline was tuned to produce topics that were both quantitatively strong and easy for people to interpret. Vocabulary filtering and text-preprocessing settings were adjusted to remove unhelpful terms and retain words that contributed to coherent topic keywords.

#### < Final configuration >

| Component | Selected setting |
|---|---|
| Input representation | Processed bag-of-words corpus and filtered vocabulary dictionary |
| Corpus-dictionary filtering | `no_below = 3`, `no_above = 0.40` |
| Final number of topics | `num_topics = 3` |
| Evaluation metrics | $C_v$ coherence and $C_{UMass}$ coherence |

> The final model uses **three topics**. This selection was supported by the quantitative evaluation and was consistent with the small number of dominant groupings suggested by the K-Means analyses.

#### < Tuning results >

> The vocabulary dictionary and preprocessing pipeline were iteratively tuned to improve the interpretability of topic keywords. The final corpus-dictionary filtering removes terms that occur too infrequently (`no_below`) and terms that occur in too large a share of documents (`no_above`).
> 
> The selected configuration produced exceptionally high **$C_v$** and **$C_{UMass}$** topic-coherence scores, indicating that the highest-weighted words within each topic are semantically related. High coherence does not mean that every review belongs to only one topic; LDA still allows individual reviews to contain a mixture of topics.