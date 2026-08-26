#### < Final findings >

> Customer reviews do not naturally divide into sharply separated, single-topic groups. Both K-Means approaches showed weak cluster separation because individual reviews often discuss several concerns at once. The final LDA model better matched this structure by allowing each review to contain a mixture of topics.
>
> The three-topic LDA solution produced the clearest summary of negative feedback:
> 
> - Service mistakes and unsatisfactory haircut quality
> - Wait times and the overall in-salon appointment process
> - Unprofessional staff behavior and communication
> 
> These themes were coherent, interpretable, and consistent with the broader patterns observed in the SBERT clustering results.

#### < Business implications >

> The findings suggest three practical areas for improvement:
> 
> - Strengthen quality-control practices for haircut and service outcomes.
> - Improve appointment flow, check-in procedures, and communication about wait times.
> - Provide staff coaching on professionalism, respectful communication, and customer-service standards.
> 
> Because reviews may contain multiple concerns, addressing only one issue may not fully improve the customer experience. Combining service-quality improvements with better appointment management and staff interactions is likely to have the greatest impact.

#### < Limitations >

> - The analysis uses reviews from one anonymous business in the beauty and hair-care industry, so findings may not generalize to other businesses or industries.
> - Only reviews rated 3 stars or below were analyzed; the models do not explain the factors associated with positive experiences.
> - K-Means forces each review into one cluster, even when multiple concerns are present.
> - Topic labels require human interpretation and may change with different preprocessing, vocabulary filters, or model settings.

#### < Future work >

> - Compare negative-review topics with themes in positive reviews to identify drivers of both dissatisfaction and satisfaction.
> - Add/Remove domain-specific vocabulary and preprocessing to improve topic quality.
> - Evaluate alternative topic models and embedding-based methods that better capture overlapping themes.
> - Track topic prevalence over time, by location, or by rating to identify emerging operational issues and prioritize interventions.