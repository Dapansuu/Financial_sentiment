# EDA Report for `final_3.csv`

- Rows: **13559**
- Columns: **8**
- Labels: **negative, neutral, positive**

## 1) Data quality
- Missing `sentence`: **0**
- Missing `sentiment`: **0**
- Fully duplicated rows: **1795**
- Duplicated sentences (ignoring label): **1927**
- Sentences with conflicting labels: **132**

## 2) Class balance
- negative: **4260** (31.42%)
- neutral: **4578** (33.76%)
- positive: **4721** (34.82%)

## 3) Text length
- Mean words per sentence: **14.91**
- Median words per sentence: **11**
- 90th percentile: **29** words
- 95th percentile: **35** words
- 99th percentile: **46** words
- Maximum: **81** words

## 4) Financial-text cues
- Rows containing digits: **7295** (53.80%)
- Rows containing `%`: **1696** (12.51%)
- Rows containing currency cues (`Rs`, `crore`, `$`, etc.): **2348** (17.32%)
- Approx. lowercase token vocabulary size: **14164**

## 5) BI-LSTM preparation notes
- Remove exact duplicate rows before splitting.
- Deduplicate identical sentences across train/validation/test, or the model will get leakage.
- Investigate the conflicting-label sentences and either fix them manually or drop them.
- Keep numbers, `%`, and currency units. They are likely useful for finance sentiment.
- Avoid aggressive stopword removal. BI-LSTMs learn context from sequence order.
- Use stratified splitting due to mild class imbalance.
- A max sequence length around **35 to 40 tokens** should cover most sentences; **46** covers ~99%.
- Use `oov_token` in the tokenizer and reserve padding/truncation carefully.
- Consider class weights only if performance is notably worse on one class.
- Check whether headlines and long descriptive sentences should be modeled together or filtered separately.

## 6) Useful files
- `conflicting_sentences.csv` -> all sentences that appear with more than one label
- `top_terms.csv` -> class-wise frequent unigrams and bigrams
- `class_distribution.png`, `word_length_distribution.png`, `word_length_by_sentiment.png`