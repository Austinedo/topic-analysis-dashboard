> Using the selected LDA configuration with `num_topics = 3` and `λ = 0` on the interactive visualization, the model identified three recurring themes in negative customer reviews. Unlike K-Means, LDA allows a review to contribute to more than one topic, so these results represent overlapping complaint patterns rather than mutually exclusive clusters.

| Topic | Main theme | Interpretation |
|---|---|---|
| Topic 1 | Service mistakes and unsatisfactory haircut quality | Reviews in this topic describe poor service outcomes, uneven or unsatisfactory haircuts, and frustration or disrespect during the visit. Customers often report leaving early, not returning, or discouraging others from visiting. |
| Topic 2 | Wait times and the in-salon service process | This topic centers on waiting, being attended to, customer service, and feeling uncared for during the appointment process. It reflects dissatisfaction with the overall in-salon experience, not only the final service outcome. |
| Topic 3 | Unprofessional barber behavior and communication | Reviews in this topic emphasize inappropriate staff conduct, poor communication, and interactions that made customers feel uncomfortable, disrespected, or annoyed. |

#### < Interpretation >

> The three-topic solution provides a clear summary of the main concerns driving negative reviews: **service quality**, **the appointment process**, and **staff conduct**. The topics are supported by coherent, semantically related keywords and show clearer thematic separation than the TF-IDF and SBERT K-Means solutions.
> 
> Because LDA uses topic mixtures, it captures the fact that customer complaints often overlap. For example, one review may mention an uneven haircut, a long wait, and rude staff; LDA can assign meaningful weight to all relevant topics instead of forcing that review into one cluster.
> 
> The themes also align with the SBERT K-Means findings: staff conduct and service quality appear across both methods. This consistency strengthens confidence that these issues reflect recurring patterns in the negative-review corpus and provides an actionable focus for operational improvement.