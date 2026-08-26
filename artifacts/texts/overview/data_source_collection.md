All data used in this analysis was collected from Google Reviews for a randomly
selected and anonymous business. Google Reviews was selected as the sole data
source because it provides an accessible, standardized, and information-rich
collection of customer feedback suitable for text analysis.

### < Collection Tool and Attribution >

> The review data was collected using the
> [Google Reviews Scraper Pro](https://github.com/georgekhananaev/google-reviews-scraper-pro)
> tool, an open-source Google Maps review-scraping project created and maintained
> by [George Khanaev](https://github.com/georgekhananaev).
>
> The tool supports extraction of Google Maps review data from a business listing,
> including review text and associated review metadata.

### < Extracted Fields >

Each extracted review record included the following fields:

- Review ID
- Location ID
- Reviewer name
- Review rating
- Number of review likes
- Reviewer profile image
- Reviewer profile URL
- Review date
- Review text
- Business-owner response

### < Privacy and Anonymization >

> To preserve the anonymity of both the business and its customers, personally
> identifiable information and business-specific identifiers were removed before
> analysis. This removed information included reviewer names, profile images,
> profile URLs, and business identifiers.
>
> The retained dataset contains only the information necessary for sentiment
> filtering and topic analysis. Throughout the analysis, the business is described
> only at the industry level. It operates within the beauty and hair-care service
> industry, which provides sufficient context for interpreting the identified
> themes while protecting the identity of the business and its customers.