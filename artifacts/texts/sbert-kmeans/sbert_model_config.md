> The SBERT + K-Means model was evaluated across multiple cluster counts to identify a configuration that balanced quantitative cluster quality with practical interpretability. While the elbow plot showed a more noticeable bend than the TF-IDF model, silhouette scores dropped sharply after \(k=3\). Many reviews also had negative silhouette values across the tested configurations, indicating that the data do not separate cleanly into distinct clusters.

#### < Final configuration >

| Component | Selected setting |
|---|---|
| Text representation | Pre-trained SBERT sentence embeddings |
| Embedding normalization | $\ell_2$-normalized unit vectors |
| Distance interpretation | Euclidean distance on normalized embeddings, equivalent to cosine-based similarity |
| Number of clusters | `n_clusters=2` |

> The final model uses **two clusters** because it produced the most interpretable semantic grouping at a small \(k\) value.

#### < Tuning results >

> Although the selected solution is meaningful to interpret, it should not be viewed as evidence of strongly separated cluster structure. The silhouette diagnostics show that many reviews are closer to a different cluster than their assigned cluster, and performance declines substantially once \(k>3\).
>
> Compared with TF-IDF K-Means, the SBERT representation still provides a practical improvement: it groups reviews by contextual meaning rather than exact word overlap. The two-cluster solution is therefore used as the most actionable semantic baseline, while recognizing that individual reviews can contain multiple overlapping concerns.