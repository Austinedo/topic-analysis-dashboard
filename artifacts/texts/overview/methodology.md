This analysis evaluates three approaches to discovering recurring themes in negative business reviews. The methods were implemented chronologically as the modeling strategy evolved:

1. **K-Means clustering on a TF-IDF document-term matrix**
2. **K-Means clustering on SBERT semantic embeddings**
3. **Latent Dirichlet Allocation (LDA) topic modeling on a processed review corpus**

These approaches were selected because they represent different assumptions about the structure of review text and provide different perspectives on topic discovery.

### < Modeling Approaches >

#### 1. TF-IDF K-Means

> The TF-IDF K-Means approach emphasizes lexical patterns. Each review is represented by the importance of its words and phrases relative to the individual review and the overall corpus. K-Means then groups reviews according to similarity in this high-dimensional document-term space.

#### 2. SBERT K-Means

> The SBERT K-Means approach captures semantic similarity beyond exact word overlap. Reviews are encoded as dense sentence embeddings using a pretrained SBERT transformer, allowing reviews that use different wording but express similar meanings to be positioned closer together in the embedding space. K-Means is then applied to these semantic representations.

#### 3. Latent Dirichlet Allocation

> LDA provides a probabilistic view of latent topics and their distribution across reviews. Rather than assigning each review to one discrete cluster, LDA represents each review as a mixture of topics and each topic as a distribution over words. This representation is useful for customer reviews because a single review can discuss multiple aspects of an experience.

### < Comparative Rationale >

> Together, these methods support qualitative and quantitative comparison of how modeling choices affect the interpretation of customer feedback. TF-IDF K-Means emphasizes surface-level lexical similarity, SBERT K-Means emphasizes contextual semantic similarity, and LDA models overlapping latent themes across the corpus.
>
> The workflow begins with a common cleaned and filtered review dataset. It then branches into representation-specific preprocessing and modeling pipelines for TF-IDF K-Means, SBERT K-Means, and LDA. The resulting analyses are evaluated through their diagnostic metrics, topic or cluster interpretability, representative reviews, and operational relevance.