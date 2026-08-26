> This analysis examines negative customer reviews (ratings of 3 stars or below) to identify recurring concerns. It assumes that reviews describing similar experiences will have similar meanings, even when they use different words, and that each review can be assigned to one main group.
> 
> Reviews are cleaned to remove HTML and web artifacts, URLs, and email addresses. The filtered reviews are then converted into **SBERT embeddings**—dense numerical representations that capture the meaning and context of each review. **K-Means clustering** groups reviews with similar embeddings, using cosine-based semantic similarity after the embeddings are normalized. We interpret each group by reviewing the examples closest to its cluster center.

#### < Cosine similarity and K-Means >

> K-Means normally minimizes squared Euclidean distance. To make this compatible with cosine similarity, each SBERT embedding is $\ell_2$-normalized to have length 1. For two normalized embeddings \(x\) and \(y\):
>
> $$
> \lVert x-y \rVert_2^2 = \lVert x \rVert_2^2 + \lVert y \rVert_2^2 - 2x^\top y = 2 - 2\cos(\theta)
> $$
> 
> Because $\cos(\theta)=x^\top y$ for unit-length vectors, minimizing Euclidean distance is equivalent to maximizing cosine similarity. This lets K-Means form clusters based on semantic similarity without changing its standard optimization process.

#### < Why this approach? >

> SBERT + K-Means is a semantic alternative to TF-IDF + K-Means. It can group reviews that describe a similar issue with different wording, making it better suited for customer feedback where people express comparable experiences in many ways. However, each review is still assigned to only one cluster, even when it discusses multiple concerns. It is therefore a useful intermediate approach before multi-topic methods such as LDA.