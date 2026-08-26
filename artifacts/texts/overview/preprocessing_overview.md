The raw review data first underwent a general cleaning pass focused on the review-text field. HTML and web artifacts, URLs, and email addresses were removed. After this initial cleaning, the dataset was filtered to retain reviews with ratings less than or equal to 3 out of 5, focusing the analysis on negative customer feedback.

The resulting cleaned and filtered dataset served as the common input to three modeling branches. Each branch used preprocessing, feature extraction, and data representation choices tailored to the requirements of its respective modeling approach. (Refer to the `Analysis & Data Workflow` figure above for preprocessing visualization)

### < TF-IDF K-Means Branch >

> For K-Means clustering with lexical features, review text underwent additional standardization. The processing included lowercasing and removal of punctuation, digits, irrelevant character artifacts, and stopwords. The resulting cleaned text was transformed into a TF-IDF document-term matrix using scikit-learn's `TfidfVectorizer`.
> 
>The TF-IDF representation assigns each review a high-dimensional sparse vector in which terms are weighted according to their importance within the review and across the corpus. Vectorizer parameters were later tuned to adjust the document-term matrix and improve clustering performance.

### < SBERT K-Means Branch >

> For K-Means clustering with semantic features, reviews received only the initial general cleaning and rating-based filtering before embedding. The retained review text was passed directly to an SBERT transformer to obtain dense sentence embeddings.
> 
> No additional text normalization was applied before SBERT embedding generation. This preserved the original wording and stylistic nuances of each review and avoided potential distortion of meaning that could affect the resulting semantic representations.

### < LDA Topic-Modeling Branch >

>For LDA topic modeling, the text was processed similarly to the TF-IDF branch but received additional linguistic preprocessing. Reviews were tokenized, lemmatized, and filtered using both standard stopwords and a custom stopword list. N-grams were extracted to capture meaningful multiword expressions.
> 
> A keyword vocabulary dictionary was constructed from the processed corpus and iteratively tuned to support more coherent and interpretable topic keywords. The processed corpus and dictionary provided the bag-of-words representation used as input to the LDA model.