> The TF-IDF + K-Means model was tuned to identify a useful vocabulary and a reasonable number of review clusters. The tuning process evaluated cluster counts from \(k=2\) through \(k=20\), using both the Within-Cluster Sum of Squares (WCSS) and silhouette scores.

#### < Final configuration >

| Component | Selected setting |
|---|---|
| TF-IDF vectorizer | `max_features=100` |
| Minimum document frequency | `min_df=14` |
| Maximum document frequency | `max_df=0.45` |
| K-Means clusters | `n_clusters=6` |

> The vectorizer retains up to 100 terms, removes words found in fewer than 14 reviews, and excludes terms that appear in more than 45% of reviews. This reduces the influence of extremely rare terms and broadly common words.

#### < Tuning results >

> Configurations with six or seven clusters received the strongest silhouette-score results before the cluster analysis became unstable. However, the WCSS curve did not show a distinct elbow, and silhouette scores remained low across the full range of tested values. Together, these results indicate weak separation between clusters.
>
> The selected six-cluster configuration is therefore presented as the best available tuned baseline—not as evidence of strongly defined topics. The overlap among cluster keywords suggests that TF-IDF features and hard K-Means assignments are limited when reviews contain multiple, overlapping concerns.