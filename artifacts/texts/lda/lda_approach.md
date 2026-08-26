> **Latent Dirichlet Allocation (LDA)** is a probabilistic topic-modeling method that represents each review as a mixture of latent topics and each topic as a distribution of words. The review corpus is converted into a bag-of-words representation using a constructed vocabulary dictionary. LDA then estimates the topic-word distributions and the proportion of each topic within every review.
>
> This approach allows a single review to express multiple concerns at once—such as staff behavior and service quality—which is especially important for business reviews that often describe several aspects of one experience.

#### < Why this approach? >

> Unlike K-Means, which assigns each review to one discrete cluster, LDA models topics as overlapping patterns across the corpus. Its topic-word distributions and document-topic weights help summarize recurring themes, compare the prevalence of issues, and identify the complaints most characteristic of negative reviews.