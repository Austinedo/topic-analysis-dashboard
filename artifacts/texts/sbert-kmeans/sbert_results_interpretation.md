#### < Review Clustering Results >

> Using the selected SBERT + K-Means configuration, the negative reviews were divided into **two semantic clusters**. Reviews were assigned based on similarity in their SBERT embeddings, and the examples below are the reviews closest to each cluster's centroid.

| Cluster | Number of Reviews in Cluster | Representative reviews | Interpretation |
|----|----|------|----|
| Cluster 0 | 133 | “Rude employees, very bad experience!”<br><br>“Very bad service I had to walk out.”<br><br>A review describing a staff member making inappropriate jokes, mispronouncing the customer's name, and behaving unprofessionally. | **Unprofessional staff conduct.** This group centers on rude, inappropriate, or disrespectful interactions with employees. |
| Cluster 1 | 329 | A review describing uneven haircuts, feeling rushed through the appointment, and dissatisfaction with the result.<br><br>A review describing poor treatment, a stylist's attitude, and refusal to provide service.<br><br>“It was the worst haircut experience ever. The barber was ready to listen to what style I want. The staff was very rude.” | **Service quality and overall experience.** This group emphasizes poor haircut outcomes, rushed service, unsatisfactory treatment, and negative appointment experiences. |

#### < Interpretation >

> The two-cluster SBERT solution provides a more meaningful separation than the TF-IDF K-Means result. Rather than relying on exact keyword overlap, SBERT groups reviews by contextual meaning. This allows complaints expressed with different language to be placed together when they describe a similar underlying experience.
>
> Cluster 0 captures reviews primarily focused on staff behavior, especially rudeness, inappropriate conduct, and disrespectful communication. Cluster 1 is broader and centers on service quality, including poor haircut results, rushed appointments, and dissatisfaction with the overall visit.
>
> The clusters still overlap in practice. Many reviews combine staff behavior and service-quality concerns, and K-Means must assign each review to only one cluster. Therefore, this result is best interpreted as two broad, actionable complaint themes—not as completely separate topics. The improved interpretability relative to TF-IDF supports the use of semantic embeddings, while the remaining overlap motivates multi-topic approaches such as LDA.