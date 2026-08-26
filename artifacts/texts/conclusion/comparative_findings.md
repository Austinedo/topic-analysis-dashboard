> The three modeling approaches show that negative customer reviews contain recurring operational concerns, but they differ substantially in how clearly those concerns can be identified.

| Method | What it captured | Evaluation | Key takeaway |
|---|---|---|---|
| TF-IDF + K-Means | Similar words and phrases across reviews | WCSS did not show a clear elbow, silhouette scores were uniformly low, and cluster keywords overlapped substantially | Lexical features produced weakly separated and difficult-to-interpret clusters |
| SBERT + K-Means | Semantic similarity between review meanings | Cluster separation remained limited, with many negative silhouette values, but small-\(k\) clusters were more interpretable | Semantic embeddings improved grouping, separating broad concerns about staff conduct and service quality |
| LDA | Overlapping topics within and across reviews | The three-topic solution produced high C_v and UMass coherence and clear topic themes | LDA provided the most coherent and interpretable representation of customer concerns |

> Across the models, the most consistent complaint patterns were poor service and haircut quality, frustrating wait times or appointment processes, and unprofessional or disrespectful staff interactions. The agreement between SBERT and LDA increases confidence that these are meaningful underlying issues rather than artifacts of one modeling method.